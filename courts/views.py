from django.shortcuts import render
from .forms import ReservationForm
# Create your views here.

def index(request):
    form = ReservationForm()
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

