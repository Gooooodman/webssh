# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.forms import widgets

from cmdb import models
from forms import HostForm

from readonly.addreadonly import ReadOnlyAdmin, ReadOnlyEditAdmin, MyAdmin as MyAdmin
from suit import apps
# 表单编辑界面input等默认宽度为col-lg-7，有些窄，改为col-lg-9
apps.DjangoSuitConfig.form_size['default'] = apps.SUIT_FORM_SIZE_XXX_LARGE

# import types
# @classmethod
# def addMethod(cls, func):
#     return setattr(cls, func.__name__, types.MethodType(func, cls))


# from django.contrib import auth
# admin.site.unregister(auth.models.User)


# @admin.register(auth.models.User)
# class MyUserAdmin(auth.admin.UserAdmin):
#     # 自定义auth.User后台版面
#     def __init__(self, model, admin_site):
#         self.suit_form_tabs = [('/tab_1', 'name1'), ('/tab_2', 'name2'), ]
#         super(self.__class__, self).__init__(model, admin_site)


@admin.register(models.HostGroup)
class HostGroup_admin(MyAdmin):

    list_display = ('name', 'ip', 'desc')


# class Host_User_Inline(admin.TabularInline):
#     model = models.Host_User


@admin.register(models.Host)
class Host_admin(MyAdmin):
    # inlines = [
    #     Host_User_Inline,
    # ]
    form = HostForm
    list_display = ('name', 'hostname', 'ip', 'group', 'tomcat_ver', 'jdk_ver', 'changetime')
    search_fields = ('name', 'hostname', 'ip', 'tomcat_ver', 'jdk_ver')

    list_filter = ('group', 'asset_type', 'tomcat_ver', 'jdk_ver')
    # filter_horizontal = ('app',)
    fieldsets = [
        ('基础信息', {'fields': ['name', 'hostname', 'ip', 'other_ip', 'port', 'group', 'usergroup', 'tomcat_ver', 'jdk_ver', 'ssh_user', 'ports']}),
        ('软硬件信息', {'fields': ['os', 'kernel', 'cpu_model', 'cpu_num', 'memory', 'disk', 'vendor', 'sn'], }),
        ('业务信息', {'fields': ['status', 'asset_type', 'machine', 'buydate', 'position', 'sernumb', 'sercode', 'admin', ], 'classes': ['collapse'], }),
        ('其它信息', {'fields': ['createtime', 'agenttime', 'tomcat', 'text', ], }),
    ]

    def get_readonly_fields(self, request, obj=None):
        readonly_fields = list(super(self.__class__, self).get_readonly_fields(request, obj=None))
        # print readonly_fields,33333333333

        readonly_fields.append('createtime')
        readonly_fields.append('agenttime')
        # print readonly_fields
        return readonly_fields


# @admin.register(models.Balance)
# class Balance_admin(MyAdmin):
#     form = BalanceForm
#     list_display = ('name', 'vip', 'info', 'ptype', 'changetime')
#     search_fields = ('name', 'vip')
#     filter_horizontal = ('host', 'a10')  # 仅用于多对多字段，提供搜索框。filter_vertical为垂直布局


from forms import SshUserForm


@admin.register(models.SshUser)
class SshUser_admin(MyAdmin):
    form = SshUserForm
    list_display = ('name', 'username', 'password', 'changetime', 'text')
    search_fields = ('name', 'username')


# # from guardian.admin import GuardedModelAdmin
# @admin.register(models.App)
# class App_admin(MyAdmin):
#     form = AppForm
#     list_display = ('name', 'appname', 'createtime', 'state')
#     # filter_horizontal=('host',)


# @admin.register(models.App_Log)
# class App_Log_admin(ReadOnlyAdmin):
#     list_display = ('host', 'name', 'do', 'user', 'path', 'nod', 'createtime')
#     search_fields = ('host__name', 'host__ip', 'do')


# @admin.register(models.ES)
# class ES_admin(MyAdmin):
#     list_display = ('name', 'cluster', 'node', 'host', 'port')
#     search_fields = ('name', 'host__name', 'host__ip')


