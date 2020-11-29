from django.shortcuts import render,get_object_or_404
from customer.models import User,Detail,Apply,Record
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