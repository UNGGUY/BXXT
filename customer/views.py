from django.shortcuts import render
from customer.models import User,Detail
import datetime

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



def search(request):
    """
    docstring
    """

    user=User(uid='arstdhneio',uname='UNGGOY',tel='18201529287',money=1000,age=24,address='beijing')
    latest_detail_list=[
        Detail(id=1,did='xxxx',hname='evilhospital',dstatus=0,dtime=datetime.datetime.now(),money=1000,type=0),
        Detail(id=2,did='xxxx',hname='evilhospital',dstatus=0,dtime=datetime.datetime.now(),money=1000,type=0),
        Detail(id=3,did='xxxx',hname='evilhospital',dstatus=0,dtime=datetime.datetime.now(),money=1000,type=0),
        Detail(id=4,did='xxxx',hname='evilhospital',dstatus=0,dtime=datetime.datetime.now(),money=1000,type=0),
    ]

    context={'latest_detail_list':latest_detail_list,
        'User':user
    }
    return render(request,'customer/search.html',context)

    