# @admin.register(models.Cert)
# class Cert_admin(MyAdmin):
#     list_display = ('name', 'users', 'apps', 'exp_date', 'path')
#     search_fields = ('name', 'apps')
#     filter_horizontal = ('send_user', )

#     # def get_readonly_fields(self, request, obj=None):
#     #     readonly_fields = list(super(self.__class__, self).get_readonly_fields(request, obj=None))

#     #     readonly_fields.append('send_date')
#     #     return readonly_fields


# @admin.register(models.Grep)
# class Grep_admin(ReadOnlyEditAdmin):
#     list_display = ('name', 'key', 'lines', 'case', 'file', 'createtime')
#     search_fields = ('key', )
#     filter_horizontal = ('host',)
#     # fields=('name', 'key', 'lines', 'case', 'file', 'host')

#     def get_readonly_fields(self, request, obj=None):
#         fs = list(super(self.__class__, self).get_readonly_fields(request, obj))
#         if not obj:
#             # 添加时，字段和user只读
#             fs.extend(['cmd', 'user'])
#         return fs

#     def save_model(self, request, obj, form, change):
#         # 自动设置用户和CMD
#         obj.user = request.user
#         case = ' -' if form.cleaned_data.get('case', 1) else '-i'
#         lines = form.cleaned_data.get('lines', 10)
#         key = form.cleaned_data['key']
#         file = form.cleaned_data['file']

#         cmd = 'grep --colour=auto %sC%d %s %s ' % (case, lines, key, file)
#         host = form.cleaned_data.get('host', [])
#         # print cmd, host, 88888,change
#         if change:
#             # 编辑
#             cmd_obj = obj.cmd
#             cmd_obj.user = obj.user
#             cmd_obj.cmd = cmd
#             cmd_obj.host.set(host)
#             cmd_obj.save()
#         else:
#             # 新建
#             c = models.CMD(name=obj.name, cmd=cmd, user=obj.user)
#             c.save()
#             c.host.set(host)
#             obj.cmd = c

#         obj.save()


@admin.register(models.CMD)
class CMD_admin(ReadOnlyAdmin):
    list_display = ('cmd', 'ctype', 'createtime', 'end')
    search_fields = ('cmd', )
    filter_horizontal = ('host',)
    list_filter = ('ctype', )


@admin.register(models.CMD_Log)
class CMD_Log_admin(ReadOnlyAdmin):
    list_display = ('cmd', 'host', 'createtime')
    search_fields = ('cmd__cmd', 'host__ip')
    suit_form_size = {'default': apps.SUIT_FORM_SIZE_FULL}  # 加宽表单编辑界面input等宽度


@admin.register(models.SH)
class SH_admin(MyAdmin):
    list_display = ('name', 'fname', 'sh', 'createtime')
    search_fields = ('fname', 'name')

    list_filter = ('sh',)


# @admin.register(models.AppFiles)
# class AppFiles_admin(ReadOnlyAdmin):
#     list_display = ('host', 'cmd_id', 'createtime', 'changetime')
#     search_fields = ('host__ip', 'host__name', )


# @admin.register(models.A10)
# class A10_admin(MyAdmin):
#     form = A10Form
#     list_display = ('name', 'url', 'username', 'password', 'createtime')
#     search_fields = ('name', 'username')


# from django.contrib import auth


# class UserProfileInline(admin.StackedInline):
#     model = models.UserProfile
#     max_num = 1
#     can_delete = False


# class UserAdmin(auth.admin.UserAdmin):
#     inlines = [UserProfileInline, ]

# admin.site.unregister(auth.models.User)
# admin.site.register(auth.models.User, UserAdmin)


# @admin.register(models.Node)
# class Node_admin(MyAdmin):
#     list_display = ('app', 'host', 'node', 'txt', )
#     search_fields = ('app__name', 'host__name')


# # @admin.register(models.H3C_CMD)
# # class H3C_CMD_admin(MyAdmin):
# #     list_display = ('name', 'cmd', 'createtime', )
# #     search_fields = ('cmd', )

