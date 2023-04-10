from django.shortcuts import render
from .forms import BillingForm
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