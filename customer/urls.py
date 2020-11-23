from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/',views.login,name='login'),
    path('account/',views.account,name='account'),
    path('business/',views.business,name='business'),
    path('search/',views.search,name='search'),
]
