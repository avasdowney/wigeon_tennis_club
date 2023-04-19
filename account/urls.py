from django.urls import path
from . import views

urlpatterns = [
    path('', views.account, name='index'),
    path('bills', views.billing, name="billing"),
    path('editProfile', views.editProfile, name="editProfile"),
    path('adminProfile', views.ReservationView.as_view(), name="adminProfile"),
    path('treasurerProfile', views.DirectoryView.as_view(), name="treasurerProfile"),
]