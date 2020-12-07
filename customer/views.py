import hashlib

from django.shortcuts import render, redirect, get_list_or_404

from django.shortcuts import render, get_object_or_404
from customer.models import User, Detail, Apply, Record
from django.db.models import Q
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
                user = models.User.objects.get(Q(uid=username) | Q(tel=username) | Q(uname=username) )
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
    user = models.User.objects.filter(uid=request.session['user_id'])
    latest_apply_list = models.Apply.objects.filter(Q(uid__uid=request.session['user_id']) & Q(isDelete=False) & ~Q(
        astatus='4'))
    context = {'User': user, 'latest_apply_list': latest_apply_list}
    return render(request, 'customer/applys.html', context)


def records(request, apply_id):
    """
    docstring
    """
    uid = request.session["user_id"]
    user = models.User.objects.get(uid=uid)

    latest_record_list = get_list_or_404(Record, aid=apply_id)

    # user = models.User.objects.filter(uid=request.session['user_id'])
    # latest_apply_list = models.Apply.objects.filter(Q(uid__uid=request.session['user_id']) & Q(isDelete=False) & ~Q(
    #     astatus='4'))
    context = {'User': user, 'latest_record_list': latest_record_list}
    return render(request, 'customer/records.html', context)

def details(request,record_id):
    uid = request.session["user_id"]
    user = models.User.objects.get(uid=uid)

    latest_detail_list=get_list_or_404(Detail, rid=record_id)

    context={'latest_detail_list':latest_detail_list,'User':user}
    return render(request,'customer/details.html',context)






# def details(request, record_id):
#     """
#     docstring
#     """
#
#     user = User(uid='arstdhneio', uname='UNGGOY', tel='18201529287', money=1000, age=24, address='beijing')
#     latest_detail_list = [
#         Detail(id=1, did='xxxx', hname='evilhospital', dstatus="合格", dtime=datetime.datetime.now(), money="-",
#                type="转诊单"),
#         Detail(id=2, did='xxxx', hname='evilhospital', dstatus="合格", dtime=datetime.datetime.now(), money=1000,
#                type="挂号单"),
#         Detail(id=3, did='xxxx', hname='evilhospital', dstatus="合格", dtime=datetime.datetime.now(), money=1000,
#                type="发票"),
#         Detail(id=4, did='xxxx', hname='evilhospital', dstatus="合格", dtime=datetime.datetime.now(), money="-",
#                type="明细"),
#     ]
#     latest_detail_list = models.Detail.objects.filter(rid="0000000001")
#     print(type(latest_detail_list))
#     context = {'latest_detail_list': latest_detail_list,
#                'User': user
#                }
#     return render(request, 'customer/details.html', context)


def detail(request,detail_id):
    """
    docstring
    """
    uid = request.session["user_id"]
    user = models.User.objects.get(uid=uid)



    detail = get_object_or_404(Detail, pk=detail_id)
    return render(request,'customer/detail.html',{'detail':detail,'User':user})



# def detail(request, detail_id):
#     """
#     docstring
#     """
#     user = User(uid='arstdhneio', uname='UNGGOY', tel='18201529287', money=1000, age=24, address='beijing')
#     detail = Detail(id=1, did='xxxx', hname='hospital', dstatus="合格", dtime=datetime.datetime.now(), money=1000,
#                     type="转诊单")
#
#     return render(request, 'customer/detail.html', {'detail': detail, 'User': user})

    # 数据库直接用这个
    # detail = get_object_or_404(Detail, pk=detail_id)
    # return render(request, 'polls/detail.html', {'detail': detail})



def confirm(request, apply_id):
    """
    docstring
    """
    uid = request.session["user_id"]
    user = models.User.objects.get(uid=uid)
    latest_record_list = get_list_or_404(Record, aid=apply_id)


    return render(request, 'customer/confirm.html')


def documents(request, apply_id):
    """
    docstring
    """
    return render(request, 'customer/documents.html')
