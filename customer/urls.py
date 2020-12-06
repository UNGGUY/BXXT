from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/',views.login,name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout, name='logout'),
    path('account/', views.account, name='account'),

    path('business/',views.business,name='business'),
    path('applys/',views.applys,name='applys'),
    path('records/<int:apply_id>/',views.records,name='records'),
    path('details/<int:record_id>/',views.details,name='details'),
    path('detail/<int:detail_id>/',views.detail,name='detail'),
    
    path('documents/<int:apply_id>/',views.documents,name='documents'),
    
]
