from django.urls import path

from . import views
from decimal import Decimal

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
    path('applys/new/', views.applys_new, name='applys_new'),

    path('records/<int:apply_id>/', views.records, name='records'),
    path('records/delete/<int:record_id>/', views.records_delete, name='records_delete'),
    path('addrecord/<int:apply_id>',views.addrecord, name='addrecord'),
    path('records/add/<int:apply_id>/', views.records_insert, name='records_insert'),

    path('details/<int:record_id>/', views.details, name='details'),

    path('detail/<int:detail_id>/', views.detail, name='detail'),
    path('detail/edit/<int:detail_id>/', views.detail_edit, name='detail_edit'),
    path('detail/update/<int:detail_id>/', views.detail_update, name='detail_update'),
    path('detail/delete/<int:detail_id>/', views.detail_delete, name='detail_delete'),

    path('documents/<int:apply_id>/', views.documents, name='documents'),


    # STAFF
    path('staff/login/',views.stafflogin,name='stafflogin'),
    path('staff/applys/',views.staffapplys,name='staffapplys'),
    path('staff/details/<int:apply_id>/',views.staffdetails,name='staffdetails'),
    path('staff/check_hospital/', views.check_hospital,name='check_hospital'),
    path('staff/audit_record/', views.audit_record, name='audit_record'),
    path('staff/audit/', views.audit, name='audit'),

    path('staff/scan_qr/', views.scan_qr, name='scan_qr'),
    path('staff/check/',views.staffcheck,name='staffcheck'),
    path('staff/checksubmit/<int:apply_id>/',views.check_submit,name='check_submit'),
    path('staff/qrcode/',views.staffqrcode,name='staffqrcode'),
    path('staff/r_details/<int:record_id>/',views.staffrdetails,name='staffrdetails'),


]