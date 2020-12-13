
from django import forms

#用户表单
class UserForm(forms.Form):
    username= forms.CharField(label = "USERNAME", max_length=128, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label="PASSWORD", max_length=256, widget=forms.PasswordInput(attrs={'class': 'form-control'}))


#注册表单
class RegisterForm(forms.Form):
    gender = (
        ('male', "男"),
        ('female', "女"),
    )
    username = forms.CharField(label="USERNAME", max_length=128, widget=forms.TextInput(attrs={'class': 'form-control'}))

    password1 = forms.CharField(label="PASSWORD", max_length=256, widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    password2 = forms.CharField(label="CONFIRM", max_length=256, widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    tel = forms.CharField(label="TELPHONE", max_length= 11, widget=forms.TextInput(attrs={'class': 'form-control'}))

    sex = forms.ChoiceField(label='GENDER', choices=gender)

#员工表单
class StaffForm(forms.Form):
    mname= forms.CharField(label = "MANAGER NAME", max_length=128, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label="PASSWORD", max_length=256, widget=forms.PasswordInput(attrs={'class': 'form-control'}))


#
# #申请表单
# class ApplyForm(forms.Form):
#     username = forms.CharField(label="USERNAME", max_length=128, widget=forms.TextInput(attrs={'class': 'form-control'}))
#     astatus = forms.CharField(label="APPLY STATE", max_length=256, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
#
# #报销记录表单
# class RecordForm(forms.Form):
#     username = forms.CharField(label="USERNAME", max_length=128, widget=forms.TextInput(attrs={'class': 'form-control'}))
#     astatus = forms.CharField(label="APPLY STATE", max_length=256, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
#
#     rtime = forms.DateField(label="LAST TIME", auto_now=True, auto_now_add=False,widget=forms.TimeInput(attrs={'class': 'form-control'}))
#     money = forms.DecimalField(max_digits=8, decimal_places=2)
#     msg = forms.CharField(label="MESSAGE", max_length=128, widget=forms.TextInput(attrs={'class': 'form-control'}))
#
#
# #科室表单
#
# class SectionForm(forms.Form):
#     style = forms.CharField(label="SETION TYPE", max_length=128, widget=forms.TextInput(attrs={'class': 'form-control'}))
#     sid = forms.CharField(label="SETION NUMBER", max_length=256, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
#
#
# #凭证表表单
# class DetailForm(forms.Form):
#     dtime = forms.CharField(label="SETION TYPE", max_length=128, widget=forms.TextInput(attrs={'class': 'form-control'}))
#     did = forms.CharField(label="SETION NUMBER", max_length=256, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
#



#
# class Detail(models.Model):
#     """凭证表"""
#
#     rid = models.ForeignKey(Record,on_delete=models.CASCADE)  # 报销编号rid
#     did = models.CharField(max_length=10)  # 编号did
#     dtime = models.DateField(auto_now=False, auto_now_add=False)  # 时间
#     choice=(
#         ('change', '转诊单'),
#         ('register', '挂号费'),
#         ('cost', '发票'),
#         ('extra', '补充'),
#     )
#     type = models.CharField('类型', max_length=20,choices=choice)
#     money = models.DecimalField(max_digits=8, decimal_places=2, null=True)  # 金额money 6位.2位
#     hname = models.CharField(max_length=20, null=True)  # 医院hname
#     sid = models.ForeignKey(Section, on_delete=models.PROTECT, null=True)  # 科室sid
#     status = (
#         ('verify', '验证'),
#         ('success', '合格'),
#         ('fail', '不合格')
#     )
#     dstatus = models.CharField('状态', max_length=20, choices=status, default='验证')  # 表单状态 默认false是合格
#     folder = models.ImageField()
#
#     def __str__(self):
#         return self.did
#
#     class Meta:
#         db_table = "detail"
#         verbose_name = '凭证表'
#         verbose_name_plural = '凭证表'
#
#
# class Hospital(models.Model):
#     #  医院编
#     hid = models.CharField(max_length=20)
#     #  医院名称
#     hname = models.CharField(max_length=100)
#     #  删除标记，true 删除 false 未删除 null
#     isDelete = models.BooleanField()
#
#     def __str__(self):
#         return self.hname
#
#     class Meta:
#         db_table = "hospital"
#         verbose_name = '医院'
#         verbose_name_plural = '医院'
#
#
# class Ratio(models.Model):
#     utype = models.ForeignKey(UserType, on_delete=models.PROTECT)
#     sid = models.ForeignKey(Section, on_delete=models.PROTECT)
#     percent = models.IntegerField(default=10)
#
#     class Meta:
#         db_table = "ratio"
#         verbose_name = '报销比例'
#         verbose_name_plural = '报销比例'
#
#
# class Audit(models.Model):
#     choice = (
#         ('finish', '完成'),
#         ('undo', '撤销'),
#     )
#     aid = models.ForeignKey(Apply, on_delete=models.CASCADE)
#     auid = models.CharField(max_length=10)
#     austatus = models.CharField('状态', max_length=10, choices=choice, default='完成')
#     mid = models.ForeignKey(Manager, on_delete=models.PROTECT)
#     autime = models.DateTimeField(auto_now_add=True)
#
#     def __str__(self):
#         return self.auid
#
#     class Meta:
#         db_table = "audit"
#         verbose_name = '审核人员'
#         verbose_name_plural = '审核人员'
#
#







