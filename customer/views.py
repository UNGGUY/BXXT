import hashlib
from decimal import Decimal

from django.shortcuts import render, redirect, get_list_or_404

from django.shortcuts import render, get_object_or_404
from customer.models import User, Detail, Apply, Record
from django.db.models import Q, Sum, Count
import datetime

# Create your views here.
from customer import models
from customer.myforms import UserForm, RegisterForm


def index(request):
    """
    docstring
    """
    return render(request, 'customer/index.html')


# 登录模块
def login(request):
    if request.session.get('is_login', None):
        print(2)
        return redirect('/bxxt/customer/')

    if request.method == "POST":
        login_form = UserForm(request.POST)
        message = "所有字段都必须填写！"

        # 废弃的用户名和密码获取方式，
        # username = request.POST.get('username', None)
        # password = request.POST.get('password', None)

        # 新方式：通过表单获取用户名和密码
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            try:
                user = models.User.objects.get(Q(uid=username) | Q(tel=username))
               # user = models.User.objects.get(Q(uid=username) | Q(tel=username) | Q(uname=username))
                if user.password == password:
                    request.session['is_login'] = True
                    request.session['user_id'] = user.uid
                    request.session['user_name'] = user.uname
                    # return redirect('/index/')
                    # return redirect('sulogin')

                    return redirect('/bxxt/customer/account')
                else:
                    message = "密码不正确！"
            except:
                message = "用户不存在"

        return render(request, 'customer/login.html', locals())
    login_form = UserForm()

    return render(request, 'customer/login.html', locals())


# 个人账户模块
def account(request):
    """
    docstring
    """
    # user=User(uid='arstdhneio',uname='UNGGOY',tel='18201529287',money=1000,age=24,address='beijing')
    user = models.User.objects.get(uid=request.session['user_id'])
    if user.sex == "1":
        user.sex = "男"
    else:
        user.sex = "女"
    context = {'User': user}

    if request.method == "POST":
        tel = request.POST.get('phonenubmer',None)
        province = request.POST.get('province',None)
        print(tel)
        print(province)

        user.tel = tel
        user.address = province
        user.save()


    return render(request, 'customer/account.html', context)


# 注册模块
def register(request):
    if request.session.get('is_login', None):
        # 登录状态不允许注册。你可以修改这条原则！
        return redirect("/bxxt/customer/")
    if request.method == "POST":
        register_form = RegisterForm(request.POST)
        message = "请检查填写的内容！"
        if register_form.is_valid():  # 获取数据
            username = register_form.cleaned_data['username']
            password1 = register_form.cleaned_data['password1']
            password2 = register_form.cleaned_data['password2']
            tel = register_form.cleaned_data['tel']
            sex = register_form.cleaned_data['sex']
            if password1 != password2:  # 判断两次密码是否相同
                message = "两次输入的密码不同！"
                return render(request, 'customer/register.html', locals())
            else:
                same_name_user = models.User.objects.filter(uname=username)
                if same_name_user:  # 用户名唯一
                    message = '用户已经存在，请重新选择用户名！'
                    return render(request, 'customer/register.html', locals())



                # 当一切都OK的情况下，创建新用户

                new_user = models.User.objects.create()
                new_user.uname = username
                new_user.password = password1  # 使用加密密码
                new_user.tel = tel
                new_user.sex= sex
                new_user.save()
                return redirect('/bxxt/customer/login/')  # 自动跳转到登录页面
    register_form = RegisterForm()
    return render(request, 'customer/register.html', locals())


# 登出模块
def logout(request):
    if not request.session.get('is_login', None):
        # 如果本来就没有登录，自然也就没有登出的说法
        return redirect("/bxxt/customer/")
    # 清空session
    request.session.flush()
    request.session['is_login'] = False

    return redirect('/bxxt/customer/')


def business(request):
    """
    docstring
    """
    uid = request.session["user_id"]
    user = models.User.objects.get(uid=uid)
    context = {'User': user}
    return render(request, 'customer/business.html', context)


def applys(request):
    """
    docstring
    """
    user = models.User.objects.get(uid=request.session['user_id'])
    latest_apply_list = models.Apply.objects.filter(Q(uid__uid=request.session['user_id']) & Q(isDelete=False) & ~Q(
        astatus='4'))
    context = {'User': user, 'latest_apply_list': latest_apply_list}
    return render(request, 'customer/applys.html', context)


def applys_delete(request, apply_id):
    models.Apply.objects.get(id=apply_id).delete()
    return redirect('/bxxt/customer/applys/')


