from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('userlogin/', views.login, name='home'),
    path('news/', views.news, name='index'),
    path('directory/', views.directory, name='index'),
    path('create_account/', views.create_account, name='index'),
    path('member_profile/', views.member_profile, name='index'),
    path('admin_dashboard/', views.admin_dashboard, name='index'),
    path('treasurer_dashboard/', views.treasurer_dashboard, name='index'),
    path('payment/', views.payment, name='index'),
    path('reserve_court/', views.reserve_court, name='index'),
]