# @admin.register(models.Tomcat_Log)
# class Tomcat_Log_admin(ReadOnlyAdmin):
#     list_display = ('ip', 'dotype', 'appname', 'node', 'createtime', )
#     search_fields = ('ip', 'appname')


# @admin.register(models.Docker)
# class Docker_admin(MyAdmin):
#     list_display = ('name', 'ip', 'port', 'tls', )
#     search_fields = ('ip', 'name')


# @admin.register(models.SshUserCheck)
# class SshUserCheck_admin(MyAdmin):
#     list_display = ('host', 'password', 'error', 'createtime', )
#     search_fields = ('host',)


# @admin.register(models.AppConf)
# class AppConf_admin(MyAdmin):
#     form = AppConfForm
#     list_display = ('name', 'conf', 'value', 'changetime', )
#     search_fields = ('name',)


# class AppConFileKey_Inline(admin.TabularInline):
#     def __init__(self, *args, **kwargs):
#         # 设置verbose_name_plural为verbose_name
#         super(AppConFileKey_Inline, self).__init__(*args, **kwargs)
#         self.opts.verbose_name_plural = self.opts.verbose_name

#     model = models.AppConFileKey
#     # min_num = 5
#     fields = ['key', 'value', 'text']
#     search_fields = ('key', 'confile')


# @admin.register(models.AppConFile)
# class AppConFile_admin(MyAdmin):
#     inlines = [
#         AppConFileKey_Inline,
#     ]
#     list_display = ('name', 'app', 'confile', 'changetime', )
#     search_fields = ('confile', 'name')


# @admin.register(models.AppSH)
# class AppSH_admin(MyAdmin):
#     list_display = ('file', 'app', 'changetime', )
#     search_fields = ('app__name', 'app__appname')
#     filter_horizontal = ('confile',)

#     def get_fields(self, request, obj=None):
#         """
#         Hook for specifying fields.
#         """
#         if obj:
#             # 编辑页面不显示修改APP
#             self.exclude = ['app', ]
#             request.app_id = obj.app.id  # 存储实例ID到request，用于页面字段queryset过滤，只显示符合的数据
#         else:
#             # 添加数据时，不显示脚本配置项，添加后需再编辑，以过滤confile字段数据
#             self.exclude = ['init', 'confile', 'cert', 'final']
#         return super(AppSH_admin, self).get_fields(request, obj)

#     def changeform_view(self, request, object_id=None, form_url='', extra_context={}):
#         if not object_id:
#             extra_context = {
#                 # 不显示按钮 保存
#                 'show_save': 0,
#                 'show_save_and_continue': 1,
#             }
#         # import ipdb;ipdb;ipdb.set_trace()
#         return admin.ModelAdmin.changeform_view(self, request, object_id, form_url, extra_context)

#     # def formfield_for_manytomany(self, db_field, request, **kwargs):
#     #     print db_field, request.app_id, kwargs
#     #     if db_field.name == "confile":
#     #         # kwargs['widget'] = widgets.HiddenInput
#     #         kwargs["queryset"] = models.AppConFile.objects.filter(app=request.app_id)
#     #     return super(AppSH_admin, self).formfield_for_manytomany(db_field, request, **kwargs)

#     def get_field_queryset(self, db, db_field, request):
#         # import ipdb;ipdb;ipdb.set_trace()
#         qs = super(AppSH_admin, self).get_field_queryset(db, db_field, request)
#         if db_field.name == "confile" and request.method == 'GET':
#             if not qs:
#                 qs = models.AppConFile.objects.all()
#             # 过滤数据，不显示其它APP专用配置
#             # kwargs['widget'] = widgets.HiddenInput
#             try:
#                 # APP专用的文件配置
#                 cf_app = qs.filter(app=request.app_id)
#             except:
#                 print '获取APP(id:%d)专用配置失败!!!' % request.app_id
#                 cf_app = models.AppConFile.objects.none()
#             cf_all = qs.filter(app__isnull=True)  # 所有APP通用的文件配置
#             qs = cf_app.union(cf_all)  # 并集
#             # print qs, 888
#         return qs
