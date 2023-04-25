from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views import generic
from django.utils import timezone
from members import models as view_members
from members import forms as member_forms
from members import views as member_views
from courts import models as view_reservations
from members.models import CustomUser
from django.views import generic
from django.http import HttpResponse
from .models import Bill
from .forms import PaymentFlagForm
# Create your views here.

def account(request):
    return render(request, 'account/profilepage.html')

def editProfile(request):
    current_user = view_members.CustomUser.objects.get(id=request.user.id)
    form = member_forms.SignUpForm(request.POST or None, instance=current_user)
    if form.is_valid():
        form.save()
        login(request, current_user)
        return render(request, 'account/updateSuccess.html')
    return render(request, 'account/editProfile.html', {'form':form})

def adminProfile(request):
    return render(request, 'account/adminProfile.html')

def treasurerProfile(request):
    return render(request, 'account/treasurerProfile.html')

def reservations(request):
    return render(request, 'account/reservations.html')

def delete_reservation(request, reservation_id):
    current_reservation = view_reservations.courtReservationForm.objects.get(pk=reservation_id)
    current_reservation.delete()
    return redirect('news')

def delete_account(request, account_id):
    current_account = view_members.CustomUser.objects.get(pk=account_id)
    current_account.delete()
    return redirect('news') 

def flag_payment_due(request, pk):
    if request.method == 'GET':
        user = view_members.CustomUser.objects.get(pk=pk)
        if user.payment_flag == True:
            user.payment_flag = False
        else:
            user.payment_flag = True
        user.save()
    return redirect('treasurerProfile')

class DirectoryView(generic.ListView):
    model = view_members.CustomUser
    context_object_name = 'user_list'
    template_name = 'account/treasurerProfile.html'

    def get_queryset(self):
        return view_members.CustomUser.objects.all().order_by("-total_due")

class ReservationView(generic.ListView):
    model = view_reservations.courtReservationForm
    context_object_name = 'reservation_list'
    template_name = 'account/adminProfile.html'

    def get_queryset(self):
        return view_reservations.courtReservationForm.objects.all()
    
class MyReservationView(generic.ListView):
    model = view_reservations.courtReservationForm
    context_object_name = 'my_reservation_list'
    template_name = 'account/reservations.html'

    def get_queryset(self):
        return view_reservations.courtReservationForm.objects.all().filter(guest1FName= 'Ava')
    
class BillView(generic.ListView):
    model = Bill
    context_object_name = 'bill_list'
    template_name = 'account/clubBills.html'

    def get_queryset(self):
        return Bill.objects.all()
