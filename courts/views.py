from django.shortcuts import render
from .forms import ReservationForm
from .models import courtReservationForm
# Create your views here.

def menu(request):
    return render(request, 'courts/menu.html')

#court 1
def c1t1(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtNumber=1, courtTime= "8:00 - 9:30")
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def c1t2(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtNumber=1, courtTime= "9:30 - 11:00")
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def c1t3(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtNumber=1, courtTime= "11:00 - 12:30")
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def c1t4(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtNumber=1, courtTime= "12:30 - 2:00")
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def c1t5(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtNumber=1, courtTime= "2:00 - 3:30")
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def c1t6(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtNumber=1, courtTime= "3:30 - 5:00")
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

#court 2
def c2t1(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtNumber=2, courtTime= "8:00 - 9:30")
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def c2t2(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtNumber=2, courtTime= "9:30 - 11:00")
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def c2t3(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtNumber=2, courtTime= "11:00 - 12:30")
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def c2t4(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtNumber=2, courtTime= "12:30 - 2:00")
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def c2t5(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtNumber=2, courtTime= "2:00 - 3:30")
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def c2t6(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtNumber=2, courtTime= "3:30 - 5:00")
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

#court 3
def c3t1(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtNumber=3, courtTime= "8:00 - 9:30")
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def c3t2(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtNumber=3, courtTime= "9:30 - 11:00")
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def c3t3(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtNumber=3, courtTime= "11:00 - 12:30")
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def c3t4(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtNumber=3, courtTime= "12:30 - 2:00")
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def c3t5(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtNumber=3, courtTime= "2:00 - 3:30")
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def c3t6(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtNumber=3, courtTime= "3:30 - 5:00")
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

#court 4
def c4t1(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtNumber=4, courtTime= "8:00 - 9:30")
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def c4t2(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtNumber=4, courtTime= "9:30 - 11:00")
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def c4t3(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtNumber=4, courtTime= "11:00 - 12:30")
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def c4t4(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtNumber=4, courtTime= "12:30 - 2:00")
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def c4t5(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtNumber=4, courtTime= "2:00 - 3:30")
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def c4t6(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtNumber=4, courtTime= "3:30 - 5:00")
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

#court 5
def c5t1(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtNumber=5, courtTime= "8:00 - 9:30")
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def c5t2(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtNumber=5, courtTime= "9:30 - 11:00")
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def c5t3(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtNumber=5, courtTime= "11:00 - 12:30")
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def c5t4(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtNumber=5, courtTime= "12:30 - 2:00")
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def c5t5(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtNumber=5, courtTime= "2:00 - 3:30")
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def c5t6(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtNumber=5, courtTime= "3:30 - 5:00")
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

#court 6
def c6t1(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtNumber=6, courtTime= "8:00 - 9:30")
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def c6t2(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtNumber=6, courtTime= "9:30 - 11:00")
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def c6t3(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtNumber=6, courtTime= "11:00 - 12:30")
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def c6t4(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtNumber=6, courtTime= "12:30 - 2:00")
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def c6t5(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtNumber=6, courtTime= "2:00 - 3:30")
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def c6t6(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtNumber=6, courtTime= "3:30 - 5:00")
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

#court 7
def c7t1(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtNumber=7, courtTime= "8:00 - 9:30")
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def c7t2(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtNumber=7, courtTime= "9:30 - 11:00")
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def c7t3(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtNumber=7, courtTime= "11:00 - 12:30")
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def c7t4(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtNumber=7, courtTime= "12:30 - 2:00")
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def c7t5(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtNumber=7, courtTime= "2:00 - 3:30")
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def c7t6(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtNumber=7, courtTime= "3:30 - 5:00")
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

#court 8
def c8t1(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtNumber=8, courtTime= "8:00 - 9:30")
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def c8t2(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtNumber=8, courtTime= "9:30 - 11:00")
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def c8t3(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtNumber=8, courtTime= "11:00 - 12:30")
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def c8t4(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtNumber=8, courtTime= "12:30 - 2:00")
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def c8t5(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtNumber=8, courtTime= "2:00 - 3:30")
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def c8t6(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtNumber=8, courtTime= "3:30 - 5:00")
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

#court 9
def c9t1(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtNumber=9, courtTime= "8:00 - 9:30")
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def c9t2(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtNumber=9, courtTime= "9:30 - 11:00")
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def c9t3(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtNumber=9, courtTime= "11:00 - 12:30")
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def c9t4(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtNumber=9, courtTime= "12:30 - 2:00")
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def c9t5(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtNumber=9, courtTime= "2:00 - 3:30")
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def c9t6(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtNumber=9, courtTime= "3:30 - 5:00")
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

#court 10
def c10t1(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtNumber=10, courtTime= "8:00 - 9:30")
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def c10t2(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtNumber=10, courtTime= "9:30 - 11:00")
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def c10t3(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtNumber=10, courtTime= "11:00 - 12:30")
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def c10t4(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtNumber=10, courtTime= "12:30 - 2:00")
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def c10t5(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtNumber=10, courtTime= "2:00 - 3:30")
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def c10t6(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtNumber=10, courtTime= "3:30 - 5:00")
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

#court 11
def c11t1(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtNumber=11, courtTime= "8:00 - 9:30")
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def c11t2(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtNumber=11, courtTime= "9:30 - 11:00")
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def c11t3(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtNumber=11, courtTime= "11:00 - 12:30")
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def c11t4(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtNumber=11, courtTime= "12:30 - 2:00")
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def c11t5(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtNumber=11, courtTime= "2:00 - 3:30")
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def c11t6(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtNumber=11, courtTime= "3:30 - 5:00")
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

#court 12
def c12t1(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtNumber=12, courtTime= "8:00 - 9:30")
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def c12t2(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtNumber=12, courtTime= "9:30 - 11:00")
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def c12t3(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtNumber=12, courtTime= "11:00 - 12:30")
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def c12t4(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtNumber=12, courtTime= "12:30 - 2:00")
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def c12t5(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtNumber=12, courtTime= "2:00 - 3:30")
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def c12t6(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtNumber=12, courtTime= "3:30 - 5:00")
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)