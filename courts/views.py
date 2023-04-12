from django.shortcuts import render
from .forms import ReservationForm
from .models import courtReservationForm
# Create your views here.

    
def menu(request):
    #court 1
    try:
        c1t1 = courtReservationForm.objects.get(courtNumber=1, courtTime = "8:00 - 9:30")
    except courtReservationForm.DoesNotExist:
        c1t1 = None
    try:
        c1t2 = courtReservationForm.objects.get(courtNumber=1, courtTime = "9:30 - 11:00")
    except courtReservationForm.DoesNotExist:
        c1t2 = None
    try:
        c1t3 = courtReservationForm.objects.get(courtNumber=1, courtTime = "11:00 - 12:30")
    except courtReservationForm.DoesNotExist:
        c1t3 = None
    try:
        c1t4 = courtReservationForm.objects.get(courtNumber=1, courtTime = "12:30 - 2:00")
    except courtReservationForm.DoesNotExist:
        c1t4 = None
    try:
        c1t5 = courtReservationForm.objects.get(courtNumber=1, courtTime = "2:00 - 3:30")
    except courtReservationForm.DoesNotExist:
        c1t5 = None
    try:
        c1t6 = courtReservationForm.objects.get(courtNumber=1, courtTime = "3:30 - 5:00")
    except courtReservationForm.DoesNotExist:
        c1t6 = None

    #court 2
    try:
        c2t1 = courtReservationForm.objects.get(courtNumber=2, courtTime = "8:00 - 9:30")
    except courtReservationForm.DoesNotExist:
        c2t1 = None
    try:
        c2t2 = courtReservationForm.objects.get(courtNumber=2, courtTime = "9:30 - 11:00")
    except courtReservationForm.DoesNotExist:
        c2t2 = None
    try:
        c2t3 = courtReservationForm.objects.get(courtNumber=2, courtTime = "11:00 - 12:30")
    except courtReservationForm.DoesNotExist:
        c2t3 = None
    try:
        c2t4 = courtReservationForm.objects.get(courtNumber=2, courtTime = "12:30 - 2:00")
    except courtReservationForm.DoesNotExist:
        c2t4 = None
    try:
        c2t5 = courtReservationForm.objects.get(courtNumber=2, courtTime = "2:00 - 3:30")
    except courtReservationForm.DoesNotExist:
        c2t5 = None
    try:
        c2t6 = courtReservationForm.objects.get(courtNumber=2, courtTime = "3:30 - 5:00")
    except courtReservationForm.DoesNotExist:
        c2t6 = None

    #court 3
    try:
        c3t1 = courtReservationForm.objects.get(courtNumber=3, courtTime = "8:00 - 9:30")
    except courtReservationForm.DoesNotExist:
        c3t1 = None
    try:
        c3t2 = courtReservationForm.objects.get(courtNumber=3, courtTime = "9:30 - 11:00")
    except courtReservationForm.DoesNotExist:
        c3t2 = None
    try:
        c3t3 = courtReservationForm.objects.get(courtNumber=3, courtTime = "11:00 - 12:30")
    except courtReservationForm.DoesNotExist:
        c3t3 = None
    try:
        c3t4 = courtReservationForm.objects.get(courtNumber=3, courtTime = "12:30 - 2:00")
    except courtReservationForm.DoesNotExist:
        c3t4 = None
    try:
        c3t5 = courtReservationForm.objects.get(courtNumber=3, courtTime = "2:00 - 3:30")
    except courtReservationForm.DoesNotExist:
        c3t5 = None
    try:
        c3t6 = courtReservationForm.objects.get(courtNumber=3, courtTime = "3:30 - 5:00")
    except courtReservationForm.DoesNotExist:
        c3t6 = None
    
    #court 4
    try:
        c4t1 = courtReservationForm.objects.get(courtNumber=4, courtTime = "8:00 - 9:30")
    except courtReservationForm.DoesNotExist:
        c4t1 = None
    try:
        c4t2 = courtReservationForm.objects.get(courtNumber=4, courtTime = "9:30 - 11:00")
    except courtReservationForm.DoesNotExist:
        c4t2 = None
    try:
        c4t3 = courtReservationForm.objects.get(courtNumber=4, courtTime = "11:00 - 12:30")
    except courtReservationForm.DoesNotExist:
        c4t3 = None
    try:
        c4t4 = courtReservationForm.objects.get(courtNumber=4, courtTime = "12:30 - 2:00")
    except courtReservationForm.DoesNotExist:
        c4t4 = None
    try:
        c4t5 = courtReservationForm.objects.get(courtNumber=4, courtTime = "2:00 - 3:30")
    except courtReservationForm.DoesNotExist:
        c4t5 = None
    try:
        c4t6 = courtReservationForm.objects.get(courtNumber=4, courtTime = "3:30 - 5:00")
    except courtReservationForm.DoesNotExist:
        c4t6 = None

    #court 5
    try:
        c5t1 = courtReservationForm.objects.get(courtNumber=5, courtTime = "8:00 - 9:30")
    except courtReservationForm.DoesNotExist:
        c5t1 = None
    try:
        c5t2 = courtReservationForm.objects.get(courtNumber=5, courtTime = "9:30 - 11:00")
    except courtReservationForm.DoesNotExist:
        c5t2 = None
    try:
        c5t3 = courtReservationForm.objects.get(courtNumber=5, courtTime = "11:00 - 12:30")
    except courtReservationForm.DoesNotExist:
        c5t3 = None
    try:
        c5t4 = courtReservationForm.objects.get(courtNumber=5, courtTime = "12:30 - 2:00")
    except courtReservationForm.DoesNotExist:
        c5t4 = None
    try:
        c5t5 = courtReservationForm.objects.get(courtNumber=5, courtTime = "2:00 - 3:30")
    except courtReservationForm.DoesNotExist:
        c5t5 = None
    try:
        c5t6 = courtReservationForm.objects.get(courtNumber=5, courtTime = "3:30 - 5:00")
    except courtReservationForm.DoesNotExist:
        c5t6 = None

    #court 6
    try:
        c6t1 = courtReservationForm.objects.get(courtNumber=6, courtTime = "8:00 - 9:30")
    except courtReservationForm.DoesNotExist:
        c6t1 = None
    try:
        c6t2 = courtReservationForm.objects.get(courtNumber=6, courtTime = "9:30 - 11:00")
    except courtReservationForm.DoesNotExist:
        c6t2 = None
    try:
        c6t3 = courtReservationForm.objects.get(courtNumber=6, courtTime = "11:00 - 12:30")
    except courtReservationForm.DoesNotExist:
        c6t3 = None
    try:
        c6t4 = courtReservationForm.objects.get(courtNumber=6, courtTime = "12:30 - 2:00")
    except courtReservationForm.DoesNotExist:
        c6t4 = None
    try:
        c6t5 = courtReservationForm.objects.get(courtNumber=6, courtTime = "2:00 - 3:30")
    except courtReservationForm.DoesNotExist:
        c6t5 = None
    try:
        c6t6 = courtReservationForm.objects.get(courtNumber=6, courtTime = "3:30 - 5:00")
    except courtReservationForm.DoesNotExist:
        c6t6 = None
    
    #court 7
    try:
        c7t1 = courtReservationForm.objects.get(courtNumber=7, courtTime = "8:00 - 9:30")
    except courtReservationForm.DoesNotExist:
        c7t1 = None
    try:
        c7t2 = courtReservationForm.objects.get(courtNumber=7, courtTime = "9:30 - 11:00")
    except courtReservationForm.DoesNotExist:
        c7t2 = None
    try:
        c7t3 = courtReservationForm.objects.get(courtNumber=7, courtTime = "11:00 - 12:30")
    except courtReservationForm.DoesNotExist:
        c7t3 = None
    try:
        c7t4 = courtReservationForm.objects.get(courtNumber=7, courtTime = "12:30 - 2:00")
    except courtReservationForm.DoesNotExist:
        c7t4 = None
    try:
        c7t5 = courtReservationForm.objects.get(courtNumber=7, courtTime = "2:00 - 3:30")
    except courtReservationForm.DoesNotExist:
        c7t5 = None
    try:
        c7t6 = courtReservationForm.objects.get(courtNumber=7, courtTime = "3:30 - 5:00")
    except courtReservationForm.DoesNotExist:
        c7t6 = None
    
    #court 8
    try:
        c8t1 = courtReservationForm.objects.get(courtNumber=8, courtTime = "8:00 - 9:30")
    except courtReservationForm.DoesNotExist:
        c8t1 = None
    try:
        c8t2 = courtReservationForm.objects.get(courtNumber=8, courtTime = "9:30 - 11:00")
    except courtReservationForm.DoesNotExist:
        c8t2 = None
    try:
        c8t3 = courtReservationForm.objects.get(courtNumber=8, courtTime = "11:00 - 12:30")
    except courtReservationForm.DoesNotExist:
        c8t3 = None
    try:
        c8t4 = courtReservationForm.objects.get(courtNumber=8, courtTime = "12:30 - 2:00")
    except courtReservationForm.DoesNotExist:
        c8t4 = None
    try:
        c8t5 = courtReservationForm.objects.get(courtNumber=8, courtTime = "2:00 - 3:30")
    except courtReservationForm.DoesNotExist:
        c8t5 = None
    try:
        c8t6 = courtReservationForm.objects.get(courtNumber=8, courtTime = "3:30 - 5:00")
    except courtReservationForm.DoesNotExist:
        c8t6 = None

    #court 9
    try:
        c9t1 = courtReservationForm.objects.get(courtNumber=9, courtTime = "8:00 - 9:30")
    except courtReservationForm.DoesNotExist:
        c9t1 = None
    try:
        c9t2 = courtReservationForm.objects.get(courtNumber=9, courtTime = "9:30 - 11:00")
    except courtReservationForm.DoesNotExist:
        c9t2 = None
    try:
        c9t3 = courtReservationForm.objects.get(courtNumber=9, courtTime = "11:00 - 12:30")
    except courtReservationForm.DoesNotExist:
        c9t3 = None
    try:
        c9t4 = courtReservationForm.objects.get(courtNumber=9, courtTime = "12:30 - 2:00")
    except courtReservationForm.DoesNotExist:
        c9t4 = None
    try:
        c9t5 = courtReservationForm.objects.get(courtNumber=9, courtTime = "2:00 - 3:30")
    except courtReservationForm.DoesNotExist:
        c9t5 = None
    try:
        c9t6 = courtReservationForm.objects.get(courtNumber=9, courtTime = "3:30 - 5:00")
    except courtReservationForm.DoesNotExist:
        c9t6 = None

    #court 10
    try:
        c10t1 = courtReservationForm.objects.get(courtNumber=10, courtTime = "8:00 - 9:30")
    except courtReservationForm.DoesNotExist:
        c10t1 = None
    try:
        c10t2 = courtReservationForm.objects.get(courtNumber=10, courtTime = "9:30 - 11:00")
    except courtReservationForm.DoesNotExist:
        c10t2 = None
    try:
        c10t3 = courtReservationForm.objects.get(courtNumber=10, courtTime = "11:00 - 12:30")
    except courtReservationForm.DoesNotExist:
        c10t3 = None
    try:
        c10t4 = courtReservationForm.objects.get(courtNumber=10, courtTime = "12:30 - 2:00")
    except courtReservationForm.DoesNotExist:
        c10t4 = None
    try:
        c10t5 = courtReservationForm.objects.get(courtNumber=10, courtTime = "2:00 - 3:30")
    except courtReservationForm.DoesNotExist:
        c10t5 = None
    try:
        c10t6 = courtReservationForm.objects.get(courtNumber=10, courtTime = "3:30 - 5:00")
    except courtReservationForm.DoesNotExist:
        c10t6 = None

    #court 11
    try:
        c11t1 = courtReservationForm.objects.get(courtNumber=11, courtTime = "8:00 - 9:30")
    except courtReservationForm.DoesNotExist:
        c11t1 = None
    try:
        c11t2 = courtReservationForm.objects.get(courtNumber=11, courtTime = "9:30 - 11:00")
    except courtReservationForm.DoesNotExist:
        c11t2 = None
    try:
        c11t3 = courtReservationForm.objects.get(courtNumber=11, courtTime = "11:00 - 12:30")
    except courtReservationForm.DoesNotExist:
        c11t3 = None
    try:
        c11t4 = courtReservationForm.objects.get(courtNumber=11, courtTime = "12:30 - 2:00")
    except courtReservationForm.DoesNotExist:
        c11t4 = None
    try:
        c11t5 = courtReservationForm.objects.get(courtNumber=11, courtTime = "2:00 - 3:30")
    except courtReservationForm.DoesNotExist:
        c11t5 = None
    try:
        c11t6 = courtReservationForm.objects.get(courtNumber=11, courtTime = "3:30 - 5:00")
    except courtReservationForm.DoesNotExist:
        c11t6 = None

    #court 12
    try:
        c12t1 = courtReservationForm.objects.get(courtNumber=12, courtTime = "8:00 - 9:30")
    except courtReservationForm.DoesNotExist:
        c12t1 = None
    try:
        c12t2 = courtReservationForm.objects.get(courtNumber=12, courtTime = "9:30 - 11:00")
    except courtReservationForm.DoesNotExist:
        c12t2 = None
    try:
        c12t3 = courtReservationForm.objects.get(courtNumber=12, courtTime = "11:00 - 12:30")
    except courtReservationForm.DoesNotExist:
        c12t3 = None
    try:
        c12t4 = courtReservationForm.objects.get(courtNumber=12, courtTime = "12:30 - 2:00")
    except courtReservationForm.DoesNotExist:
        c12t4 = None
    try:
        c12t5 = courtReservationForm.objects.get(courtNumber=12, courtTime = "2:00 - 3:30")
    except courtReservationForm.DoesNotExist:
        c12t5 = None
    try:
        c12t6 = courtReservationForm.objects.get(courtNumber=12, courtTime = "3:30 - 5:00")
    except courtReservationForm.DoesNotExist:
        c12t6 = None


    context = {'c1t1' :c1t1, 'c1t2' : c1t2, 'c1t3' : c1t3, 'c1t4' :c1t4, 'c1t5' : c1t5, 'c1t6' : c1t6,
               'c2t1' :c2t1, 'c2t2' : c2t2, 'c2t3' : c2t3, 'c2t4' :c2t4, 'c2t5' : c2t5, 'c2t6' : c2t6,
               'c3t1' :c3t1, 'c3t2' : c3t2, 'c3t3' : c3t3, 'c3t4' :c3t4, 'c3t5' : c3t5, 'c3t6' : c3t6,
               'c4t1' :c4t1, 'c4t2' : c4t2, 'c4t3' : c4t3, 'c4t4' :c4t4, 'c4t5' : c4t5, 'c4t6' : c4t6,
               'c5t1' :c5t1, 'c5t2' : c5t2, 'c5t3' : c5t3, 'c5t4' :c5t4, 'c5t5' : c5t5, 'c5t6' : c5t6,
               'c6t1' :c6t1, 'c6t2' : c6t2, 'c6t3' : c6t3, 'c6t4' :c6t4, 'c6t5' : c6t5, 'c6t6' : c6t6,
               'c7t1' :c7t1, 'c7t2' : c7t2, 'c7t3' : c7t3, 'c7t4' :c7t4, 'c7t5' : c7t5, 'c7t6' : c7t6,
               'c8t1' :c8t1, 'c8t2' : c8t2, 'c8t3' : c8t3, 'c8t4' :c8t4, 'c8t5' : c8t5, 'c8t6' : c8t6,
               'c9t1' :c9t1, 'c9t2' : c9t2, 'c9t3' : c9t3, 'c9t4' :c9t4, 'c9t5' : c9t5, 'c9t6' : c9t6,
               'c10t1' :c10t1, 'c10t2' : c10t2, 'c10t3' : c10t3, 'c10t4' :c10t4, 'c10t5' : c10t5, 'c10t6' : c10t6,
               'c11t1' :c11t1, 'c11t2' : c11t2, 'c11t3' : c11t3, 'c11t4' :c11t4, 'c11t5' : c11t5, 'c11t6' : c11t6,
               'c12t1' :c12t1, 'c12t2' : c12t2, 'c12t3' : c12t3, 'c12t4' :c12t4, 'c12t5' : c12t5, 'c12t6' : c12t6
               }
    return render(request, 'courts/menu.html',context)

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