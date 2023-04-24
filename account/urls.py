from django.urls import path
from . import views
from members import views as member_views

urlpatterns = [
    path('', views.account, name='index'),
    path('editProfile', views.editProfile, name="editProfile"),
    path('bills/<int:pk>', member_views.billing, name="billing"),
    path('adminProfile', views.ReservationView.as_view(), name="adminProfile"),
    path('treasurerProfile', views.DirectoryView.as_view(), name="treasurerProfile"),
    path('clubBills', views.BillView.as_view(), name="clubBills"),
    path('reservations', views.MyReservationView.as_view(), name="reservations"),
    path('deleteReservation/<reservation_id>', views.delete_reservation, name="deleteReservation"),
    path('deleteAccount/<account_id>', views.delete_account, name="deleteAccount"),
]