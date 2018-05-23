# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
# from django.utils.timezone import now, localdate
from datetime import datetime, timedelta

from django.contrib.auth.models import User, Group
import traceback
from Crypto.Cipher import AES
import base64
import paramiko


# from django.db.models.options import Options
# old_contribute_to_class = Options.contribute_to_class


# def new_contribute_to_class(instance, cls, name):
#     # 设置verbose_name_plural为verbose_name
#     old_contribute_to_class(instance, cls, name)
#     instance.verbose_name_plural = instance.verbose_name
# models.options.Options.contribute_to_class = new_contribute_to_class


class HostGroup(models.Model):
    name = models.CharField(u"组名/区域", max_length=30, unique=True)
    ip = models.CharField(u"IP匹配", help_text='IP开头字符，比如Core组IP为10.2.4.开头。用于客户端脚本添加新主机时自动设置组，不支持通配符', max_length=20, default='', blank=True)
    desc = models.CharField(u"描述", max_length=100, null=True, blank=True)

    class Meta:
        ordering = ['name']
        verbose_name = '主机分组'

    def __unicode__(self):
        return self.name

    @staticmethod
    def get_group(ip):
        # 客户端脚本自动添加主机时，自动设置主机所属组(安全区域)

        groups = HostGroup.objects.exclude(ip='').order_by('-ip')
        group_id = 0
        for group in groups:
            if ip.startswith(group.ip):
                group_id = group.id
                break
        return group_id


def get_AES(password, encode=1):
    # 密码加密

    KEY = '1234567890123456'
    BLOCK_SIZE = 16  # AES.block_size
    PADDING = chr(20)  # 'ý' #未满16*n时，补齐字符chr(253)

    pad = lambda s: s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * PADDING
    EncodeAES = lambda c, s: base64.b64encode(c.encrypt(pad(s)))
    DecodeAES = lambda c, e: c.decrypt(base64.b64decode(e)).rstrip(PADDING)
    cipher = AES.new(KEY)
    if encode:
        # 密码加密，用于内部保存
        # try:
        #     decoded = DecodeAES(cipher, password)
        # return  password #未修改密码直接提交，原字符已为密文，无需再次加密
        # except:
        #     pass
        return EncodeAES(cipher, password)  # 修改了密码，重新加密为密文
    else:
        # 密码解密，用于外部提取
        try:
            return DecodeAES(cipher, password)
        except:
            print 'Error: AES密码解密失败！！'
            return ''


class SshUser(models.Model):
    # 各服务器SSH登陆用户
    name = models.CharField(u"名称", max_length=50, default='', help_text='标识名称，当不同服务器使用相同的SSH账号名，但密码不同时，此项名称可进行区分。')
    username = models.CharField(u"SSH账号", max_length=50, default='', )
    password = models.CharField(u"密码", max_length=50, default='', null=True, blank=True, help_text='若不想修改原密码，不用设置此项')
    changetime = models.DateTimeField('最后修改', auto_now=True, blank=True, null=True)
    text = models.TextField(u"备注信息", default='', null=True, blank=True)

    class Meta:
        ordering = ['name']
        verbose_name = '主机SSH用户'
        unique_together = [('name', 'username'), ]

    def __unicode__(self):
        return '%s - %s' % (self.name, self.username)

    def save(self, *args, **kwargs):

        if self.password:
            password_aes = get_AES(password=self.password)  # AES加密
            self.password = password_aes
        elif self.id:
            del self.password  # 防止不修改密码时，提交的空密码覆盖原有数据
        # import ipdb;ipdb.set_trace()
        super(self.__class__, self).save(*args, **kwargs)  # Call the "real" save() method.


