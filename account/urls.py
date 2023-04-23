from django.urls import path
from . import views

urlpatterns = [
    path('', views.account, name='index'),
    path('account', views.account, name="account"),
    path('bills', views.billing, name="billing"),
    path('editProfile', views.editProfile, name="editProfile"),
    path('adminProfile', views.ReservationView.as_view(), name="adminProfile"),
    path('treasurerProfile', views.DirectoryView.as_view(), name="treasurerProfile"),
    path('clubBills', views.BillView.as_view(), name="clubBills"),
    path('reservations', views.reservations, name="reservations"),
    path('deleteReservation/<reservation_id>', views.delete_reservation, name="deleteReservation"),
]