from django.urls import path
from . import views

app_name = "account"
urlpatterns = [
    path('', views.account, name='index'),
    path('editProfile', views.editProfile, name="editProfile"),
    path('adminProfile', views.ReservationView.as_view(), name="adminProfile"),
    path('treasurerProfile', views.DirectoryView.as_view(), name="treasurerProfile"),
    path('reservations', views.reservations, name="reservations"),
]