from django.shortcuts import render

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
    return render(request,'customer/account.html')