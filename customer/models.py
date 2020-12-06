from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import Group, User as adminUser
# import MySQLdb


# Create your models here.

class Manager(models.Model):
    """超级用户表/管理员表"""
    class Type(models.TextChoices):
        admin = '0', _('管理员')
        manager = '1', _('审核负责人')
        auditer = '2', _('审核人')
        checker = '3', _('收单员')

    mid = models.CharField('账户', max_length=20)  # 账户Mid
    pw = models.CharField('密码', max_length=16)  # 账户密码pw
    mname = models.CharField('姓名', max_length=20)  # 用户姓名mname
    type = models.CharField('身份', choices=Type.choices, max_length=20)
    right = models.IntegerField('有效数量', default=0)
    count = models.IntegerField('处理数量', default=0)
    isDelete = models.BooleanField('是否删除', default=False, null=True)  # 删除标识 默认default  或 true null

    def __str__(self):
        return self.mid

    def save(self):
        models.Model.save(self, force_insert=False, force_update=False, using=None, update_fields=None)
        print(self.type)
        if self.type == '0':  # 管理员
            admin = Group.objects.filter(name='admin').first()  # 二级管理组 是管理员在xadmin后台添加的权限组
        else:
            if self.type == '1':  # 负责人
                admin = Group.objects.filter(name='manager').first()  # 二级管理组 是管理员在xadmin后台添加的权限组
        user = adminUser(username=self.mid)
        user.set_password(self.pw)
        user.is_superuser = False
        user.is_active = True
        user.first_name = self.mname
        user.is_staff = True
        print(user)
        user.save()  # 先生成用户
        user.groups.add(admin)

    class Meta:
        db_table = "manager"
        verbose_name = '员工'
        verbose_name_plural = verbose_name


class UserType(models.Model):
    utype = models.CharField('人员类型', max_length=20)
    limit = models.DecimalField('金额标准', max_digits=8, decimal_places=2)
    ratio = models.IntegerField('报销比例/%', default=70)
    change = models.IntegerField('变化幅度/%', default=10)

    def __str__(self):
        return self.utype

    class Meta:
        db_table = "usertype"
        verbose_name = '人员类型'
        verbose_name_plural = verbose_name


class User(models.Model):
    gender = (
        ('1', '男'),
        ('0', '女'),
    )
    ######################
    # 注意，这里的用户名是网络上的用户名
    # 姓名
    uname = models.CharField('姓名', max_length=20)
    # 身份证/账户
    uid = models.CharField('身份证/账号', max_length=18, unique=True)
    # 密码
    password = models.CharField('密码', max_length=16)
    # 手机号
    tel = models.CharField('手机号', max_length=11)
    # 身份
    utype = models.ForeignKey(UserType, on_delete=models.PROTECT, verbose_name=u"人员类型")
    # 性别
    sex = models.CharField('性别', max_length=20, choices=gender)
    # 报销金额
    money = models.DecimalField('报销金额', max_digits=8, decimal_places=2)
    # 年龄
    age = models.PositiveIntegerField('年龄', default=1)
    # 省份
    address = models.CharField('省份', max_length=20, default="北京")

    isDelete = models.BooleanField('删除状态', default=False, null=True)

    def __str__(self):
        return self.uname

    def delete(self):
        self.isDelete = True
        self.save()

    class Meta:
        verbose_name = '用户'
        verbose_name_plural = verbose_name
        db_table = "user"


class Hospital(models.Model):
    #  医院编
    hid = models.CharField('医院编号', max_length=20)
    #  医院名称
    hname = models.CharField('医院名称', max_length=100)
    #  删除标记，true 删除 false 未删除 null
    isDelete = models.BooleanField('是否删除', null=True, default=False)

    def __str__(self):
        return self.hname

    class Meta:
        db_table = "hospital"
        verbose_name = '医院'
        verbose_name_plural = verbose_name


