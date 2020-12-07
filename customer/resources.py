from import_export import resources
from customer.models import *


class HospitalResource(resources.ModelResource):

    class Meta:
        model = Hospital
        fields = ('id', 'hid', 'hname')


class UserResource(resources.ModelResource):

    class Meta:
        model = User
        fields = ('id', 'uid', 'uname', 'password', 'tel', 'utype', 'sex', 'money', 'age', 'address', 'isDelete')


class ManagerResource(resources.ModelResource):

    class Meta:
        model = Manager
        fields = ('id', 'mid', 'mname', 'pw', 'type', 'right', 'count', 'isDelete')


class UserTypeResource(resources.ModelResource):

    class Meta:
        model = UserType
        fields = ('id', 'utype', 'limit', 'ratio', 'change')


class ApplyResource(resources.ModelResource):

    class Meta:
        model = Apply
        fields = ('id', 'aid', 'uid', 'astatus', 'atime', 'isDelete')


class RecordResource(resources.ModelResource):

    class Meta:
        model = Record
        fields = ('id', 'aid', 'rid', 'rtime', 'money', 'money_bx', 'msg')


class DetailResource(resources.ModelResource):

    class Meta:
        model = Detail
        fields = ('id', 'rid', 'did', 'dtime', 'type', 'money', 'money_bx', 'hname', 'sname', 'dsatus', 'msg')


class AuditResource(resources.ModelResource):
    class Meta:
        model = Audit
        fields = ('id', 'aid', 'auid', 'austatus', 'mid', 'autime')