def records(request, apply_id):
    """
    docstring
    """
    user = models.User.objects.get(uid=request.session['user_id'])
    latest_record_list = models.Record.objects.filter(aid__id=apply_id)
    context = {'User': user, 'latest_record_list': latest_record_list}

    return render(request, 'customer/records.html', context)


def records_delete(request, record_id):
    record = models.Record.objects.get(id=record_id)
    aid = record.aid.id
    record.delete()
    return redirect('/bxxt/customer/records/'+str(aid))


def details(request, record_id):
    """
    docstring
    """
    # 如果状态为待报销，则只输出合格的
    record = models.Apply.objects.get(record__id=record_id)
    if record.astatus == '3' or record.astatus == '4':
        latest_detail_list = models.Detail.objects.filter(Q(rid__id=record_id) & Q(dstatus='1'))
    else:
        latest_detail_list = models.Detail.objects.filter(rid__id=record_id)
    user = models.User.objects.get(uid=request.session['user_id'])
    context = {'latest_detail_list': latest_detail_list,
               'User': user
               }
    return render(request, 'customer/details.html', context)


def detail(request, detail_id):
    """
    docstring
    """
    user = models.User.objects.get(uid=request.session['user_id'])
    rs = models.Detail.objects.get(id=detail_id)
    return render(request, 'customer/detail.html', {'detail': rs, 'User': user})

    # 数据库直接用这个
    # detail = get_object_or_404(Detail, pk=detail_id)
    # return render(request, 'polls/detail.html', {'detail': detail})


def documents(request, apply_id):
    """
    docstring
    """
    user = models.User.objects.get(uid=request.session['user_id'])
    details = models.Detail.objects.filter(Q(rid__aid=apply_id) & Q(dstatus='1') & Q(type='1')).\
        aggregate(sum=Sum('money'))
    print(details['sum'])
    records = models.Record.objects.filter(aid=apply_id)
    latest_document_list = list()
    amount = 0
    for record in records:
        money_reg = models.Detail.objects.filter(Q(rid=record.id) & Q(dstatus='1') & Q(type='1')). \
            aggregate(sum=Sum('money'), bx=Sum('money_bx'))
        money_inv = models.Detail.objects.filter(Q(rid=record.id) & Q(dstatus='1') & Q(type='2')). \
            aggregate(sum=Sum('money'), bx=Sum('money_bx'))
        desum = models.Detail.objects.filter(Q(rid=record.id) & Q(dstatus='1')). count()
        ratio = user.utype.ratio
        if user.money >= user.utype.limit:
            ratio += user.utype.change
        if not money_reg['sum']:
            money_reg['sum'] = 0
        if not money_inv['sum']:
            money_inv['sum'] = 0
        if not money_reg['bx']:
            money_reg['bx'] = 0
        if not money_inv['bx']:
            money_inv['bx'] = 0
        document = {'aid': record.aid,
                    'rid': record.rid,
                    'dtime': models.Detail.objects.filter(rid=record.id)[0].dtime,
                    'register': money_reg['sum'],
                    'invoice': money_inv['sum'],
                    'cost': money_reg['sum']+money_inv['sum'],
                    'money': money_reg['bx']+money_inv['bx'],
                    'ratio': str(ratio)+"%",
                    'money_bx': Decimal((money_reg['bx']+money_inv['bx'])*ratio/100).quantize(Decimal('0.00')),
                    'desum': desum
                    }
        latest_document_list.append(document)
        amount +=Decimal((money_reg['bx']+money_inv['bx'])*ratio/100).quantize(Decimal('0.00'))

    context = {'latest_document_list': latest_document_list,
               'User': user,
               'amount': amount,
               }

    return render(request, 'customer/documents.html', context)


def undo(request, apply_id):
    apply = models.Apply.objects.get(id=apply_id)
    if apply.astatus == '1':
        apply.astatus = '0'
        apply.save()
    return redirect('/bxxt/customer/applys/')


def submit(request, apply_id):
    apply = models.Apply.objects.get(id=apply_id)
    apply.astatus = '1'
    records = models.Record.objects.filter(aid=apply_id)
    for record in records:
        details = models.Detail.objects.filter(rid=record.id)
        count = 0
        for detail in details:
            detail.dstatus = '0'
            count += detail.money
            detail.save()
        record.money = count
        record.money_bx = count
        record.save()
    apply.save()
    return redirect('/bxxt/customer/applys/')


def confirm(request, apply_id):
    apply = models.Apply.objects.get(id=apply_id)
    apply.astatus = '3'
    details = models.Detail.objects.filter(Q(rid__aid=apply_id) & Q(dstatus='-1'))
    for detail in details:
        detail.delete()
    apply.save()
    return redirect('/bxxt/customer/applys/')