class Host(models.Model):
    # 虚拟机、物理机 等设备
    ASSET_STATUS = (
        (1, u"在用"),
        (2, u"备用"),
        (3, u"故障"),
        (4, u"下线"),
        (6, u"其它"),
    )

    ASSET_TYPE = (
        (1, u"物理机"),
        (2, u"虚拟机"),
        (3, u"容器"),
        (4, u"H3C交换机"),
        (6, u"其它")
    )

    name = models.CharField(max_length=100, verbose_name=u"标识名称", default='', help_text='用于人工辨别，自动脚本默认设置为主机名，可改为其它便于人员识别的名称')
    hostname = models.CharField(max_length=50, verbose_name=u"主机名/计算机名", unique=True, help_text='关键字段，请谨慎修改')  # 服务器数据以计算机名为锚，以验证身份不重复添加数据
    ip = models.GenericIPAddressField(u"管理IP", max_length=15, help_text='若有多个IP且主机名无指定解析则默认为0.0.0.0，请在客户端/etc/hosts中设置其主机名对应IP解析')
    port = models.IntegerField(verbose_name='ssh端口', null=True, blank=True, default=22)
    other_ip = models.CharField(u"其它IP", max_length=100, null=True, blank=True)
    group = models.ForeignKey(HostGroup, verbose_name=u"组/安全区域", default=1, on_delete=models.SET_NULL, null=True, blank=True)
    # asset_no = models.CharField(u"资产编号", max_length=50, null=True, blank=True)
    # domain = models.CharField(u"安全区域", max_length=20, null=True, blank=True)
    status = models.SmallIntegerField(u"设备状态", choices=ASSET_STATUS, default=1, null=True, blank=True)
    asset_type = models.SmallIntegerField(u"设备类型", choices=ASSET_TYPE, default=1, null=True, blank=True)
    # 注意，django 1.11对postgresql 8.*低版本支持不好，ForeignKey字段有修改就会SQL报错 array_agg(attname ORDER BY rnum)
    machine = models.ForeignKey('self', verbose_name=u"所属物理机", limit_choices_to={'asset_type': 1},
                                on_delete=models.SET_NULL, null=True, blank=True, help_text='设备类型为虚拟机/容器时，设置所在物理机')
    os = models.CharField(u"操作系统", max_length=100, default='', null=True, blank=True)
    # vendor = models.CharField(u"设备厂商", max_length=50, null=True, blank=True)
    cpu_model = models.CharField(u"CPU型号", max_length=100, default='', null=True, blank=True)
    cpu_num = models.CharField(u"CPU数量", max_length=100, default='', null=True, blank=True, help_text='物理核个数, 逻辑核个数，(intel高端CPU带超线程技术)')
    memory = models.CharField(u"内存大小", max_length=30, default='', null=True, blank=True)
    disk = models.CharField(u"硬盘信息", max_length=255, default='', null=True, blank=True)
    vendor = models.CharField(u"供应商", max_length=150, default='', null=True, blank=True)
    sn = models.CharField(u"主机序列号", max_length=150, default='', null=True, blank=True)
    ports = models.TextField(u"监听端口", default='', null=True, blank=True, help_text='主机上处于监听状态的TCP和UDP端口')

    createtime = models.DateTimeField('创建时间',
                                      auto_now_add=True,
                                      # default=now,
                                      blank=True, null=True)
    changetime = models.DateTimeField('修改时间', auto_now=True, blank=True, null=True)
    agenttime = models.DateTimeField('配置更新', blank=True, null=True, help_text='最近一次主机客户端自动脚本运行更新软硬件信息的时间')

    usergroup = models.ManyToManyField(Group, verbose_name='网站用户组', blank=True, help_text='网站哪些用户组能对当前主机进行操作')
    user = models.ManyToManyField(User, verbose_name='网站用户权限', blank=True,
                                  # through='Host_User',  # 行级别的权限控制，人工录入时麻烦，比较困难实现快速批量设置主机清单
                                  help_text='网站哪些用户能对当前主机进行操作，超级用户直接有操作权限')
    ssh_user = models.ForeignKey(SshUser, verbose_name='SSH终端用户', on_delete=models.SET_NULL, null=True, blank=True, help_text='当前主机的SSH用户，用于ssh连接执行命令或终端WEB SSH')

    buydate = models.DateField('购买日期', default=datetime.today, blank=True, null=True)
    position = models.CharField(u"所处位置", max_length=250, default='', null=True, blank=True)
    sernumb = models.CharField(u"服务编号", max_length=150, default='', null=True, blank=True)
    sercode = models.CharField(u"服务代码", max_length=150, default='', null=True, blank=True)
    admin = models.ForeignKey(User, verbose_name='管理人', related_name='user_set2', null=True, blank=True, help_text='负责人直接有(当前主机/名下主机)操作权限')

    tomcat = models.CharField(max_length=100, verbose_name=u"Tomcat目录", default='/data/app/tomcat')
    tomcat_ver = models.CharField(max_length=50, verbose_name=u"Tomcat版本", default='', blank=True)
    jdk_ver = models.CharField(max_length=50, verbose_name=u"JDK版本", default='', blank=True)
    kernel = models.CharField(max_length=60, verbose_name=u"系统内核版本", default='', blank=True)

    # idc = models.ForeignKey(Idc, verbose_name=u"所在机房", on_delete=models.SET_NULL, null=True, blank=True)
    # position = models.CharField(u"所在位置", max_length=100, null=True, blank=True)
    # info = models.CharField(u"应用信息", max_length=200, default='', null=True, blank=True)
    text = models.TextField(u"备注信息", default='', null=True, blank=True)

    class Meta:
        permissions = (
            # 实现表级别的权限控制
            ("deploy_host", "Can deploy host"),    # APP部署
            ("webssh_host", "Can webssh host"),    # 终端登陆
            ("grep_host", "Can grep host"),      # 执行日志搜索
            ("run_sh_host", "Can run_sh host"),    # 执行常用命令
            ("run_cmd_host", "Can run_cmd host"),   # 执行自定义命令
            ("other_do_host", "Can other_do host"),  # 执行其它操作，如ES节点索引
        )
        ordering = ['group', 'ip']
        verbose_name = '主机'

    def __unicode__(self):
        return '%s - %s' % (self.name, self.ip)

    @staticmethod
    def newhost(kwargs):
        # 添加/修改host数据
        hostname = kwargs['hostname']
        host = Host.objects.filter(hostname=hostname)
        try:
            if host:
                host = host[0]
                # print '已有记录',hostname,'更新主机信息'
                kwargs.pop('hostname')
                text = kwargs.get('text', '')
                if text:
                    kwargs['text'] = '%s\r\n%s' % (host.text, text)  # 备注信息只在原基础信息上追加
                for k, v in kwargs.items():
                    setattr(host, k, v)
                host.agenttime = datetime.today()
                host.save()
            else:
                # 添加新主机
                hostname, ip = kwargs.get('hostname', ''), kwargs.get('ip', '')
                kwargs['name'] = kwargs.get('name', '%s' % (hostname, ))  # 当标识名未提供，则填入计算机名。
                kwargs['asset_type'] = kwargs.get('asset_type', 2)  # 默认为虚拟机类型
                kwargs['agenttime'] = datetime.today()  # 配制更新日期

                group_id = kwargs.get('group_id', HostGroup.get_group(ip))

                if group_id:
                    kwargs['group_id'] = group_id

                Host(**kwargs).save()
            return 1
        except:
            print(traceback.format_exc())
            return 0

    def get_ssh_user(self):
        # 获取某台主机SSH用户/密码

        ssh_user = self.ssh_user
        if not ssh_user:
            ssh_users = SshUser.objects.filter(username='app')  # 下面取id最小的app用户
            if ssh_users:
                ssh_user = ssh_users[0]
            else:
                print 'Error: SshUser数据表为空，新安装CMDB？'
                return '', ''
        username = ssh_user.username
        password = get_AES(password=ssh_user.password, encode=0)
        return username, password

    @staticmethod
    def get_user_host(user):
        # 获取用户有操作权限的所有主机

        hosts = Host.objects.all()
        if user.is_superuser:
            return hosts

        hosts1 = hosts.filter(user=user)  # 已设置用户为操作用户
        hosts2 = hosts.filter(admin=user)
        hosts3 = hosts.filter(machine__in=hosts2)  # 负责人有物理机名下虚拟机权限
        # print hosts2.union(hosts3),7777

        hosts4 = hosts.filter(usergroup__in=user.groups.all())  # 已设置用户所属组有操作权限
        # hosts4 = []
        return hosts1 | hosts2 | hosts3 | hosts4

    def chk_user_prem(self, user, perm):
        # 验证用户操作权限
        # import ipdb;ipdb.set_trace()
        if user.is_superuser:
            return 1  # 超级管理员直接有权限
        elif not user.has_perm('cmdb.%s_host' % perm):
            return 0  # 未设置用户相对应的主机权限，超级管理员无需设置而直接有权限
        elif user in self.user.all() or self.admin == user:
            return 1  # 主机有设置用户为网站操作用户/负责人
        elif self.machine and self.machine.admin == user:
            return 1  # 所属物理机负责人有操作权限

        usergroups = self.usergroup.all()
        for usergroup in usergroups:
            if user in usergroup.user_set.all():
                return 1  # 主机设置的网站用户组包含user
        return 0

    def ssh_cmd(self, cmd, ssh_timeout=10):
        # 登陆服务器执行cmd，返回('正常信息', '错误信息')
        # import ipdb;import ipdb; ipdb.set_trace()
        try:
            cmd = cmd.format(self)  # 有些为变量，比如Tomcat目录
        except:
            pass
        print cmd, 888
        ip = self.ip
        port = getattr(self, 'port', 22)
        ssh_user, ssh_pwd = self.get_ssh_user()

        if not ssh_pwd:
            return ('', 'Error: SSH User %s 异常' % ssh_user)

        s = paramiko.SSHClient()
        s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        try:
            s.connect(ip, port, ssh_user, ssh_pwd, timeout=ssh_timeout)
        except Exception as e:
            return ('', 'SSH connect error: %s' % e)

        stdin, stdout, stderr = s.exec_command(cmd)
        # stdin.write("Y")
        # msg = stdout.read().decode('utf-8'), stderr.read().decode('utf-8')
        if self.asset_type == 4:
            # H3C交换机，显示More之后内容
            stdin.write('                                                                          q')
            out = stdout.read()
            out = out.replace('  ---- More ----\x1b[16D                \x1b[16D', '')  # import pyte
        else:
            out = stdout.read()
        err = stderr.read()
        s.close()
        return out, err

    def get_ha_a10(self):
        # 获取主机的A10组

        balances = self.balance_set.all()
        a10s = set()
        for balance in balances:
            a10s = a10s | set(balance.a10.filter(state=1))
        if not a10s:
            if self.ip.startswith('10.2.4.'):
                ha = 2
            elif self.ip.startswith('10.2.12.'):
                ha = 1
            elif self.ip.startswith('10.2.14.'):
                ha = 2
            elif self.ip.startswith('10.2.16.'):
                ha = 3
            else:
                # ha = 1
                return a10s

            a10s = A10.objects.filter(ha=ha, state=1)
        a10s = [a10 for a10 in a10s]
        a10s.sort(cmp=None, key=lambda i: i.name, reverse=False)
        return a10s


