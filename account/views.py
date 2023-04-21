from django.shortcuts import render
from .forms import BillingForm
from django.views import generic
from django.utils import timezone
from members import models as view_members
from members import forms as member_forms
from members import views as member_views
from courts import models as view_reservations
from .models import Bill
from django.views import generic
# Create your views here.

def account(request):
    return render(request, 'account/profilepage.html')

def billing(request):
    if request.method == 'POST':
        form = BillingForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'account/success.html', {})
    form = BillingForm()
    context = {'form': form}
    return render(request, 'account/bills.html', context)

def editProfile(request):
    current_user = request.user
    prefill = view_members.CustomUser(first_name=current_user.first_name, last_name=current_user.last_name, age=current_user.age, email=current_user.email, address=current_user.address, 
    phone=current_user.phone, is_public=current_user.is_public, pay_online=current_user.pay_online, 
    did_pay=current_user.did_pay, total_due=current_user.total_due)
    form = member_forms.SignUpForm(instance=prefill)
    return render(request, 'account/editProfile.html', {'form':form})

def adminProfile(request):
    return render(request, 'account/adminProfile.html')

def treasurerProfile(request):
    return render(request, 'account/treasurerProfile.html')

def reservations(request):
    return render(request, 'account/reservations.html')

class DirectoryView(generic.ListView):
    model = view_members.CustomUser
    context_object_name = 'user_list'
    template_name = 'account/treasurerProfile.html'

    def get_queryset(self):
        return view_members.CustomUser.objects.all().order_by("last_name")

class ReservationView(generic.ListView):
    model = view_reservations.courtReservationForm
    context_object_name = 'reservation_list'
    template_name = 'account/adminProfile.html'

    def get_queryset(self):
        return view_reservations.courtReservationForm.objects.all()
    
class BillView(generic.ListView):
    model = Bill
    context_object_name = 'bill_list'
    template_name = 'account/clubBills.html'

    def get_queryset(self):
        return Bill.objects.all()