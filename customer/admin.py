from django.contrib import admin

# Register your models here.
from django.contrib import admin
import xadmin
from django.http import HttpResponse
from django.template.response import TemplateResponse
from xadmin.util import model_ngettext

from customer.models import Manager, Apply, Audit, Hospital, UserType, User, Record, Detail
from xadmin import views
from xadmin.plugins.actions import BaseActionView
from django.utils.translation import gettext_lazy as _


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
    # 批量导入
    # 删除重写
    actions = [MyDelete]

    # 删除屏蔽
    @staticmethod
    def has_delete_permission(request=None):
        # Disable add
        return False


class ManagerAdmin(object):
    list_display = ['mid', 'mname', 'type', 'count', 'workrate', 'isDelete']
    ordering = ['isDelete']
    search_fields = ['mid', 'mname']
    list_filter = ['type', 'isDelete']
    model_icon = 'fa fa-user'
    show_bookmarks = False

    def workrate(self, instance):
        if instance.count == 0:
            return '-'
        else:
            return instance.right / instance.count

    workrate.short_description = '正确率'
    workrate.is_column = True
    workrate.allow_tags = True
    list_editable = ['mname']
    # readonly_fields =  "isDelete"
    # 批量导入
    # 删除重写
    actions = [MyDelete]

    # 删除屏蔽
    @staticmethod
    def has_delete_permission(request=None):
        # Disable add
        return False


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
    list_display = ['aid', 'rid', 'rtime', 'money', 'msg']
    model_icon = 'fa fa-tag'
    list_editable = ['money']
    # readonly_fields = ("isDelete", "aid", "rid", "rtime", "msg")
    search_fields = ['aid__aid', 'rid']
    show_bookmarks = False

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
    list_display = ['rid', 'did', 'dtime', 'type', 'money', 'hname', 'sname', 'dstatus', 'folder']
    model_icon = 'fa fa-tags'
    list_editable = ['money', "dstatus"]
    # readonly_fields = ('rid', 'did', 'dtime', 'type', 'hname', 'sid', 'folder')
    search_fields = ['rid__rid', 'did', 'sname', 'hname']
    list_filter = ['type', 'dstatus']
    show_bookmarks = False

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
        return '<a href="%s">%s</a>' % ('http://127.0.0.1:8000/xadmin/customer/apply/?_q_=' + str(obj.aid), obj.aid)

    aid_detail.allow_tags = True
    aid_detail.short_description = '申请记录'
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
# xadmin.site.register(Section, SectionAdmin)
xadmin.site.register(UserType, UserTypeAdmin)
# xadmin.site.register(Ratio, RatioAdmin)
xadmin.site.register(Apply, ApplyAdmin)
xadmin.site.register(Record, RecordAdmin)
xadmin.site.register(Detail, DetailAdmin)
xadmin.site.register(Audit, AuditAdmin)