class Apply(models.Model):
    choice = (
        ('0', '未提交'),
        ('1', '申请中'),
        ('2', '待确认'),
        ('3', '待报销'),
        ('4', '已报销'),
    )
    # 编号
    aid = models.CharField('申请编号', max_length=18)
    # 发起人id
    uid = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name=u"发起人")
    # 申请的状态
    astatus = models.CharField("申请状态", choices=choice, default='未提交', max_length=20)
    isDelete = models.BooleanField('是否删除', default=False, null=True)  # 删除标识 默认default  或 true null
    atime = models.DateTimeField('申请时间', auto_now_add=True)

    def __str__(self):
        return self.aid

    class Meta:
        db_table = "apply"
        verbose_name = '申请记录'
        verbose_name_plural = verbose_name


class Record(models.Model):
    """报销记录表"""
    aid = models.ForeignKey(Apply, on_delete=models.CASCADE, verbose_name=u"申请编号")  # 申请编号aid
    rid = models.CharField('记录编号', max_length=10)  # 编号rid
    rtime = models.DateField('修改时间', auto_now=True, auto_now_add=False)  # 最后修改时间rtime
    money = models.DecimalField('金额', max_digits=8, decimal_places=2, default=0.00)  # 金额money 6位.2位
    money_bx = models.DecimalField('可报销金额', max_digits=8, decimal_places=2, default=0.00)  # 可报销金额money 6位.2位
    msg = models.CharField('备注', max_length=200, null=True,blank=True)  # 备注信息msg

    def __str__(self):
        return self.rid

    class Meta:
        db_table = "record"
        verbose_name = '报销记录'
        verbose_name_plural = verbose_name


class Detail(models.Model):
    """凭证表"""

    rid = models.ForeignKey(Record,on_delete=models.CASCADE, verbose_name=u"报销编号")  # 报销编号rid
    did = models.CharField('凭证编号', max_length=10)  # 编号did
    dtime = models.DateField('时间', auto_now=False, auto_now_add=False)  # 时间
    choice=(
        ('0', '转诊单'),
        ('1', '挂号费'),
        ('2', '发票'),
        ('3', '补充'),
    )
    type = models.CharField('类型', choices=choice, max_length=20)
    money = models.DecimalField('金额', max_digits=8, decimal_places=2, null=True, blank=True)  # 金额money 6位.2位
    # 可报销金额money 6位.2位
    money_bx = models.DecimalField('可报销金额', max_digits=8, decimal_places=2, default=0.00, null=True, blank=True)
    hname = models.CharField('医院', max_length=20, null=True, blank=True)  # 医院hname
    sname = models.CharField('科室', max_length=20, null=True, blank=True)  # 科室sname
    status = (
        ('0', '验证'),
        ('1', '合格'),
        ('-1', '不合格')
    )
    dstatus = models.CharField('状态', choices=status, default='验证', max_length=20)  # 表单状态 默认false是合格
    msg = models.CharField('备注', max_length=200, null=True, blank=True)  # 备注信息msg

    def __str__(self):
        return self.did

    folder = models.ImageField('图片', upload_to='images')

    class Meta:
        db_table = "detail"
        verbose_name = '凭证'
        verbose_name_plural = verbose_name


class Audit(models.Model):
    choice = (
        ('1', '完成'),
        ('0', '撤销'),
    )
    aid = models.ForeignKey(Apply, on_delete=models.CASCADE, verbose_name=u"申请编号")
    auid = models.CharField('审核编号', max_length=10)
    austatus = models.CharField('状态', choices=choice, default='完成', max_length=20)
    mid = models.ForeignKey(Manager, on_delete=models.PROTECT, verbose_name=u"审核人")
    autime = models.DateTimeField('审核时间', auto_now_add=True)

    def __str__(self):
        return self.auid

    class Meta:
        db_table = "audit"
        verbose_name = '审核记录'
        verbose_name_plural = verbose_name






