
import hashlib

from django.shortcuts import render, redirect

from django.shortcuts import render,get_object_or_404
from customer.models import User,Detail,Apply,Record
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
                user = models.User.objects.get(uname=username)
                if user.password == password:
                    request.session['is_login'] = True
                    request.session['user_id'] = user.uid
                    request.session['user_name'] = user.uname
                    # return redirect('/index/')
                    #return redirect('sulogin')
                    print(1)
                    return redirect('/bxxt/customer/account')
                else:
                    message = "密码不正确！"
            except:
                message = "用户不存在"
        print(3)
        return render(request, 'customer/login.html', locals())
    login_form = UserForm()
    print(4)
    return render(request, 'customer/login.html', locals())

#个人账户模块
def account(request):
    """
    docstring
    """

    return render(request, 'customer/account.html')




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
            email = register_form.cleaned_data['email']
            sex = register_form.cleaned_data['sex']
            if password1 != password2:  # 判断两次密码是否相同
                message = "两次输入的密码不同！"
                return render(request, 'customer/register.html', locals())
            else:
                same_name_user = models.User.objects.filter(name=username)
                if same_name_user:  # 用户名唯一
                    message = '用户已经存在，请重新选择用户名！'
                    return render(request, 'customer/register.html', locals())
                same_email_user = models.User.objects.filter(email=email)
                if same_email_user:  # 邮箱地址唯一
                    message = '该邮箱地址已被注册，请使用别的邮箱！'
                    return render(request, 'customer/register.html', locals())

                # 当一切都OK的情况下，创建新用户

                new_user = models.User.objects.create()
                new_user.name = username
                new_user.password = password1  # 使用加密密码
                new_user.email = email
                new_user.sex = sex
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

    user=User(uid='arstdhneio',uname='UNGGOY',tel='18201529287',money=1000,age=24,address='beijing')
    context={'User':user}
    return render(request,'customer/account.html',context)


def business(request):
    """
    docstring
    """
    user=User(uid='arstdhneio',uname='UNGGOY',tel='18201529287',money=1000,age=24,address='beijing')
    context={'User':user}
    return render(request,'customer/business.html',context)


def applys(request):
    """
    docstring
    """
    user=User(uid='arstdhneio',uname='UNGGOY',tel='18201529287',money=1000,age=24,address='beijing')
    latest_apply_list=[
        Apply(id=1,aid='xxxx',astatus=0),
        Apply(id=2,aid='xxxx',astatus=1),
        Apply(id=3,aid='xxxx',astatus=2),
        Apply(id=4,aid='xxxx',astatus=3),
        Apply(id=5,aid='xxxx',astatus=4),
    ]
    context={'User':user,'latest_apply_list':latest_apply_list}
    return render(request,'customer/applys.html',context)

def records(request,apply_id):
    """
    docstring
    """
    user=User(uid='arstdhneio',uname='UNGGOY',tel='18201529287',money=1000,age=24,address='beijing')
    latest_record_list=[
        Record(id=1,rid='xxxx',rtime=datetime.datetime.now(),msg='hello',money=100),
        Record(id=2,rid='xxxx',rtime=datetime.datetime.now(),msg='world',money=100),
        Record(id=3,rid='xxxx',rtime=datetime.datetime.now(),msg='Django',money=100),
        Record(id=4,rid='xxxx',rtime=datetime.datetime.now(),msg='what',money=100),
        Record(id=5,rid='xxxx',rtime=datetime.datetime.now(),msg='fuck',money=100),
    ]
    context={'User':user,'latest_record_list':latest_record_list}

    return render(request,'customer/records.html',context)


def details(request,record_id):
    """
    docstring
    """

    user=User(uid='arstdhneio',uname='UNGGOY',tel='18201529287',money=1000,age=24,address='beijing')
    latest_detail_list=[
        Detail(id=1,did='xxxx',hname='evilhospital',dstatus=0,dtime=datetime.datetime.now(),money=1000,type=0),
        Detail(id=2,did='xxxx',hname='evilhospital',dstatus=1,dtime=datetime.datetime.now(),money=1000,type=0),
        Detail(id=3,did='xxxx',hname='evilhospital',dstatus=1,dtime=datetime.datetime.now(),money=1000,type=0),
        Detail(id=4,did='xxxx',hname='evilhospital',dstatus=0,dtime=datetime.datetime.now(),money=1000,type=0),
    ]
    
    context={'latest_detail_list':latest_detail_list,
        'User':user
    }
    return render(request,'customer/details.html',context)


def detail(request,detail_id):
    """
    docstring
    """
    user=User(uid='arstdhneio',uname='UNGGOY',tel='18201529287',money=1000,age=24,address='beijing')
    Detail(id=1,did='xxxx',hname='evilhospital',dstatus=0,dtime=datetime.datetime.now(),money=1000,type=0)

    return render(request,'customer/detail.html',{'detail':detail,'User':user})

    # 数据库直接用这个
    # detail = get_object_or_404(Detail, pk=detail_id)
    # return render(request, 'polls/detail.html', {'detail': detail})

