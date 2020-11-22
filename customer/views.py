from django.shortcuts import render
from customer.models import User

# Create your views here.
def index(request):
    """
    docstring
    """
    return render(request,'customer/index.html')

def login(request):
    """
    docstring
    """
    return render(request,'customer/login.html')

def account(request):
    """
    docstring
    """
    user=User()
    user.uname="UNGGOY"
    user.uid="arstdhneio"
    user.tel="18201529287"
    user.money=1000
    user.age=24
    user.address="beijing"
    context={'User':user}
    return render(request,'customer/account.html',context)


def business(request):
    """
    docstring
    """
    user=User()
    user.uname="UNGGOY"
    user.uid="arstdhneio"
    user.tel="18201529287"
    user.money=1000
    user.age=24
    user.address="beijing"
    context={'User':user}
    return render(request,"customer/business.html",context)