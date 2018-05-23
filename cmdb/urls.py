# coding=utf-8
#

from django.conf.urls import url

from host import *  # host, a10
# from app import *  # app,
# from balance import *
# from views import *  # es, user, 证书
# from zabbix import zabbix_tomcat_app
# from dk import *
# from appsh import *


urlpatterns = [

    url(r'^host/add', host_add, name="host_add"),
    url(r'^host/del', host_del, name="host_del"),
    url(r'^host/alldel', host_alldel, name="host_alldel"),
    url(r'^host/(?P<id>\d+)/$', host_edit, name="host_edit"),
    # url(r'^group',  Group.as_view(), name="group"),
    url(r'^host', host, name="host"),
    # url(r'^(host)',  asset, name="host"),

    url(r'^webssh', WebSSH.as_view(), name="webssh"),
    url(r'^cmdrun', CmdRun.as_view(), name="cmdrun"),


]
