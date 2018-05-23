# -*- coding: utf-8 -*-


import paramiko
import socket
from channels.generic.websockets import WebsocketConsumer
try:
    import simplejson as json
except ImportError:
    import json
from django.utils.encoding import smart_unicode
from django.core.exceptions import ObjectDoesNotExist
import ast
import time

from django.core.cache import cache

from cmdb.models import HostGroup, Host, SshUser
# from sudoterminal import ShellHandler

# print 2,'webssh.consumers'
from interactive import interactive_shell

####################################
# 程序中有print u'汉字'时，需定义程序环境编码为UTF-8，否则需直接用print '汉字'，不能用u''
import sys
reload(sys)
sys.setdefaultencoding('UTF-8')  # 原默认为sys.getdefaultencoding(): ascii
####################################

# from multiprocessing import Manager
# m=Manager()
global multiple_chan
# multiple_chan = m.dict() #runworker 多进程共享变量
multiple_chan = dict()


class webterminal(WebsocketConsumer):
    ssh = paramiko.SSHClient()
    http_user = True  # 自动从HTTP获取用户(免重新登陆)
    http_user_and_session = True
    channel_session = True
    channel_session_user = True

    def connect(self, message):
        self.message.reply_channel.send({"accept": True})
        # import ipdb;ipdb.set_trace()
        # permission auth

    def disconnect(self, message):
        self.message.reply_channel.send({"accept": False})
        if multiple_chan.has_key(self.message.reply_channel.name):
            multiple_chan[self.message.reply_channel.name].close()
        self.close()

    def receive(self, text=None, bytes=None, **kwargs):
        try:
            if text:
                # print text,9999999
                data = json.loads(text)
                if data[0] == 'hostid':
                    hostid = data[1]
                    self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                    try:
                        data = Host.objects.get(id=hostid)
                        user = self.message.user
                        if not data.chk_user_prem(user, 'webssh'):
                            print '用户<%s>没有主机权限webssh_host:' % user.username, data
                            self.message.reply_channel.send({"text": json.dumps(['stdout', u'\033[1;3;31m非法操作！当前用户无主机webssh_host权限。\033[0m'])}, immediately=True)
                            self.message.reply_channel.send({"accept": False})
                            return
                        ip = data.ip

                    except ObjectDoesNotExist:
                        self.message.reply_channel.send({"text": json.dumps(['stdout', '\033[1;3;31mConnect to server! Server ip doesn\'t exist!\033[0m'])}, immediately=True)
                        self.message.reply_channel.send({"accept": False})
                        return

                    username, password = data.get_ssh_user()
                    try:
                        port = data.port
                        method = 'password'
                        if method == 'password':
                            self.ssh.connect(ip, port=port, username=username, password=password, timeout=3)
                        else:
                            key = data.key
                            self.ssh.connect(ip, port=port, username=username, key_filename=key, timeout=3)
                    except socket.timeout:
                        self.message.reply_channel.send({"text": json.dumps(['stdout', '\033[1;3;31mConnect to server time out\033[0m'])}, immediately=True)
                        self.message.reply_channel.send({"accept": False})
                        return
                    except Exception as e:
                        self.message.reply_channel.send(
                            {"text": json.dumps(['stdout', '\033[1;3;31mError: %s (HOST: %s, SSH_User: %s)\033[0m' % (e, ip, username)])}, immediately=True)
                        self.message.reply_channel.send({"accept": False})
                        return

                    chan = self.ssh.invoke_shell(term='xterm', width=90, height=32,)
                    # cache.set('multiple_chan', chan, timeout=3600)

                    multiple_chan[self.message.reply_channel.name] = chan

                    print 'chan------:', chan
                    interactive_shell(chan, self.message.reply_channel.name)

                elif data[0] in ['stdin']:  # ,'stdout'
                    print data
                    # print 111
                    # import ipdb;ipdb.set_trace()
                    # print 222

                    # multiple_chan = cache.get('multiple_chan', {})
                    if multiple_chan.has_key(self.message.reply_channel.name):
                        multiple_chan[self.message.reply_channel.name].send(json.loads(text)[1])
                        # print 333
                    else:
                        self.message.reply_channel.send({"text": json.dumps(['stdout', '\033[1;3;31mSsh session is terminate or closed!\033[0m'])}, immediately=True)
                else:
                    self.message.reply_channel.send({"text": json.dumps(['stdout', '\033[1;3;31mUnknow command found!\033[0m'])}, immediately=True)
            elif bytes:
                if multiple_chan.has_key(self.message.reply_channel.name):
                    multiple_chan[self.message.reply_channel.name].send(json.loads(bytes)[1])
        except socket.error:
            if multiple_chan.has_key(self.message.reply_channel.name):
                multiple_chan[self.message.reply_channel.name].close()
        except Exception, e:
            import traceback
            print traceback.print_exc()


# class CommandExecute(WebsocketConsumer):
#     http_user = True
#     http_user_and_session = True
#     channel_session = True
#     channel_session_user = True

#     def connect(self, message):
#         self.message.reply_channel.send({"accept": True})
# permission auth

#     def disconnect(self, message):
#         self.message.reply_channel.send({"accept":False})
#         self.close()

#     def receive(self,text=None, bytes=None, **kwargs):
#         try:
#             if text:
#                 data = json.loads(text)
#                 if isinstance(data,list):
#                     return
#                 if data.has_key('parameter'):
#                     parameter = data['parameter']
#                     taskname = parameter.get('taskname',None)
#                     groupname = parameter.get('groupname',None)
#                     ip = parameter.get('ip',None)
#                     if taskname and ip and groupname:
#                         server_list = [ ip ]
#                     elif taskname and not ip and not groupname:
#                         server_list = []
#                         [server_list.extend([ server.ip for server in ServerGroup.objects.get(name=group.name).servers.all() ]) for group in CommandsSequence.objects.get(name = taskname).group.all() ]
#                     elif taskname and groupname and not ip:
#                         server_list = [ server.ip for server in ServerGroup.objects.get(name=groupname).servers.all() ]
#                     commands = json.loads(CommandsSequence.objects.get(name = taskname).commands)
#                     if isinstance(commands,(basestring,str,unicode)):
#                         commands = ast.literal_eval(commands)
# Run commands
#                     for server_ip in server_list:

#                         self.message.reply_channel.send({"text":json.dumps(['stdout','\033[1;3;31mExecute task on server:%s \033[0m' %(smart_unicode(server_ip)) ] )},immediately=True)

# get server credential info
#                         serverdata = ServerInfor.objects.get(ip=server_ip)
#                         port = serverdata.credential.port
#                         method = serverdata.credential.method
#                         username = serverdata.credential.username
#                         if method == 'password':
#                             credential = serverdata.credential.password
#                         else:
#                             credential = serverdata.credential.key


# do actual job
#                         ssh = ShellHandler(server_ip,username,port,method,credential,channel_name=self.message.reply_channel.name)
#                         for command in commands:
#                             ssh.execute(command)
#                         del ssh

#                 else:
# illegal
#                     self.message.reply_channel.send({"text":json.dumps(['stdout','\033[1;3;31mIllegal parameter passed to the server!\033[0m'])},immediately=True)
#                     self.close()
#             if bytes:
#                 data = json.loads(bytes)
#         except Exception,e:
#             import traceback
#             print traceback.print_exc()
#             self.message.reply_channel.send({"text":json.dumps(['stdout','\033[1;3;31mSome error happend, Please report it to the administrator! Error info:%s \033[0m' %(smart_unicode(e)) ] )},immediately=True)
