from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout, name='logout'),
    path('account/', views.account, name='account'),
    path('account/update/', views.account_update, name='account_update'),

    path('business/', views.business, name='business'),

    path('applys/', views.applys, name='applys'),
    path('applys/delete/<int:apply_id>/', views.applys_delete, name='applys_delete'),
    path('applys/undo/<int:apply_id>/', views.undo, name='undo'),
    path('applys/submit/<int:apply_id>/', views.submit, name='submit'),
    path('applys/confirm/<int:apply_id>/', views.confirm, name='confirm'),

    path('records/<int:apply_id>/', views.records, name='records'),
    path('records/delete/<int:record_id>/', views.records_delete, name='records_delete'),

    path('details/<int:record_id>/', views.details, name='details'),

    path('detail/<int:detail_id>/', views.detail, name='detail'),

    path('documents/<int:apply_id>/', views.documents, name='documents'),

    path('edit/<int:detail_id>/',views.edit,name='edit'),

    path('addrecord/<int:apply_id>',views.addrecord,name='addrecord')

]