# class Host_User(models.Model):
# 主机用户权限多对多中间表，实现行级别的权限控制

#     host = models.ForeignKey(Host, verbose_name=u"主机",)
#     user = models.ForeignKey(User, verbose_name=u"网站用户",)

#     deploy = models.BooleanField(verbose_name='APP部署', default=False)
#     webssh = models.BooleanField(verbose_name='连接终端', default=False)
#     sh = models.BooleanField(verbose_name='常用脚本', default=False)
#     cmd = models.BooleanField(verbose_name='自定义命令', default=False)
#     grep = models.BooleanField(verbose_name='日志搜索', default=True)
#     other = models.BooleanField(verbose_name='其它操作', default=True, help_text='比如主机ES节点索引打开/关闭等')

#     class Meta:
#         unique_together = [('host', 'user'), ]
#         verbose_name = '用户操作权限'


class SH(models.Model):
    # 常用脚本

    SH_TYPE = (
        (1, u"默认"),
        (2, u"H3C交换机"),
        (3, u"APP配置"),
    )

    name = models.CharField(max_length=100, verbose_name=u"标识名", default='')
    fname = models.CharField(max_length=100, verbose_name=u"文件名", default='', help_text='使脚本能通过URL形式来调用，http://10.2.21.34:8088/api/sh/文件名，并且通过后缀名区分py、sh脚本')
    sh = models.SmallIntegerField(u"脚本类型", choices=SH_TYPE, default=1, null=True, blank=True)
    # server = models.SmallIntegerField(u"主机类型", choices=SERVER_TYPE, default=1, null=True, blank=True)
    cmd = models.TextField(u"脚本内容", blank=True, null=True)
    text = models.TextField(u"备注", blank=True, null=True)

    createtime = models.DateTimeField('创建时间', auto_now_add=True, blank=True, null=True)

    class Meta:
        verbose_name = '常用命令/脚本'
        ordering = ['sh', 'fname']
        unique_together = [('sh', 'fname'), ]

    def __unicode__(self):
        return self.name

    def save(self, *args, **kwargs):
        #  windows、苹果换行改为Uinx
        try:
            self.cmd = self.cmd.replace('\r\n', '\n').replace('\r', '\n')
        except:
            print self.name, 'SH脚本替换换行失败，忽略!!!!!!!!'
            pass
        return super(self.__class__, self).save(*args, **kwargs)


