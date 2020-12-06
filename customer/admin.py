from django.contrib import admin

# Register your models here.
from django.contrib import admin
import xadmin
from django.contrib.auth.models import Group
from django.http import HttpResponse
from django.template.response import TemplateResponse
from xadmin.util import model_ngettext

from customer.models import Manager, Apply, Audit, Hospital, UserType, User, Record, Detail
from xadmin import views
from xadmin.plugins.actions import BaseActionView
from django.utils.translation import gettext_lazy as _
from django.db.models import Q
from xadmin.layout import Fieldset, Row


class MyDelete(BaseActionView):

    # 这里需要填写三个属性
    action_name = "my_delete"    #: 相当于这个 Action 的唯一标示, 尽量用比较针对性的名字
    description = '删除所选的 %(verbose_name_plural)s'
    #: 描述, 出现在 Action 菜单中, 可以使用 ``%(verbose_name_plural)s`` 代替 Model 的名字.

    model_perm = 'change'    #: 该 Action 所需权限

    def do_action(self, queryset):
        # queryset 是包含了已经选择的数据的 queryset
        for obj in queryset:
            # obj 的操作
            obj.isDelete = True
            obj.save()


class UserAdmin(object):
    list_display = ['uid', 'uname', 'utype', 'sex', 'age', 'tel', 'money', 'address', 'isDelete']
    ordering = ["isDelete"]
    search_fields = ['uid', 'uname', 'tel']
    list_filter = ['utype', 'sex', 'address', 'isDelete']
    list_per_page = 20
    model_icon = 'fa fa-users'
    list_editable = ['uname', 'utype', 'age', 'tel', 'address']
    show_bookmarks = False
    form_layout = (
        Fieldset('账户信息',
            Row('uid', 'password', 'isDelete'),
        ),
        Fieldset('个人信息',
                 Row('uname', 'sex', ''),
                 Row('age', 'tel', ''),
                 Row('address', '', ''),
                 Row('utype', '', ''),
                 Row('money', '', ''),
                 )
    )
    # 批量导入
    # 删除重写
    actions = [MyDelete]

    # 删除屏蔽
    @staticmethod
    def has_delete_permission(request=None):
        # Disable add
        return False


class ManagerAdmin(object):

    list_display = ['mid_detail', 'mname', 'type', 'count', 'work_rate', 'isDelete']
    ordering = ['isDelete']
    search_fields = ['mid', 'mname']
    list_filter = ['type', 'isDelete']
    model_icon = 'fa fa-user'
    show_bookmarks = False

    def work_rate(self, instance):
        if instance.count == 0:
            return '-'
        else:
            return instance.right / instance.count

    work_rate.short_description = '<div class="dropdown pull-left">' \
                                   '<a class="dropdown-toggle md-opjjpmhoiojifppkkcdabiobhakljdgm_doc" ' \
                                   'data-toggle="dropdown" href="#">' \
                                   '正确率' \
                                   '</a>' \
                                   '<ul class="dropdown-menu" role="menu">' \
                                   '<li><a href="?o=count.right.isDelete" ' \
                                   'class="active md-opjjpmhoiojifppkkcdabiobhakljdgm_doc">' \
                                   '<i class="fa fa-caret-up"></i> 正序</a></li>' \
                                   '<li><a href="?o=-count.-right.isDelete" ' \
                                   'class="active md-opjjpmhoiojifppkkcdabiobhakljdgm_doc">' \
                                   '<i class="fa fa-caret-down"></i> 倒序</a></li>' \
                                   '</ul></div>'
    work_rate.is_column = True
    work_rate.allow_tags = True
    list_editable = ['mname']

    def mid_detail(self, obj):
        if Group.objects.get(user=self.request.user).name == 'manager':
            return '<a href="%s">%s</a>' % ('/xadmin/customer/audit/?_rel_mid__id__exact=' + str(obj.id), obj.mid)
        else:
            return '%s' % obj.mid
    mid_detail.allow_tags = True
    mid_detail.short_description = '<div class="dropdown pull-left">' \
                                   '<a class="dropdown-toggle md-opjjpmhoiojifppkkcdabiobhakljdgm_doc" ' \
                                   'data-toggle="dropdown" href="#">' \
                                   '账户' \
                                   '</a>' \
                                   '<ul class="dropdown-menu" role="menu">' \
                                   '<li><a href="?o=mid.isDelete" ' \
                                   'class="active md-opjjpmhoiojifppkkcdabiobhakljdgm_doc">' \
                                   '<i class="fa fa-caret-up"></i> 正序</a></li>' \
                                   '<li><a href="?o=-mid.isDelete" ' \
                                   'class="active md-opjjpmhoiojifppkkcdabiobhakljdgm_doc">' \
                                   '<i class="fa fa-caret-down"></i> 倒序</a></li>' \
                                   '</ul></div>'
    form_layout = (
        Fieldset('账户信息',
                 Row('mid', 'pw', 'isDelete'),
                 ),
        Fieldset('个人信息',
                 Row('mname', 'type', ''),
                 Row('count', 'right', ''),
                 )
    )

    # 批量导入
    # 删除重写
    actions = [MyDelete]

    # 删除屏蔽
    @staticmethod
    def has_delete_permission(request=None):
        # Disable add
        return False

    def queryset(self):
        qs = super(ManagerAdmin, self).queryset()
        if self.request.user.is_superuser:  # 超级用户可查看所有数据
            return qs
        else:
            rs = qs.filter(Q(type='2') | Q(type='3'))
            return rs  # user是IDC Model的user字段


