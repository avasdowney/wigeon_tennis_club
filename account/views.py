from django.shortcuts import render
from .forms import BillingForm
from django.views import generic
from django.utils import timezone
from members import models as view_members
from courts import models as view_reservations
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
    return render(request, 'account/editProfile.html')

def adminProfile(request):
    return render(request, 'account/adminProfile.html')

def treasurerProfile(request):
    return render(request, 'account/treasurerProfile.html')

class DirectoryView(generic.ListView):
    model = view_members.CustomUser
    context_object_name = 'user_list'
    template_name = 'members/directory.html'

    def get_queryset(self):
        return view_members.CustomUser.objects.all().order_by("last_name")

class ReservationView(generic.ListView):
    model = view_reservations.courtReservationForm
    context_object_name = 'reservation_list'
    template_name = 'account/adminProfile.html'

    def get_queryset(self):
        return view_reservations.courtReservationForm.objects.all()