# -*- coding: utf-8 -*-

import socket
import sys
from paramiko.py3compat import u
from django.utils.encoding import smart_unicode

try:
    import termios
    import tty
    has_termios = True
except ImportError:
    has_termios = False
    raise Exception('This project does\'t support windows system!')
try:
    import simplejson as json
except ImportError:
    import json

import threading
import time

reload(sys)
sys.setdefaultencoding('UTF-8')


def interactive_shell(chan, channel):
    if has_termios:
        # sh=threading.Thread(target=posix_shell, args=(chan,channel))
        # sh.setDaemon(True)
        # sh.start()
        posix_shell(chan, channel)
    else:
        sys.exit(1)

# from webssh.asgi import channel_layer #正式运行时daphne 不支持


def posix_shell(chan, channel):
    # print 3,'webssh.interactive'
    from webssh.asgi import channel_layer
    # channel_layer = channel_layer2()
    try:
        chan.settimeout(0.0)

        while 1:
            # 循环监视ssh终端输出，实时发给websocket客户端显示
            if not chan.recv_ready():
                time.sleep(0.1)
                continue
            try:
                x = chan.recv(1024)  # 收取ssh-tty打印信息，带着色
                while ord(x[-1]) > 127:
                    # utf8字符为3位，有时截取时结尾刚好碰到utf8字符，导致汉字被分割成二部分
                    try:
                        x += chan.recv(1)
                    except:
                        break
                print x, 888
                # import ipdb;ipdb.set_trace()
                # print 111,len(x),222,'<%s>'% x[-1]
                if len(x) == 0:
                    channel_layer.send(channel, {'text': json.dumps(['disconnect', smart_unicode('\r\n*** EOF\r\n')])})
                    break
                channel_layer.send(channel, {'text': json.dumps(['stdout', smart_unicode(x)])})  # 发送信息到web SSH显示
                # print json.dumps(['stdout',smart_unicode(x)]),555
            except socket.timeout:
                pass
            except UnicodeDecodeError, e:
                # import ipdb;ipdb.set_trace()
                print e
                lines = x.splitlines()
                for line in lines:
                    # recv(1024字节)，除乱码字符所在行外，将其它行正常显示
                    if line:
                        try:
                            channel_layer.send(channel, {'text': json.dumps(['stdout', '%s\r\n' % smart_unicode(line)])})
                        except UnicodeDecodeError, e:
                            channel_layer.send(channel, {'text': json.dumps(['stdout', 'Error: utf-8编码失败！！！\r\n%s\r\n' % smart_unicode(e)], )})

            except Exception, e:
                print 111, e, 3333
                channel_layer.send(channel, {'text': json.dumps(['stdout', 'Error: 连接意外中断.' + smart_unicode(e)], )})
                break

    finally:
        print u'连接断开..', channel
        pass
