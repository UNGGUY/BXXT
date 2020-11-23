from django.db import models


# Create your models here.

class Manager(models.Model):
    """超级用户表/管理员表"""
    choice = (
        ('auditer', '审核人'),
        ('manager', '审核管理人'),
        ('admin', '后台管理员'),
        ('checker', '收单员'),
    )
    mid = models.CharField(max_length=20)  # 账户Mid
    pw = models.CharField(max_length=16)  # 账户密码pw
    mname = models.CharField(max_length=20)  # 用户姓名mname
    type = models.CharField('身份', max_length=20, choices=choice)  # 身份type
    isDelete = models.BooleanField(default=False)  # 删除标识 默认default  或 true null

    def __str__(self):
        return self.mid

    class Meta:
        db_table = "manager"
        verbose_name = '审核管理员'
        verbose_name_plural = '审核管理员'


class UserType(models.Model):
    utype = models.CharField(max_length=20)
    limit = models.DecimalField(max_digits=8, decimal_places=2)
    change = models.IntegerField(default=10)

    def __str__(self):
        return self.utype

    class Meta:
        db_table = "usertype"
        verbose_name = '用户类型'
        verbose_name_plural = '用户类型'


class User(models.Model):
    gender = (
        ('male', '男'),
        ('female', '女'),
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
    utype = models.ForeignKey(UserType, on_delete=models.PROTECT)
    # 性别
    sex = models.CharField('性别', max_length=10, choices=gender, default='男')
    # 报销金额
    money = models.DecimalField('报销金额', max_digits=8, decimal_places=2)
    # 年龄
    age = models.PositiveIntegerField('年龄', default=1)
    # 省份
    address = models.CharField('省份', max_length=20, default="北京")

    isDelete = models.BooleanField('三元态', default=False)

    def __str__(self):
        return self.uname

    class Meta:
        verbose_name = '用户'
        verbose_name_plural = '用户'
        db_table = "user"


# 申请记录表
class Apply(models.Model):
    choice = (
        ('uncommitted', '未提交'),
        ('applying', '申请中'),
        ('verify', '待确认'),
        ('waiting', '待报销'),
        ('perfect', '已报销'),
    )
    # 编号
    aid = models.CharField('编号', max_length=18)
    # 发起人id
    uid = models.ForeignKey(User, on_delete=models.PROTECT)
    # 申请的状态
    astatus = models.CharField("申请状态", max_length=20, choices=choice, default='未提交')
    isDelete = models.BooleanField(default=False)  # 删除标识 默认default  或 true null

    def __str__(self):
        return self.aid

    class Meta:
        db_table = "apply"
        verbose_name = '申请记录'
        verbose_name_plural = '申请记录'


class Record(models.Model):
    """报销记录表"""
    aid = models.ForeignKey(Apply, on_delete=models.CASCADE)  # 申请编号aid
    rid = models.CharField(max_length=10)  # 编号rid
    rtime = models.DateField(auto_now=True, auto_now_add=False)  # 最后修改时间rtime
    money = models.DecimalField(max_digits=8, decimal_places=2)  # 金额money 6位.2位
    msg = models.CharField(max_length=200)  # 备注信息msg

    def __str__(self):
        return self.rid

    class Meta:
        db_table = "record"
        verbose_name = '报销记录'
        verbose_name_plural = '报销记录'


class Section(models.Model):
    stype = models.CharField(max_length=20)  # 科室类型
    sid = models.CharField(max_length=20)  # 科室编号
    # 删除标记，true 删除 false 未删除 null
    isDelete = models.BooleanField()

    def __str__(self):
        return self.stype

    class Meta:
        db_table = "section"
        verbose_name = '科室'
        verbose_name_plural = '科室'


class Detail(models.Model):
    """凭证表"""

    rid = models.ForeignKey(Record,on_delete=models.CASCADE)  # 报销编号rid
    did = models.CharField(max_length=10)  # 编号did
    dtime = models.DateField(auto_now=False, auto_now_add=False)  # 时间
    choice=(
        ('change', '转诊单'),
        ('register', '挂号费'),
        ('cost', '发票'),
        ('extra', '补充'),
    )
    type = models.CharField('类型', max_length=20,choices=choice)
    money = models.DecimalField(max_digits=8, decimal_places=2, null=True)  # 金额money 6位.2位
    hname = models.CharField(max_length=20, null=True)  # 医院hname
    sid = models.ForeignKey(Section, on_delete=models.PROTECT, null=True)  # 科室sid
    status = (
        ('verify', '验证'),
        ('success', '合格'),
        ('fail', '不合格')
    )
    dstatus = models.CharField('状态', max_length=20, choices=status, default='验证')  # 表单状态 默认false是合格
    folder = models.ImageField()

    def __str__(self):
        return self.did

    class Meta:
        db_table = "detail"
        verbose_name = '凭证表'
        verbose_name_plural = '凭证表'


class Hospital(models.Model):
    #  医院编
    hid = models.CharField(max_length=20)
    #  医院名称
    hname = models.CharField(max_length=100)
    #  删除标记，true 删除 false 未删除 null
    isDelete = models.BooleanField()

    def __str__(self):
        return self.hname

    class Meta:
        db_table = "hospital"
        verbose_name = '医院'
        verbose_name_plural = '医院'


class Ratio(models.Model):
    utype = models.ForeignKey(UserType, on_delete=models.PROTECT)
    sid = models.ForeignKey(Section, on_delete=models.PROTECT)
    percent = models.IntegerField(default=10)

    class Meta:
        db_table = "ratio"
        verbose_name = '报销比例'
        verbose_name_plural = '报销比例'


class Audit(models.Model):
    choice = (
        ('finish', '完成'),
        ('undo', '撤销'),
    )
    aid = models.ForeignKey(Apply, on_delete=models.CASCADE)
    auid = models.CharField(max_length=10)
    austatus = models.CharField('状态', max_length=10, choices=choice, default='完成')
    mid = models.ForeignKey(Manager, on_delete=models.PROTECT)
    autime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.auid

    class Meta:
        db_table = "audit"
        verbose_name = '审核人员'
        verbose_name_plural = '审核人员'






