from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('userlogin/', views.login, name='index'),
]