class CMD(models.Model):
    # 命令项执行记录
    CMD_TYPE = (
        (1, u"GREP日志"),
        (2, u"常用脚本"),
        (4, u"APP配置较验"),
        (6, u"自定义命令"),
    )

    cmd = models.TextField(u"命令内容")
    ctype = models.SmallIntegerField(u"命令类型", choices=CMD_TYPE, default=1, null=True, blank=True)
    host = models.ManyToManyField(Host, verbose_name='执行主机', blank=True)
    text = models.TextField(u"备注", blank=True, null=True)

    createtime = models.DateTimeField('创建时间', auto_now_add=True, blank=True, null=True)
    user = models.ForeignKey(User, verbose_name='操作人', null=True, blank=True, )
    end = models.BooleanField(verbose_name='任务完成', default=False)

    class Meta:
        verbose_name = 'CMD记录'

    def __unicode__(self):
        return self.cmd

    @staticmethod
    def newcmd(hosts, **kwargs):
        if not hosts:
            return
        cmd = CMD(**kwargs)
        cmd.save()
        cmd.host.set(hosts)
        return cmd


# default_cmd_name = u'自定义命令'
class CMD_Log(models.Model):
    # 命令执行结果

    cmd = models.ForeignKey(CMD, verbose_name=u"命令")
    host = models.ForeignKey(Host, verbose_name='主机')
    createtime = models.DateTimeField('创建时间', auto_now_add=True, blank=True, null=True)
    text = models.TextField(u"返回信息", default='', null=True, blank=True)

    class Meta:
        verbose_name = 'CMD结果'

    def __unicode__(self):
        return '%s (%s)' % (self.cmd, self.host)

