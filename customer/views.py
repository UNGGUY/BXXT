import hashlib

from django.shortcuts import render, redirect

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
