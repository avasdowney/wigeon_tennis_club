from django.urls import path
from . import views

urlpatterns = [
    path('', views.account, name='index'),
    path('bills', views.billing, name="billing"),
    path('editProfile', views.editProfile, name="editProfile"),
    path('adminProfile', views.adminProfile, name="adminProfile"),
]