from django.shortcuts import render
from .forms import ReservationForm
# Create your views here.

def menu(request):
    return render(request, 'courts/menu.html')

def reservationform(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'courts/success.html', {})
    form = ReservationForm()
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