class HospitalAdmin(object):
    list_display = ['hid', 'hname', 'isDelete']
    ordering = ['isDelete']
    model_icon = 'fa fa-hospital-o'
    search_fields = ['hid', 'hname']
    # readonly_fields = "isDelete"
    show_bookmarks = False
    list_filter = ["isDelete"]
    # 删除重写
    actions = [MyDelete]

    # 删除屏蔽
    @staticmethod
    def has_delete_permission(request=None):
        # Disable add
        return False


class UserTypeAdmin(object):
    list_display = ['utype', 'limit', 'ratio', 'change']
    model_icon = 'fa fa-user-md'
    list_editable = ['limit', 'ratio', 'change']
    show_bookmarks = False

    form_layout = (
        Row('utype', '', ''),
        Row('limit', 'ratio', 'change')
    )

    # 删除屏蔽
    @staticmethod
    def has_delete_permission(request=None):
        # Disable add
        return False
    # 增加重写


class ApplyAdmin(object):
    list_display = ['aid', 'uid', 'astatus', 'atime', 'isDelete']
    ordering = ['isDelete']
    model_icon = 'fa fa-tasks'
    list_editable = ['astatus']
    # readonly_fields = ("isDelete", "aid", "uid", 'atime')
    search_fields = ['aid', 'uid__uname']
    list_filter = ['astatus', 'atime', "isDelete"]
    show_bookmarks = False

    # @staticmethod
    # def has_add_permission(request=None):
    #     # Disable add
    #     return False

    # 删除重写
    actions = [MyDelete]

    # 删除屏蔽
    @staticmethod
    def has_delete_permission(request=None):
        # Disable add
        return False


class RecordAdmin(object):
    list_display = ['aid', 'rid', 'rtime', 'money', 'money_bx', 'msg']
    model_icon = 'fa fa-tag'
    list_editable = ['money_bx']
    # readonly_fields = ("isDelete", "aid", "rid", "rtime", "msg")
    search_fields = ['aid__aid', 'rid']
    show_bookmarks = False

    form_layout = (
        Row('aid', 'rid'),
        Row('money', 'money_bx', ''),
        Row('msg')
    )

    # @staticmethod
    # def has_add_permission (request=None):
    #     # Disable add
    #     return False

    # 删除屏蔽
    @staticmethod
    def has_delete_permission(request=None):
        # Disable add
        return False


class DetailAdmin(object):
    list_display = ['rid', 'did', 'dtime', 'type', 'money', 'money_bx', 'hname', 'sname', 'dstatus', 'folder', 'msg']
    model_icon = 'fa fa-tags'
    list_editable = ['money_bx', "dstatus"]
    # readonly_fields = ('rid', 'did', 'dtime', 'type', 'hname', 'sid', 'folder')
    search_fields = ['rid__rid', 'did', 'sname', 'hname']
    list_filter = ['type', 'dstatus']
    show_bookmarks = False

    form_layout = (
        Row('rid', 'did'),
        Row('dtime', 'type'),
        Row('hname', 'sname'),
        Row('money', 'money_bx', ''),
        Row('folder'),
        Row('msg'),
        Row('dstatus')
    )

    # @staticmethod
    # def has_add_permission(request=None):
    #     # Disable add
    #     return False

    # 删除屏蔽
    @staticmethod
    def has_delete_permission(request=None):
        # Disable add
        return False


class AuditAdmin(object):
    list_display = ['auid', 'aid_detail', 'austatus', 'mid', 'autime']
    model_icon = 'fa fa-columns'
    list_editable = ['austatus']
    # readonly_fields = ('auid', 'aid', 'mid', 'autime')
    show_bookmarks = False

    def aid_detail(self, obj):
        return '<a href="%s">%s</a>' % ('/xadmin/customer/apply/?_q_=' + str(obj.aid), obj.aid)

    aid_detail.allow_tags = True
    str = "<div class='dropdown pull-left'>" \
          "<a class='dropdown-toggle md-opjjpmhoiojifppkkcdabiobhakljdgm_doc' data-toggle='dropdown' href='#'>" \
          "申请编号</a>" \
          "<ul class='dropdown-menu' role='menu'>" \
          "<li><a href='?_q_=&amp;o=aid' class='active md-opjjpmhoiojifppkkcdabiobhakljdgm_doc'>" \
          "<i class='fa fa-caret-up'></i> 正序</a></li>" \
          "<li><a href='?_q_=&amp;o=-aid' class='active md-opjjpmhoiojifppkkcdabiobhakljdgm_doc'>" \
          "<i class='fa fa-caret-down'></i> 倒序</a></li>" \
          "</ul></div>"
    aid_detail.short_description = str
    search_fields = ['auid', "aid__aid"]
    list_filter = ['austatus', "autime"]

    # 删除屏蔽
    @staticmethod
    def has_delete_permission(request=None):
        # Disable add
        return False


class GlobalSetting(object):
    site_title = 'BXXT'
    site_header = 'BXXT'
    site_footer = 'BXXT'


xadmin.site.register(views.CommAdminView, GlobalSetting)
xadmin.site.register(User, UserAdmin)
xadmin.site.register(Manager, ManagerAdmin)
xadmin.site.register(Hospital, HospitalAdmin)
xadmin.site.register(UserType, UserTypeAdmin)
xadmin.site.register(Audit, AuditAdmin)
xadmin.site.register(Apply, ApplyAdmin)
xadmin.site.register(Record, RecordAdmin)
xadmin.site.register(Detail, DetailAdmin)

