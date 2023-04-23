from django.shortcuts import render
from .forms import ReservationForm
from .models import courtReservationForm
from datetime import datetime, timedelta
from members.models import CustomUser
from account.forms import BillingForm
# Create your views here.

    
def menu(request):
    #dates
    date1 = datetime.now()
    date2 = (datetime.now()+timedelta(1))
    date3 = (datetime.now()+timedelta(2))
    date4 = (datetime.now()+timedelta(3))
    date5 = (datetime.now()+timedelta(4))
    date6 = (datetime.now()+timedelta(5))
    date7 = (datetime.now()+timedelta(6))

    date1Disp = datetime.now().strftime("%b. %d, %Y")
    date2Disp = (datetime.now()+timedelta(1)).strftime("%b. %d, %Y")
    date3Disp = (datetime.now()+timedelta(2)).strftime("%b. %d, %Y")
    date4Disp = (datetime.now()+timedelta(3)).strftime("%b. %d, %Y")
    date5Disp = (datetime.now()+timedelta(4)).strftime("%b. %d, %Y")
    date6Disp = (datetime.now()+timedelta(5)).strftime("%b. %d, %Y")
    date7Disp = (datetime.now()+timedelta(6)).strftime("%b. %d, %Y")
    
    #court 1
    try:
        c1t1 = courtReservationForm.objects.get(courtDate = date1,courtNumber=1, courtTime = "8:00 - 9:30")
    except courtReservationForm.DoesNotExist:
        c1t1 = None
    try:
        c1t2 = courtReservationForm.objects.get(courtDate = date1,courtNumber=1, courtTime = "9:30 - 11:00")
    except courtReservationForm.DoesNotExist:
        c1t2 = None
    try:
        c1t3 = courtReservationForm.objects.get(courtDate = date1,courtNumber=1, courtTime = "11:00 - 12:30")
    except courtReservationForm.DoesNotExist:
        c1t3 = None
    try:
        c1t4 = courtReservationForm.objects.get(courtDate = date1,courtNumber=1, courtTime = "12:30 - 2:00")
    except courtReservationForm.DoesNotExist:
        c1t4 = None
    try:
        c1t5 = courtReservationForm.objects.get(courtDate = date1,courtNumber=1, courtTime = "2:00 - 3:30")
    except courtReservationForm.DoesNotExist:
        c1t5 = None
    try:
        c1t6 = courtReservationForm.objects.get(courtDate = date1,courtNumber=1, courtTime = "3:30 - 5:00")
    except courtReservationForm.DoesNotExist:
        c1t6 = None

    #court 2
    try:
        c2t1 = courtReservationForm.objects.get(courtDate = date1,courtNumber=2, courtTime = "8:00 - 9:30")
    except courtReservationForm.DoesNotExist:
        c2t1 = None
    try:
        c2t2 = courtReservationForm.objects.get(courtDate = date1,courtNumber=2, courtTime = "9:30 - 11:00")
    except courtReservationForm.DoesNotExist:
        c2t2 = None
    try:
        c2t3 = courtReservationForm.objects.get(courtDate = date1,courtNumber=2, courtTime = "11:00 - 12:30")
    except courtReservationForm.DoesNotExist:
        c2t3 = None
    try:
        c2t4 = courtReservationForm.objects.get(courtDate = date1,courtNumber=2, courtTime = "12:30 - 2:00")
    except courtReservationForm.DoesNotExist:
        c2t4 = None
    try:
        c2t5 = courtReservationForm.objects.get(courtDate = date1,courtNumber=2, courtTime = "2:00 - 3:30")
    except courtReservationForm.DoesNotExist:
        c2t5 = None
    try:
        c2t6 = courtReservationForm.objects.get(courtDate = date1,courtNumber=2, courtTime = "3:30 - 5:00")
    except courtReservationForm.DoesNotExist:
        c2t6 = None

    #court 3
    try:
        c3t1 = courtReservationForm.objects.get(courtDate = date1,courtNumber=3, courtTime = "8:00 - 9:30")
    except courtReservationForm.DoesNotExist:
        c3t1 = None
    try:
        c3t2 = courtReservationForm.objects.get(courtDate = date1,courtNumber=3, courtTime = "9:30 - 11:00")
    except courtReservationForm.DoesNotExist:
        c3t2 = None
    try:
        c3t3 = courtReservationForm.objects.get(courtDate = date1,courtNumber=3, courtTime = "11:00 - 12:30")
    except courtReservationForm.DoesNotExist:
        c3t3 = None
    try:
        c3t4 = courtReservationForm.objects.get(courtDate = date1,courtNumber=3, courtTime = "12:30 - 2:00")
    except courtReservationForm.DoesNotExist:
        c3t4 = None
    try:
        c3t5 = courtReservationForm.objects.get(courtDate = date1,courtNumber=3, courtTime = "2:00 - 3:30")
    except courtReservationForm.DoesNotExist:
        c3t5 = None
    try:
        c3t6 = courtReservationForm.objects.get(courtDate = date1,courtNumber=3, courtTime = "3:30 - 5:00")
    except courtReservationForm.DoesNotExist:
        c3t6 = None
    
    #court 4
    try:
        c4t1 = courtReservationForm.objects.get(courtDate = date1,courtNumber=4, courtTime = "8:00 - 9:30")
    except courtReservationForm.DoesNotExist:
        c4t1 = None
    try:
        c4t2 = courtReservationForm.objects.get(courtDate = date1,courtNumber=4, courtTime = "9:30 - 11:00")
    except courtReservationForm.DoesNotExist:
        c4t2 = None
    try:
        c4t3 = courtReservationForm.objects.get(courtDate = date1,courtNumber=4, courtTime = "11:00 - 12:30")
    except courtReservationForm.DoesNotExist:
        c4t3 = None
    try:
        c4t4 = courtReservationForm.objects.get(courtDate = date1,courtNumber=4, courtTime = "12:30 - 2:00")
    except courtReservationForm.DoesNotExist:
        c4t4 = None
    try:
        c4t5 = courtReservationForm.objects.get(courtDate = date1,courtNumber=4, courtTime = "2:00 - 3:30")
    except courtReservationForm.DoesNotExist:
        c4t5 = None
    try:
        c4t6 = courtReservationForm.objects.get(courtDate = date1,courtNumber=4, courtTime = "3:30 - 5:00")
    except courtReservationForm.DoesNotExist:
        c4t6 = None

    #court 5
    try:
        c5t1 = courtReservationForm.objects.get(courtDate = date1,courtNumber=5, courtTime = "8:00 - 9:30")
    except courtReservationForm.DoesNotExist:
        c5t1 = None
    try:
        c5t2 = courtReservationForm.objects.get(courtDate = date1,courtNumber=5, courtTime = "9:30 - 11:00")
    except courtReservationForm.DoesNotExist:
        c5t2 = None
    try:
        c5t3 = courtReservationForm.objects.get(courtDate = date1,courtNumber=5, courtTime = "11:00 - 12:30")
    except courtReservationForm.DoesNotExist:
        c5t3 = None
    try:
        c5t4 = courtReservationForm.objects.get(courtDate = date1,courtNumber=5, courtTime = "12:30 - 2:00")
    except courtReservationForm.DoesNotExist:
        c5t4 = None
    try:
        c5t5 = courtReservationForm.objects.get(courtDate = date1,courtNumber=5, courtTime = "2:00 - 3:30")
    except courtReservationForm.DoesNotExist:
        c5t5 = None
    try:
        c5t6 = courtReservationForm.objects.get(courtDate = date1,courtNumber=5, courtTime = "3:30 - 5:00")
    except courtReservationForm.DoesNotExist:
        c5t6 = None

    #court 6
    try:
        c6t1 = courtReservationForm.objects.get(courtDate = date1,courtNumber=6, courtTime = "8:00 - 9:30")
    except courtReservationForm.DoesNotExist:
        c6t1 = None
    try:
        c6t2 = courtReservationForm.objects.get(courtDate = date1,courtNumber=6, courtTime = "9:30 - 11:00")
    except courtReservationForm.DoesNotExist:
        c6t2 = None
    try:
        c6t3 = courtReservationForm.objects.get(courtDate = date1,courtNumber=6, courtTime = "11:00 - 12:30")
    except courtReservationForm.DoesNotExist:
        c6t3 = None
    try:
        c6t4 = courtReservationForm.objects.get(courtDate = date1,courtNumber=6, courtTime = "12:30 - 2:00")
    except courtReservationForm.DoesNotExist:
        c6t4 = None
    try:
        c6t5 = courtReservationForm.objects.get(courtDate = date1,courtNumber=6, courtTime = "2:00 - 3:30")
    except courtReservationForm.DoesNotExist:
        c6t5 = None
    try:
        c6t6 = courtReservationForm.objects.get(courtDate = date1,courtNumber=6, courtTime = "3:30 - 5:00")
    except courtReservationForm.DoesNotExist:
        c6t6 = None
    
    #court 7
    try:
        c7t1 = courtReservationForm.objects.get(courtDate = date1,courtNumber=7, courtTime = "8:00 - 9:30")
    except courtReservationForm.DoesNotExist:
        c7t1 = None
    try:
        c7t2 = courtReservationForm.objects.get(courtDate = date1,courtNumber=7, courtTime = "9:30 - 11:00")
    except courtReservationForm.DoesNotExist:
        c7t2 = None
    try:
        c7t3 = courtReservationForm.objects.get(courtDate = date1,courtNumber=7, courtTime = "11:00 - 12:30")
    except courtReservationForm.DoesNotExist:
        c7t3 = None
    try:
        c7t4 = courtReservationForm.objects.get(courtDate = date1,courtNumber=7, courtTime = "12:30 - 2:00")
    except courtReservationForm.DoesNotExist:
        c7t4 = None
    try:
        c7t5 = courtReservationForm.objects.get(courtDate = date1,courtNumber=7, courtTime = "2:00 - 3:30")
    except courtReservationForm.DoesNotExist:
        c7t5 = None
    try:
        c7t6 = courtReservationForm.objects.get(courtDate = date1,courtNumber=7, courtTime = "3:30 - 5:00")
    except courtReservationForm.DoesNotExist:
        c7t6 = None
    
    #court 8
    try:
        c8t1 = courtReservationForm.objects.get(courtDate = date1,courtNumber=8, courtTime = "8:00 - 9:30")
    except courtReservationForm.DoesNotExist:
        c8t1 = None
    try:
        c8t2 = courtReservationForm.objects.get(courtDate = date1,courtNumber=8, courtTime = "9:30 - 11:00")
    except courtReservationForm.DoesNotExist:
        c8t2 = None
    try:
        c8t3 = courtReservationForm.objects.get(courtDate = date1,courtNumber=8, courtTime = "11:00 - 12:30")
    except courtReservationForm.DoesNotExist:
        c8t3 = None
    try:
        c8t4 = courtReservationForm.objects.get(courtDate = date1,courtNumber=8, courtTime = "12:30 - 2:00")
    except courtReservationForm.DoesNotExist:
        c8t4 = None
    try:
        c8t5 = courtReservationForm.objects.get(courtDate = date1,courtNumber=8, courtTime = "2:00 - 3:30")
    except courtReservationForm.DoesNotExist:
        c8t5 = None
    try:
        c8t6 = courtReservationForm.objects.get(courtDate = date1,courtNumber=8, courtTime = "3:30 - 5:00")
    except courtReservationForm.DoesNotExist:
        c8t6 = None

    #court 9
    try:
        c9t1 = courtReservationForm.objects.get(courtDate = date1,courtNumber=9, courtTime = "8:00 - 9:30")
    except courtReservationForm.DoesNotExist:
        c9t1 = None
    try:
        c9t2 = courtReservationForm.objects.get(courtDate = date1,courtNumber=9, courtTime = "9:30 - 11:00")
    except courtReservationForm.DoesNotExist:
        c9t2 = None
    try:
        c9t3 = courtReservationForm.objects.get(courtDate = date1,courtNumber=9, courtTime = "11:00 - 12:30")
    except courtReservationForm.DoesNotExist:
        c9t3 = None
    try:
        c9t4 = courtReservationForm.objects.get(courtDate = date1,courtNumber=9, courtTime = "12:30 - 2:00")
    except courtReservationForm.DoesNotExist:
        c9t4 = None
    try:
        c9t5 = courtReservationForm.objects.get(courtDate = date1,courtNumber=9, courtTime = "2:00 - 3:30")
    except courtReservationForm.DoesNotExist:
        c9t5 = None
    try:
        c9t6 = courtReservationForm.objects.get(courtDate = date1,courtNumber=9, courtTime = "3:30 - 5:00")
    except courtReservationForm.DoesNotExist:
        c9t6 = None

    #court 10
    try:
        c10t1 = courtReservationForm.objects.get(courtDate = date1,courtNumber=10, courtTime = "8:00 - 9:30")
    except courtReservationForm.DoesNotExist:
        c10t1 = None
    try:
        c10t2 = courtReservationForm.objects.get(courtDate = date1,courtNumber=10, courtTime = "9:30 - 11:00")
    except courtReservationForm.DoesNotExist:
        c10t2 = None
    try:
        c10t3 = courtReservationForm.objects.get(courtDate = date1,courtNumber=10, courtTime = "11:00 - 12:30")
    except courtReservationForm.DoesNotExist:
        c10t3 = None
    try:
        c10t4 = courtReservationForm.objects.get(courtDate = date1,courtNumber=10, courtTime = "12:30 - 2:00")
    except courtReservationForm.DoesNotExist:
        c10t4 = None
    try:
        c10t5 = courtReservationForm.objects.get(courtDate = date1,courtNumber=10, courtTime = "2:00 - 3:30")
    except courtReservationForm.DoesNotExist:
        c10t5 = None
    try:
        c10t6 = courtReservationForm.objects.get(courtDate = date1,courtNumber=10, courtTime = "3:30 - 5:00")
    except courtReservationForm.DoesNotExist:
        c10t6 = None

    #court 11
    try:
        c11t1 = courtReservationForm.objects.get(courtDate = date1,courtNumber=11, courtTime = "8:00 - 9:30")
    except courtReservationForm.DoesNotExist:
        c11t1 = None
    try:
        c11t2 = courtReservationForm.objects.get(courtDate = date1,courtNumber=11, courtTime = "9:30 - 11:00")
    except courtReservationForm.DoesNotExist:
        c11t2 = None
    try:
        c11t3 = courtReservationForm.objects.get(courtDate = date1,courtNumber=11, courtTime = "11:00 - 12:30")
    except courtReservationForm.DoesNotExist:
        c11t3 = None
    try:
        c11t4 = courtReservationForm.objects.get(courtDate = date1,courtNumber=11, courtTime = "12:30 - 2:00")
    except courtReservationForm.DoesNotExist:
        c11t4 = None
    try:
        c11t5 = courtReservationForm.objects.get(courtDate = date1,courtNumber=11, courtTime = "2:00 - 3:30")
    except courtReservationForm.DoesNotExist:
        c11t5 = None
    try:
        c11t6 = courtReservationForm.objects.get(courtDate = date1,courtNumber=11, courtTime = "3:30 - 5:00")
    except courtReservationForm.DoesNotExist:
        c11t6 = None

    #court 12
    try:
        c12t1 = courtReservationForm.objects.get(courtDate = date1,courtNumber=12, courtTime = "8:00 - 9:30")
    except courtReservationForm.DoesNotExist:
        c12t1 = None
    try:
        c12t2 = courtReservationForm.objects.get(courtDate = date1,courtNumber=12, courtTime = "9:30 - 11:00")
    except courtReservationForm.DoesNotExist:
        c12t2 = None
    try:
        c12t3 = courtReservationForm.objects.get(courtDate = date1,courtNumber=12, courtTime = "11:00 - 12:30")
    except courtReservationForm.DoesNotExist:
        c12t3 = None
    try:
        c12t4 = courtReservationForm.objects.get(courtDate = date1,courtNumber=12, courtTime = "12:30 - 2:00")
    except courtReservationForm.DoesNotExist:
        c12t4 = None
    try:
        c12t5 = courtReservationForm.objects.get(courtDate = date1,courtNumber=12, courtTime = "2:00 - 3:30")
    except courtReservationForm.DoesNotExist:
        c12t5 = None
    try:
        c12t6 = courtReservationForm.objects.get(courtDate = date1,courtNumber=12, courtTime = "3:30 - 5:00")
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
               'c12t1' :c12t1, 'c12t2' : c12t2, 'c12t3' : c12t3, 'c12t4' :c12t4, 'c12t5' : c12t5, 'c12t6' : c12t6,
               'date1' :date1, 'date2':date2, 'date3':date3, 'date4':date4, 'date5':date5, 'date6':date6, 'date7':date7,
               'date1Disp':date1Disp, 'date2Disp':date2Disp,'date3Disp':date3Disp,'date4Disp':date4Disp,
               'date5Disp':date5Disp,'date6Disp':date6Disp,'date7Disp':date7Disp
               }
    return render(request, 'courts/menu.html',context)

def menu2(request):
    #dates
    date1 = datetime.now()
    date2 = (datetime.now()+timedelta(1))
    date3 = (datetime.now()+timedelta(2))
    date4 = (datetime.now()+timedelta(3))
    date5 = (datetime.now()+timedelta(4))
    date6 = (datetime.now()+timedelta(5))
    date7 = (datetime.now()+timedelta(6))

    date1Disp = datetime.now().strftime("%b. %d, %Y")
    date2Disp = (datetime.now()+timedelta(1)).strftime("%b. %d, %Y")
    date3Disp = (datetime.now()+timedelta(2)).strftime("%b. %d, %Y")
    date4Disp = (datetime.now()+timedelta(3)).strftime("%b. %d, %Y")
    date5Disp = (datetime.now()+timedelta(4)).strftime("%b. %d, %Y")
    date6Disp = (datetime.now()+timedelta(5)).strftime("%b. %d, %Y")
    date7Disp = (datetime.now()+timedelta(6)).strftime("%b. %d, %Y")

    #court 1
    try:
        c1t1 = courtReservationForm.objects.get(courtDate = date2, courtNumber=1, courtTime = "8:00 - 9:30")
    except courtReservationForm.DoesNotExist:
        c1t1 = None
    try:
        c1t2 = courtReservationForm.objects.get(courtDate = date2,courtNumber=1, courtTime = "9:30 - 11:00")
    except courtReservationForm.DoesNotExist:
        c1t2 = None
    try:
        c1t3 = courtReservationForm.objects.get(courtDate = date2,courtNumber=1, courtTime = "11:00 - 12:30")
    except courtReservationForm.DoesNotExist:
        c1t3 = None
    try:
        c1t4 = courtReservationForm.objects.get(courtDate = date2,courtNumber=1, courtTime = "12:30 - 2:00")
    except courtReservationForm.DoesNotExist:
        c1t4 = None
    try:
        c1t5 = courtReservationForm.objects.get(courtDate = date2,courtNumber=1, courtTime = "2:00 - 3:30")
    except courtReservationForm.DoesNotExist:
        c1t5 = None
    try:
        c1t6 = courtReservationForm.objects.get(courtDate = date2,courtNumber=1, courtTime = "3:30 - 5:00")
    except courtReservationForm.DoesNotExist:
        c1t6 = None

    #court 2
    try:
        c2t1 = courtReservationForm.objects.get(courtDate = date2,courtNumber=2, courtTime = "8:00 - 9:30")
    except courtReservationForm.DoesNotExist:
        c2t1 = None
    try:
        c2t2 = courtReservationForm.objects.get(courtDate = date2,courtNumber=2, courtTime = "9:30 - 11:00")
    except courtReservationForm.DoesNotExist:
        c2t2 = None
    try:
        c2t3 = courtReservationForm.objects.get(courtDate = date2,courtNumber=2, courtTime = "11:00 - 12:30")
    except courtReservationForm.DoesNotExist:
        c2t3 = None
    try:
        c2t4 = courtReservationForm.objects.get(courtDate = date2,courtNumber=2, courtTime = "12:30 - 2:00")
    except courtReservationForm.DoesNotExist:
        c2t4 = None
    try:
        c2t5 = courtReservationForm.objects.get(courtDate = date2,courtNumber=2, courtTime = "2:00 - 3:30")
    except courtReservationForm.DoesNotExist:
        c2t5 = None
    try:
        c2t6 = courtReservationForm.objects.get(courtDate = date2,courtNumber=2, courtTime = "3:30 - 5:00")
    except courtReservationForm.DoesNotExist:
        c2t6 = None

    #court 3
    try:
        c3t1 = courtReservationForm.objects.get(courtDate = date2,courtNumber=3, courtTime = "8:00 - 9:30")
    except courtReservationForm.DoesNotExist:
        c3t1 = None
    try:
        c3t2 = courtReservationForm.objects.get(courtDate = date2,courtNumber=3, courtTime = "9:30 - 11:00")
    except courtReservationForm.DoesNotExist:
        c3t2 = None
    try:
        c3t3 = courtReservationForm.objects.get(courtDate = date2,courtNumber=3, courtTime = "11:00 - 12:30")
    except courtReservationForm.DoesNotExist:
        c3t3 = None
    try:
        c3t4 = courtReservationForm.objects.get(courtDate = date2,courtNumber=3, courtTime = "12:30 - 2:00")
    except courtReservationForm.DoesNotExist:
        c3t4 = None
    try:
        c3t5 = courtReservationForm.objects.get(courtDate = date2,courtNumber=3, courtTime = "2:00 - 3:30")
    except courtReservationForm.DoesNotExist:
        c3t5 = None
    try:
        c3t6 = courtReservationForm.objects.get(courtDate = date2,courtNumber=3, courtTime = "3:30 - 5:00")
    except courtReservationForm.DoesNotExist:
        c3t6 = None
    
    #court 4
    try:
        c4t1 = courtReservationForm.objects.get(courtDate = date2,courtNumber=4, courtTime = "8:00 - 9:30")
    except courtReservationForm.DoesNotExist:
        c4t1 = None
    try:
        c4t2 = courtReservationForm.objects.get(courtDate = date2,courtNumber=4, courtTime = "9:30 - 11:00")
    except courtReservationForm.DoesNotExist:
        c4t2 = None
    try:
        c4t3 = courtReservationForm.objects.get(courtDate = date2,courtNumber=4, courtTime = "11:00 - 12:30")
    except courtReservationForm.DoesNotExist:
        c4t3 = None
    try:
        c4t4 = courtReservationForm.objects.get(courtDate = date2,courtNumber=4, courtTime = "12:30 - 2:00")
    except courtReservationForm.DoesNotExist:
        c4t4 = None
    try:
        c4t5 = courtReservationForm.objects.get(courtDate = date2,courtNumber=4, courtTime = "2:00 - 3:30")
    except courtReservationForm.DoesNotExist:
        c4t5 = None
    try:
        c4t6 = courtReservationForm.objects.get(courtDate = date2,courtNumber=4, courtTime = "3:30 - 5:00")
    except courtReservationForm.DoesNotExist:
        c4t6 = None

    #court 5
    try:
        c5t1 = courtReservationForm.objects.get(courtDate = date2,courtNumber=5, courtTime = "8:00 - 9:30")
    except courtReservationForm.DoesNotExist:
        c5t1 = None
    try:
        c5t2 = courtReservationForm.objects.get(courtDate = date2,courtNumber=5, courtTime = "9:30 - 11:00")
    except courtReservationForm.DoesNotExist:
        c5t2 = None
    try:
        c5t3 = courtReservationForm.objects.get(courtDate = date2,courtNumber=5, courtTime = "11:00 - 12:30")
    except courtReservationForm.DoesNotExist:
        c5t3 = None
    try:
        c5t4 = courtReservationForm.objects.get(courtDate = date2,courtNumber=5, courtTime = "12:30 - 2:00")
    except courtReservationForm.DoesNotExist:
        c5t4 = None
    try:
        c5t5 = courtReservationForm.objects.get(courtDate = date2,courtNumber=5, courtTime = "2:00 - 3:30")
    except courtReservationForm.DoesNotExist:
        c5t5 = None
    try:
        c5t6 = courtReservationForm.objects.get(courtDate = date2,courtNumber=5, courtTime = "3:30 - 5:00")
    except courtReservationForm.DoesNotExist:
        c5t6 = None

    #court 6
    try:
        c6t1 = courtReservationForm.objects.get(courtDate = date2,courtNumber=6, courtTime = "8:00 - 9:30")
    except courtReservationForm.DoesNotExist:
        c6t1 = None
    try:
        c6t2 = courtReservationForm.objects.get(courtDate = date2,courtNumber=6, courtTime = "9:30 - 11:00")
    except courtReservationForm.DoesNotExist:
        c6t2 = None
    try:
        c6t3 = courtReservationForm.objects.get(courtDate = date2,courtNumber=6, courtTime = "11:00 - 12:30")
    except courtReservationForm.DoesNotExist:
        c6t3 = None
    try:
        c6t4 = courtReservationForm.objects.get(courtDate = date2,courtNumber=6, courtTime = "12:30 - 2:00")
    except courtReservationForm.DoesNotExist:
        c6t4 = None
    try:
        c6t5 = courtReservationForm.objects.get(courtDate = date2,courtNumber=6, courtTime = "2:00 - 3:30")
    except courtReservationForm.DoesNotExist:
        c6t5 = None
    try:
        c6t6 = courtReservationForm.objects.get(courtDate = date2,courtNumber=6, courtTime = "3:30 - 5:00")
    except courtReservationForm.DoesNotExist:
        c6t6 = None
    
    #court 7
    try:
        c7t1 = courtReservationForm.objects.get(courtDate = date2,courtNumber=7, courtTime = "8:00 - 9:30")
    except courtReservationForm.DoesNotExist:
        c7t1 = None
    try:
        c7t2 = courtReservationForm.objects.get(courtDate = date2,courtNumber=7, courtTime = "9:30 - 11:00")
    except courtReservationForm.DoesNotExist:
        c7t2 = None
    try:
        c7t3 = courtReservationForm.objects.get(courtDate = date2,courtNumber=7, courtTime = "11:00 - 12:30")
    except courtReservationForm.DoesNotExist:
        c7t3 = None
    try:
        c7t4 = courtReservationForm.objects.get(courtDate = date2,courtNumber=7, courtTime = "12:30 - 2:00")
    except courtReservationForm.DoesNotExist:
        c7t4 = None
    try:
        c7t5 = courtReservationForm.objects.get(courtDate = date2,courtNumber=7, courtTime = "2:00 - 3:30")
    except courtReservationForm.DoesNotExist:
        c7t5 = None
    try:
        c7t6 = courtReservationForm.objects.get(courtDate = date2,courtNumber=7, courtTime = "3:30 - 5:00")
    except courtReservationForm.DoesNotExist:
        c7t6 = None
    
    #court 8
    try:
        c8t1 = courtReservationForm.objects.get(courtDate = date2,courtNumber=8, courtTime = "8:00 - 9:30")
    except courtReservationForm.DoesNotExist:
        c8t1 = None
    try:
        c8t2 = courtReservationForm.objects.get(courtDate = date2,courtNumber=8, courtTime = "9:30 - 11:00")
    except courtReservationForm.DoesNotExist:
        c8t2 = None
    try:
        c8t3 = courtReservationForm.objects.get(courtDate = date2,courtNumber=8, courtTime = "11:00 - 12:30")
    except courtReservationForm.DoesNotExist:
        c8t3 = None
    try:
        c8t4 = courtReservationForm.objects.get(courtDate = date2,courtNumber=8, courtTime = "12:30 - 2:00")
    except courtReservationForm.DoesNotExist:
        c8t4 = None
    try:
        c8t5 = courtReservationForm.objects.get(courtDate = date2,courtNumber=8, courtTime = "2:00 - 3:30")
    except courtReservationForm.DoesNotExist:
        c8t5 = None
    try:
        c8t6 = courtReservationForm.objects.get(courtDate = date2,courtNumber=8, courtTime = "3:30 - 5:00")
    except courtReservationForm.DoesNotExist:
        c8t6 = None

    #court 9
    try:
        c9t1 = courtReservationForm.objects.get(courtDate = date2,courtNumber=9, courtTime = "8:00 - 9:30")
    except courtReservationForm.DoesNotExist:
        c9t1 = None
    try:
        c9t2 = courtReservationForm.objects.get(courtDate = date2,courtNumber=9, courtTime = "9:30 - 11:00")
    except courtReservationForm.DoesNotExist:
        c9t2 = None
    try:
        c9t3 = courtReservationForm.objects.get(courtDate = date2,courtNumber=9, courtTime = "11:00 - 12:30")
    except courtReservationForm.DoesNotExist:
        c9t3 = None
    try:
        c9t4 = courtReservationForm.objects.get(courtDate = date2,courtNumber=9, courtTime = "12:30 - 2:00")
    except courtReservationForm.DoesNotExist:
        c9t4 = None
    try:
        c9t5 = courtReservationForm.objects.get(courtDate = date2,courtNumber=9, courtTime = "2:00 - 3:30")
    except courtReservationForm.DoesNotExist:
        c9t5 = None
    try:
        c9t6 = courtReservationForm.objects.get(courtDate = date2,courtNumber=9, courtTime = "3:30 - 5:00")
    except courtReservationForm.DoesNotExist:
        c9t6 = None

    #court 10
    try:
        c10t1 = courtReservationForm.objects.get(courtDate = date2,courtNumber=10, courtTime = "8:00 - 9:30")
    except courtReservationForm.DoesNotExist:
        c10t1 = None
    try:
        c10t2 = courtReservationForm.objects.get(courtDate = date2,courtNumber=10, courtTime = "9:30 - 11:00")
    except courtReservationForm.DoesNotExist:
        c10t2 = None
    try:
        c10t3 = courtReservationForm.objects.get(courtDate = date2,courtNumber=10, courtTime = "11:00 - 12:30")
    except courtReservationForm.DoesNotExist:
        c10t3 = None
    try:
        c10t4 = courtReservationForm.objects.get(courtDate = date2,courtNumber=10, courtTime = "12:30 - 2:00")
    except courtReservationForm.DoesNotExist:
        c10t4 = None
    try:
        c10t5 = courtReservationForm.objects.get(courtDate = date2,courtNumber=10, courtTime = "2:00 - 3:30")
    except courtReservationForm.DoesNotExist:
        c10t5 = None
    try:
        c10t6 = courtReservationForm.objects.get(courtDate = date2,courtNumber=10, courtTime = "3:30 - 5:00")
    except courtReservationForm.DoesNotExist:
        c10t6 = None

    #court 11
    try:
        c11t1 = courtReservationForm.objects.get(courtDate = date2,courtNumber=11, courtTime = "8:00 - 9:30")
    except courtReservationForm.DoesNotExist:
        c11t1 = None
    try:
        c11t2 = courtReservationForm.objects.get(courtDate = date2,courtNumber=11, courtTime = "9:30 - 11:00")
    except courtReservationForm.DoesNotExist:
        c11t2 = None
    try:
        c11t3 = courtReservationForm.objects.get(courtDate = date2,courtNumber=11, courtTime = "11:00 - 12:30")
    except courtReservationForm.DoesNotExist:
        c11t3 = None
    try:
        c11t4 = courtReservationForm.objects.get(courtDate = date2,courtNumber=11, courtTime = "12:30 - 2:00")
    except courtReservationForm.DoesNotExist:
        c11t4 = None
    try:
        c11t5 = courtReservationForm.objects.get(courtDate = date2,courtNumber=11, courtTime = "2:00 - 3:30")
    except courtReservationForm.DoesNotExist:
        c11t5 = None
    try:
        c11t6 = courtReservationForm.objects.get(courtDate = date2,courtNumber=11, courtTime = "3:30 - 5:00")
    except courtReservationForm.DoesNotExist:
        c11t6 = None

    #court 12
    try:
        c12t1 = courtReservationForm.objects.get(courtDate = date2,courtNumber=12, courtTime = "8:00 - 9:30")
    except courtReservationForm.DoesNotExist:
        c12t1 = None
    try:
        c12t2 = courtReservationForm.objects.get(courtDate = date2,courtNumber=12, courtTime = "9:30 - 11:00")
    except courtReservationForm.DoesNotExist:
        c12t2 = None
    try:
        c12t3 = courtReservationForm.objects.get(courtDate = date2,courtNumber=12, courtTime = "11:00 - 12:30")
    except courtReservationForm.DoesNotExist:
        c12t3 = None
    try:
        c12t4 = courtReservationForm.objects.get(courtDate = date2,courtNumber=12, courtTime = "12:30 - 2:00")
    except courtReservationForm.DoesNotExist:
        c12t4 = None
    try:
        c12t5 = courtReservationForm.objects.get(courtDate = date2,courtNumber=12, courtTime = "2:00 - 3:30")
    except courtReservationForm.DoesNotExist:
        c12t5 = None
    try:
        c12t6 = courtReservationForm.objects.get(courtDate = date2,courtNumber=12, courtTime = "3:30 - 5:00")
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
               'c12t1' :c12t1, 'c12t2' : c12t2, 'c12t3' : c12t3, 'c12t4' :c12t4, 'c12t5' : c12t5, 'c12t6' : c12t6,
               'date1' :date1, 'date2':date2, 'date3':date3, 'date4':date4, 'date5':date5, 'date6':date6, 'date7':date7,
               'date1Disp':date1Disp, 'date2Disp':date2Disp,'date3Disp':date3Disp,'date4Disp':date4Disp,
               'date5Disp':date5Disp,'date6Disp':date6Disp,'date7Disp':date7Disp
               }
    return render(request, 'courts/menu2.html',context)

def menu3(request):
     
    #dates
    date1 = datetime.now()
    date2 = (datetime.now()+timedelta(1))
    date3 = (datetime.now()+timedelta(2))
    date4 = (datetime.now()+timedelta(3))
    date5 = (datetime.now()+timedelta(4))
    date6 = (datetime.now()+timedelta(5))
    date7 = (datetime.now()+timedelta(6))

    date1Disp = datetime.now().strftime("%b. %d, %Y")
    date2Disp = (datetime.now()+timedelta(1)).strftime("%b. %d, %Y")
    date3Disp = (datetime.now()+timedelta(2)).strftime("%b. %d, %Y")
    date4Disp = (datetime.now()+timedelta(3)).strftime("%b. %d, %Y")
    date5Disp = (datetime.now()+timedelta(4)).strftime("%b. %d, %Y")
    date6Disp = (datetime.now()+timedelta(5)).strftime("%b. %d, %Y")
    date7Disp = (datetime.now()+timedelta(6)).strftime("%b. %d, %Y")

    #court 1
    try:
        c1t1 = courtReservationForm.objects.get(courtDate = date3, courtNumber=1, courtTime = "8:00 - 9:30")
    except courtReservationForm.DoesNotExist:
        c1t1 = None
    try:
        c1t2 = courtReservationForm.objects.get(courtDate = date3,courtNumber=1, courtTime = "9:30 - 11:00")
    except courtReservationForm.DoesNotExist:
        c1t2 = None
    try:
        c1t3 = courtReservationForm.objects.get(courtDate = date3,courtNumber=1, courtTime = "11:00 - 12:30")
    except courtReservationForm.DoesNotExist:
        c1t3 = None
    try:
        c1t4 = courtReservationForm.objects.get(courtDate = date3,courtNumber=1, courtTime = "12:30 - 2:00")
    except courtReservationForm.DoesNotExist:
        c1t4 = None
    try:
        c1t5 = courtReservationForm.objects.get(courtDate = date3,courtNumber=1, courtTime = "2:00 - 3:30")
    except courtReservationForm.DoesNotExist:
        c1t5 = None
    try:
        c1t6 = courtReservationForm.objects.get(courtDate = date3,courtNumber=1, courtTime = "3:30 - 5:00")
    except courtReservationForm.DoesNotExist:
        c1t6 = None

    #court 2
    try:
        c2t1 = courtReservationForm.objects.get(courtDate = date3,courtNumber=2, courtTime = "8:00 - 9:30")
    except courtReservationForm.DoesNotExist:
        c2t1 = None
    try:
        c2t2 = courtReservationForm.objects.get(courtDate = date3,courtNumber=2, courtTime = "9:30 - 11:00")
    except courtReservationForm.DoesNotExist:
        c2t2 = None
    try:
        c2t3 = courtReservationForm.objects.get(courtDate = date3,courtNumber=2, courtTime = "11:00 - 12:30")
    except courtReservationForm.DoesNotExist:
        c2t3 = None
    try:
        c2t4 = courtReservationForm.objects.get(courtDate = date3,courtNumber=2, courtTime = "12:30 - 2:00")
    except courtReservationForm.DoesNotExist:
        c2t4 = None
    try:
        c2t5 = courtReservationForm.objects.get(courtDate = date3,courtNumber=2, courtTime = "2:00 - 3:30")
    except courtReservationForm.DoesNotExist:
        c2t5 = None
    try:
        c2t6 = courtReservationForm.objects.get(courtDate = date3,courtNumber=2, courtTime = "3:30 - 5:00")
    except courtReservationForm.DoesNotExist:
        c2t6 = None

    #court 3
    try:
        c3t1 = courtReservationForm.objects.get(courtDate = date3,courtNumber=3, courtTime = "8:00 - 9:30")
    except courtReservationForm.DoesNotExist:
        c3t1 = None
    try:
        c3t2 = courtReservationForm.objects.get(courtDate = date3,courtNumber=3, courtTime = "9:30 - 11:00")
    except courtReservationForm.DoesNotExist:
        c3t2 = None
    try:
        c3t3 = courtReservationForm.objects.get(courtDate = date3,courtNumber=3, courtTime = "11:00 - 12:30")
    except courtReservationForm.DoesNotExist:
        c3t3 = None
    try:
        c3t4 = courtReservationForm.objects.get(courtDate = date3,courtNumber=3, courtTime = "12:30 - 2:00")
    except courtReservationForm.DoesNotExist:
        c3t4 = None
    try:
        c3t5 = courtReservationForm.objects.get(courtDate = date3,courtNumber=3, courtTime = "2:00 - 3:30")
    except courtReservationForm.DoesNotExist:
        c3t5 = None
    try:
        c3t6 = courtReservationForm.objects.get(courtDate = date3,courtNumber=3, courtTime = "3:30 - 5:00")
    except courtReservationForm.DoesNotExist:
        c3t6 = None
    
    #court 4
    try:
        c4t1 = courtReservationForm.objects.get(courtDate = date3,courtNumber=4, courtTime = "8:00 - 9:30")
    except courtReservationForm.DoesNotExist:
        c4t1 = None
    try:
        c4t2 = courtReservationForm.objects.get(courtDate = date3,courtNumber=4, courtTime = "9:30 - 11:00")
    except courtReservationForm.DoesNotExist:
        c4t2 = None
    try:
        c4t3 = courtReservationForm.objects.get(courtDate = date3,courtNumber=4, courtTime = "11:00 - 12:30")
    except courtReservationForm.DoesNotExist:
        c4t3 = None
    try:
        c4t4 = courtReservationForm.objects.get(courtDate = date3,courtNumber=4, courtTime = "12:30 - 2:00")
    except courtReservationForm.DoesNotExist:
        c4t4 = None
    try:
        c4t5 = courtReservationForm.objects.get(courtDate = date3,courtNumber=4, courtTime = "2:00 - 3:30")
    except courtReservationForm.DoesNotExist:
        c4t5 = None
    try:
        c4t6 = courtReservationForm.objects.get(courtDate = date3,courtNumber=4, courtTime = "3:30 - 5:00")
    except courtReservationForm.DoesNotExist:
        c4t6 = None

    #court 5
    try:
        c5t1 = courtReservationForm.objects.get(courtDate = date3,courtNumber=5, courtTime = "8:00 - 9:30")
    except courtReservationForm.DoesNotExist:
        c5t1 = None
    try:
        c5t2 = courtReservationForm.objects.get(courtDate = date3,courtNumber=5, courtTime = "9:30 - 11:00")
    except courtReservationForm.DoesNotExist:
        c5t2 = None
    try:
        c5t3 = courtReservationForm.objects.get(courtDate = date3,courtNumber=5, courtTime = "11:00 - 12:30")
    except courtReservationForm.DoesNotExist:
        c5t3 = None
    try:
        c5t4 = courtReservationForm.objects.get(courtDate = date3,courtNumber=5, courtTime = "12:30 - 2:00")
    except courtReservationForm.DoesNotExist:
        c5t4 = None
    try:
        c5t5 = courtReservationForm.objects.get(courtDate = date3,courtNumber=5, courtTime = "2:00 - 3:30")
    except courtReservationForm.DoesNotExist:
        c5t5 = None
    try:
        c5t6 = courtReservationForm.objects.get(courtDate = date3,courtNumber=5, courtTime = "3:30 - 5:00")
    except courtReservationForm.DoesNotExist:
        c5t6 = None

    #court 6
    try:
        c6t1 = courtReservationForm.objects.get(courtDate = date3,courtNumber=6, courtTime = "8:00 - 9:30")
    except courtReservationForm.DoesNotExist:
        c6t1 = None
    try:
        c6t2 = courtReservationForm.objects.get(courtDate = date3,courtNumber=6, courtTime = "9:30 - 11:00")
    except courtReservationForm.DoesNotExist:
        c6t2 = None
    try:
        c6t3 = courtReservationForm.objects.get(courtDate = date3,courtNumber=6, courtTime = "11:00 - 12:30")
    except courtReservationForm.DoesNotExist:
        c6t3 = None
    try:
        c6t4 = courtReservationForm.objects.get(courtDate = date3,courtNumber=6, courtTime = "12:30 - 2:00")
    except courtReservationForm.DoesNotExist:
        c6t4 = None
    try:
        c6t5 = courtReservationForm.objects.get(courtDate = date3,courtNumber=6, courtTime = "2:00 - 3:30")
    except courtReservationForm.DoesNotExist:
        c6t5 = None
    try:
        c6t6 = courtReservationForm.objects.get(courtDate = date3,courtNumber=6, courtTime = "3:30 - 5:00")
    except courtReservationForm.DoesNotExist:
        c6t6 = None
    
    #court 7
    try:
        c7t1 = courtReservationForm.objects.get(courtDate = date3,courtNumber=7, courtTime = "8:00 - 9:30")
    except courtReservationForm.DoesNotExist:
        c7t1 = None
    try:
        c7t2 = courtReservationForm.objects.get(courtDate = date3,courtNumber=7, courtTime = "9:30 - 11:00")
    except courtReservationForm.DoesNotExist:
        c7t2 = None
    try:
        c7t3 = courtReservationForm.objects.get(courtDate = date3,courtNumber=7, courtTime = "11:00 - 12:30")
    except courtReservationForm.DoesNotExist:
        c7t3 = None
    try:
        c7t4 = courtReservationForm.objects.get(courtDate = date3,courtNumber=7, courtTime = "12:30 - 2:00")
    except courtReservationForm.DoesNotExist:
        c7t4 = None
    try:
        c7t5 = courtReservationForm.objects.get(courtDate = date3,courtNumber=7, courtTime = "2:00 - 3:30")
    except courtReservationForm.DoesNotExist:
        c7t5 = None
    try:
        c7t6 = courtReservationForm.objects.get(courtDate = date3,courtNumber=7, courtTime = "3:30 - 5:00")
    except courtReservationForm.DoesNotExist:
        c7t6 = None
    
    #court 8
    try:
        c8t1 = courtReservationForm.objects.get(courtDate = date3,courtNumber=8, courtTime = "8:00 - 9:30")
    except courtReservationForm.DoesNotExist:
        c8t1 = None
    try:
        c8t2 = courtReservationForm.objects.get(courtDate = date3,courtNumber=8, courtTime = "9:30 - 11:00")
    except courtReservationForm.DoesNotExist:
        c8t2 = None
    try:
        c8t3 = courtReservationForm.objects.get(courtDate = date3,courtNumber=8, courtTime = "11:00 - 12:30")
    except courtReservationForm.DoesNotExist:
        c8t3 = None
    try:
        c8t4 = courtReservationForm.objects.get(courtDate = date3,courtNumber=8, courtTime = "12:30 - 2:00")
    except courtReservationForm.DoesNotExist:
        c8t4 = None
    try:
        c8t5 = courtReservationForm.objects.get(courtDate = date3,courtNumber=8, courtTime = "2:00 - 3:30")
    except courtReservationForm.DoesNotExist:
        c8t5 = None
    try:
        c8t6 = courtReservationForm.objects.get(courtDate = date3,courtNumber=8, courtTime = "3:30 - 5:00")
    except courtReservationForm.DoesNotExist:
        c8t6 = None

    #court 9
    try:
        c9t1 = courtReservationForm.objects.get(courtDate = date3,courtNumber=9, courtTime = "8:00 - 9:30")
    except courtReservationForm.DoesNotExist:
        c9t1 = None
    try:
        c9t2 = courtReservationForm.objects.get(courtDate = date3,courtNumber=9, courtTime = "9:30 - 11:00")
    except courtReservationForm.DoesNotExist:
        c9t2 = None
    try:
        c9t3 = courtReservationForm.objects.get(courtDate = date3,courtNumber=9, courtTime = "11:00 - 12:30")
    except courtReservationForm.DoesNotExist:
        c9t3 = None
    try:
        c9t4 = courtReservationForm.objects.get(courtDate = date3,courtNumber=9, courtTime = "12:30 - 2:00")
    except courtReservationForm.DoesNotExist:
        c9t4 = None
    try:
        c9t5 = courtReservationForm.objects.get(courtDate = date3,courtNumber=9, courtTime = "2:00 - 3:30")
    except courtReservationForm.DoesNotExist:
        c9t5 = None
    try:
        c9t6 = courtReservationForm.objects.get(courtDate = date3,courtNumber=9, courtTime = "3:30 - 5:00")
    except courtReservationForm.DoesNotExist:
        c9t6 = None

    #court 10
    try:
        c10t1 = courtReservationForm.objects.get(courtDate = date3,courtNumber=10, courtTime = "8:00 - 9:30")
    except courtReservationForm.DoesNotExist:
        c10t1 = None
    try:
        c10t2 = courtReservationForm.objects.get(courtDate = date3,courtNumber=10, courtTime = "9:30 - 11:00")
    except courtReservationForm.DoesNotExist:
        c10t2 = None
    try:
        c10t3 = courtReservationForm.objects.get(courtNumber=10, courtTime = "11:00 - 12:30")
    except courtReservationForm.DoesNotExist:
        c10t3 = None
    try:
        c10t4 = courtReservationForm.objects.get(courtDate = date3,courtNumber=10, courtTime = "12:30 - 2:00")
    except courtReservationForm.DoesNotExist:
        c10t4 = None
    try:
        c10t5 = courtReservationForm.objects.get(courtDate = date3,courtNumber=10, courtTime = "2:00 - 3:30")
    except courtReservationForm.DoesNotExist:
        c10t5 = None
    try:
        c10t6 = courtReservationForm.objects.get(courtDate = date3,courtNumber=10, courtTime = "3:30 - 5:00")
    except courtReservationForm.DoesNotExist:
        c10t6 = None

    #court 11
    try:
        c11t1 = courtReservationForm.objects.get(courtDate = date3,courtNumber=11, courtTime = "8:00 - 9:30")
    except courtReservationForm.DoesNotExist:
        c11t1 = None
    try:
        c11t2 = courtReservationForm.objects.get(courtDate = date3,courtNumber=11, courtTime = "9:30 - 11:00")
    except courtReservationForm.DoesNotExist:
        c11t2 = None
    try:
        c11t3 = courtReservationForm.objects.get(courtDate = date3,courtNumber=11, courtTime = "11:00 - 12:30")
    except courtReservationForm.DoesNotExist:
        c11t3 = None
    try:
        c11t4 = courtReservationForm.objects.get(courtDate = date3,courtNumber=11, courtTime = "12:30 - 2:00")
    except courtReservationForm.DoesNotExist:
        c11t4 = None
    try:
        c11t5 = courtReservationForm.objects.get(courtDate = date3,courtNumber=11, courtTime = "2:00 - 3:30")
    except courtReservationForm.DoesNotExist:
        c11t5 = None
    try:
        c11t6 = courtReservationForm.objects.get(courtDate = date3,courtNumber=11, courtTime = "3:30 - 5:00")
    except courtReservationForm.DoesNotExist:
        c11t6 = None

    #court 12
    try:
        c12t1 = courtReservationForm.objects.get(courtDate = date3,courtNumber=12, courtTime = "8:00 - 9:30")
    except courtReservationForm.DoesNotExist:
        c12t1 = None
    try:
        c12t2 = courtReservationForm.objects.get(courtDate = date3,courtNumber=12, courtTime = "9:30 - 11:00")
    except courtReservationForm.DoesNotExist:
        c12t2 = None
    try:
        c12t3 = courtReservationForm.objects.get(courtDate = date3,courtNumber=12, courtTime = "11:00 - 12:30")
    except courtReservationForm.DoesNotExist:
        c12t3 = None
    try:
        c12t4 = courtReservationForm.objects.get(courtDate = date3,courtNumber=12, courtTime = "12:30 - 2:00")
    except courtReservationForm.DoesNotExist:
        c12t4 = None
    try:
        c12t5 = courtReservationForm.objects.get(courtDate = date3,courtNumber=12, courtTime = "2:00 - 3:30")
    except courtReservationForm.DoesNotExist:
        c12t5 = None
    try:
        c12t6 = courtReservationForm.objects.get(courtDate = date3,courtNumber=12, courtTime = "3:30 - 5:00")
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
               'c12t1' :c12t1, 'c12t2' : c12t2, 'c12t3' : c12t3, 'c12t4' :c12t4, 'c12t5' : c12t5, 'c12t6' : c12t6,
               'date1' :date1, 'date2':date2, 'date3':date3, 'date4':date4, 'date5':date5, 'date6':date6, 'date7':date7,
               'date1Disp':date1Disp, 'date2Disp':date2Disp,'date3Disp':date3Disp,'date4Disp':date4Disp,
               'date5Disp':date5Disp,'date6Disp':date6Disp,'date7Disp':date7Disp
               }
    return render(request, 'courts/menu3.html',context)

def menu4(request):
    #dates
    date1 = datetime.now()
    date2 = (datetime.now()+timedelta(1))
    date3 = (datetime.now()+timedelta(2))
    date4 = (datetime.now()+timedelta(3))
    date5 = (datetime.now()+timedelta(4))
    date6 = (datetime.now()+timedelta(5))
    date7 = (datetime.now()+timedelta(6))

    date1Disp = datetime.now().strftime("%b. %d, %Y")
    date2Disp = (datetime.now()+timedelta(1)).strftime("%b. %d, %Y")
    date3Disp = (datetime.now()+timedelta(2)).strftime("%b. %d, %Y")
    date4Disp = (datetime.now()+timedelta(3)).strftime("%b. %d, %Y")
    date5Disp = (datetime.now()+timedelta(4)).strftime("%b. %d, %Y")
    date6Disp = (datetime.now()+timedelta(5)).strftime("%b. %d, %Y")
    date7Disp = (datetime.now()+timedelta(6)).strftime("%b. %d, %Y")

    #court 1
    try:
        c1t1 = courtReservationForm.objects.get(courtDate = date4,courtNumber=1, courtTime = "8:00 - 9:30")
    except courtReservationForm.DoesNotExist:
        c1t1 = None
    try:
        c1t2 = courtReservationForm.objects.get(courtDate = date4,courtNumber=1, courtTime = "9:30 - 11:00")
    except courtReservationForm.DoesNotExist:
        c1t2 = None
    try:
        c1t3 = courtReservationForm.objects.get(courtDate = date4,courtNumber=1, courtTime = "11:00 - 12:30")
    except courtReservationForm.DoesNotExist:
        c1t3 = None
    try:
        c1t4 = courtReservationForm.objects.get(courtDate = date4,courtNumber=1, courtTime = "12:30 - 2:00")
    except courtReservationForm.DoesNotExist:
        c1t4 = None
    try:
        c1t5 = courtReservationForm.objects.get(courtDate = date4,courtNumber=1, courtTime = "2:00 - 3:30")
    except courtReservationForm.DoesNotExist:
        c1t5 = None
    try:
        c1t6 = courtReservationForm.objects.get(courtDate = date4,courtNumber=1, courtTime = "3:30 - 5:00")
    except courtReservationForm.DoesNotExist:
        c1t6 = None

    #court 2
    try:
        c2t1 = courtReservationForm.objects.get(courtDate = date4,courtNumber=2, courtTime = "8:00 - 9:30")
    except courtReservationForm.DoesNotExist:
        c2t1 = None
    try:
        c2t2 = courtReservationForm.objects.get(courtDate = date4,courtNumber=2, courtTime = "9:30 - 11:00")
    except courtReservationForm.DoesNotExist:
        c2t2 = None
    try:
        c2t3 = courtReservationForm.objects.get(courtDate = date4,courtNumber=2, courtTime = "11:00 - 12:30")
    except courtReservationForm.DoesNotExist:
        c2t3 = None
    try:
        c2t4 = courtReservationForm.objects.get(courtDate = date4,courtNumber=2, courtTime = "12:30 - 2:00")
    except courtReservationForm.DoesNotExist:
        c2t4 = None
    try:
        c2t5 = courtReservationForm.objects.get(courtDate = date4,courtNumber=2, courtTime = "2:00 - 3:30")
    except courtReservationForm.DoesNotExist:
        c2t5 = None
    try:
        c2t6 = courtReservationForm.objects.get(courtDate = date4,courtNumber=2, courtTime = "3:30 - 5:00")
    except courtReservationForm.DoesNotExist:
        c2t6 = None

    #court 3
    try:
        c3t1 = courtReservationForm.objects.get(courtDate = date4,courtNumber=3, courtTime = "8:00 - 9:30")
    except courtReservationForm.DoesNotExist:
        c3t1 = None
    try:
        c3t2 = courtReservationForm.objects.get(courtDate = date4,courtNumber=3, courtTime = "9:30 - 11:00")
    except courtReservationForm.DoesNotExist:
        c3t2 = None
    try:
        c3t3 = courtReservationForm.objects.get(courtDate = date4,courtNumber=3, courtTime = "11:00 - 12:30")
    except courtReservationForm.DoesNotExist:
        c3t3 = None
    try:
        c3t4 = courtReservationForm.objects.get(courtDate = date4,courtNumber=3, courtTime = "12:30 - 2:00")
    except courtReservationForm.DoesNotExist:
        c3t4 = None
    try:
        c3t5 = courtReservationForm.objects.get(courtDate = date4,courtNumber=3, courtTime = "2:00 - 3:30")
    except courtReservationForm.DoesNotExist:
        c3t5 = None
    try:
        c3t6 = courtReservationForm.objects.get(courtDate = date4,courtNumber=3, courtTime = "3:30 - 5:00")
    except courtReservationForm.DoesNotExist:
        c3t6 = None
    
    #court 4
    try:
        c4t1 = courtReservationForm.objects.get(courtDate = date4,courtNumber=4, courtTime = "8:00 - 9:30")
    except courtReservationForm.DoesNotExist:
        c4t1 = None
    try:
        c4t2 = courtReservationForm.objects.get(courtDate = date4,courtNumber=4, courtTime = "9:30 - 11:00")
    except courtReservationForm.DoesNotExist:
        c4t2 = None
    try:
        c4t3 = courtReservationForm.objects.get(courtDate = date4,courtNumber=4, courtTime = "11:00 - 12:30")
    except courtReservationForm.DoesNotExist:
        c4t3 = None
    try:
        c4t4 = courtReservationForm.objects.get(courtDate = date4,courtNumber=4, courtTime = "12:30 - 2:00")
    except courtReservationForm.DoesNotExist:
        c4t4 = None
    try:
        c4t5 = courtReservationForm.objects.get(courtDate = date4,courtNumber=4, courtTime = "2:00 - 3:30")
    except courtReservationForm.DoesNotExist:
        c4t5 = None
    try:
        c4t6 = courtReservationForm.objects.get(courtDate = date4,courtNumber=4, courtTime = "3:30 - 5:00")
    except courtReservationForm.DoesNotExist:
        c4t6 = None

    #court 5
    try:
        c5t1 = courtReservationForm.objects.get(courtDate = date4,courtNumber=5, courtTime = "8:00 - 9:30")
    except courtReservationForm.DoesNotExist:
        c5t1 = None
    try:
        c5t2 = courtReservationForm.objects.get(courtDate = date4,courtNumber=5, courtTime = "9:30 - 11:00")
    except courtReservationForm.DoesNotExist:
        c5t2 = None
    try:
        c5t3 = courtReservationForm.objects.get(courtDate = date4,courtNumber=5, courtTime = "11:00 - 12:30")
    except courtReservationForm.DoesNotExist:
        c5t3 = None
    try:
        c5t4 = courtReservationForm.objects.get(courtDate = date4,courtNumber=5, courtTime = "12:30 - 2:00")
    except courtReservationForm.DoesNotExist:
        c5t4 = None
    try:
        c5t5 = courtReservationForm.objects.get(courtDate = date4,courtNumber=5, courtTime = "2:00 - 3:30")
    except courtReservationForm.DoesNotExist:
        c5t5 = None
    try:
        c5t6 = courtReservationForm.objects.get(courtDate = date4,courtNumber=5, courtTime = "3:30 - 5:00")
    except courtReservationForm.DoesNotExist:
        c5t6 = None

    #court 6
    try:
        c6t1 = courtReservationForm.objects.get(courtDate = date4,courtNumber=6, courtTime = "8:00 - 9:30")
    except courtReservationForm.DoesNotExist:
        c6t1 = None
    try:
        c6t2 = courtReservationForm.objects.get(courtDate = date4,courtNumber=6, courtTime = "9:30 - 11:00")
    except courtReservationForm.DoesNotExist:
        c6t2 = None
    try:
        c6t3 = courtReservationForm.objects.get(courtDate = date4,courtNumber=6, courtTime = "11:00 - 12:30")
    except courtReservationForm.DoesNotExist:
        c6t3 = None
    try:
        c6t4 = courtReservationForm.objects.get(courtDate = date4,courtNumber=6, courtTime = "12:30 - 2:00")
    except courtReservationForm.DoesNotExist:
        c6t4 = None
    try:
        c6t5 = courtReservationForm.objects.get(courtDate = date4,courtNumber=6, courtTime = "2:00 - 3:30")
    except courtReservationForm.DoesNotExist:
        c6t5 = None
    try:
        c6t6 = courtReservationForm.objects.get(courtDate = date4,courtNumber=6, courtTime = "3:30 - 5:00")
    except courtReservationForm.DoesNotExist:
        c6t6 = None
    
    #court 7
    try:
        c7t1 = courtReservationForm.objects.get(courtDate = date4,courtNumber=7, courtTime = "8:00 - 9:30")
    except courtReservationForm.DoesNotExist:
        c7t1 = None
    try:
        c7t2 = courtReservationForm.objects.get(courtDate = date4,courtNumber=7, courtTime = "9:30 - 11:00")
    except courtReservationForm.DoesNotExist:
        c7t2 = None
    try:
        c7t3 = courtReservationForm.objects.get(courtDate = date4,courtNumber=7, courtTime = "11:00 - 12:30")
    except courtReservationForm.DoesNotExist:
        c7t3 = None
    try:
        c7t4 = courtReservationForm.objects.get(courtDate = date4,courtNumber=7, courtTime = "12:30 - 2:00")
    except courtReservationForm.DoesNotExist:
        c7t4 = None
    try:
        c7t5 = courtReservationForm.objects.get(courtDate = date4,courtNumber=7, courtTime = "2:00 - 3:30")
    except courtReservationForm.DoesNotExist:
        c7t5 = None
    try:
        c7t6 = courtReservationForm.objects.get(courtDate = date4,courtNumber=7, courtTime = "3:30 - 5:00")
    except courtReservationForm.DoesNotExist:
        c7t6 = None
    
    #court 8
    try:
        c8t1 = courtReservationForm.objects.get(courtDate = date4,courtNumber=8, courtTime = "8:00 - 9:30")
    except courtReservationForm.DoesNotExist:
        c8t1 = None
    try:
        c8t2 = courtReservationForm.objects.get(courtDate = date4,courtNumber=8, courtTime = "9:30 - 11:00")
    except courtReservationForm.DoesNotExist:
        c8t2 = None
    try:
        c8t3 = courtReservationForm.objects.get(courtDate = date4,courtNumber=8, courtTime = "11:00 - 12:30")
    except courtReservationForm.DoesNotExist:
        c8t3 = None
    try:
        c8t4 = courtReservationForm.objects.get(courtDate = date4,courtNumber=8, courtTime = "12:30 - 2:00")
    except courtReservationForm.DoesNotExist:
        c8t4 = None
    try:
        c8t5 = courtReservationForm.objects.get(courtDate = date4,courtNumber=8, courtTime = "2:00 - 3:30")
    except courtReservationForm.DoesNotExist:
        c8t5 = None
    try:
        c8t6 = courtReservationForm.objects.get(courtDate = date4,courtNumber=8, courtTime = "3:30 - 5:00")
    except courtReservationForm.DoesNotExist:
        c8t6 = None

    #court 9
    try:
        c9t1 = courtReservationForm.objects.get(courtDate = date4,courtNumber=9, courtTime = "8:00 - 9:30")
    except courtReservationForm.DoesNotExist:
        c9t1 = None
    try:
        c9t2 = courtReservationForm.objects.get(courtDate = date4,courtNumber=9, courtTime = "9:30 - 11:00")
    except courtReservationForm.DoesNotExist:
        c9t2 = None
    try:
        c9t3 = courtReservationForm.objects.get(courtDate = date4,courtNumber=9, courtTime = "11:00 - 12:30")
    except courtReservationForm.DoesNotExist:
        c9t3 = None
    try:
        c9t4 = courtReservationForm.objects.get(courtDate = date4,courtNumber=9, courtTime = "12:30 - 2:00")
    except courtReservationForm.DoesNotExist:
        c9t4 = None
    try:
        c9t5 = courtReservationForm.objects.get(courtDate = date4,courtNumber=9, courtTime = "2:00 - 3:30")
    except courtReservationForm.DoesNotExist:
        c9t5 = None
    try:
        c9t6 = courtReservationForm.objects.get(courtDate = date4,courtNumber=9, courtTime = "3:30 - 5:00")
    except courtReservationForm.DoesNotExist:
        c9t6 = None

    #court 10
    try:
        c10t1 = courtReservationForm.objects.get(courtDate = date4,courtNumber=10, courtTime = "8:00 - 9:30")
    except courtReservationForm.DoesNotExist:
        c10t1 = None
    try:
        c10t2 = courtReservationForm.objects.get(courtDate = date4,courtNumber=10, courtTime = "9:30 - 11:00")
    except courtReservationForm.DoesNotExist:
        c10t2 = None
    try:
        c10t3 = courtReservationForm.objects.get(courtDate = date4,courtNumber=10, courtTime = "11:00 - 12:30")
    except courtReservationForm.DoesNotExist:
        c10t3 = None
    try:
        c10t4 = courtReservationForm.objects.get(courtDate = date4,courtNumber=10, courtTime = "12:30 - 2:00")
    except courtReservationForm.DoesNotExist:
        c10t4 = None
    try:
        c10t5 = courtReservationForm.objects.get(courtDate = date4,courtNumber=10, courtTime = "2:00 - 3:30")
    except courtReservationForm.DoesNotExist:
        c10t5 = None
    try:
        c10t6 = courtReservationForm.objects.get(courtDate = date4,courtNumber=10, courtTime = "3:30 - 5:00")
    except courtReservationForm.DoesNotExist:
        c10t6 = None

    #court 11
    try:
        c11t1 = courtReservationForm.objects.get(courtDate = date4,courtNumber=11, courtTime = "8:00 - 9:30")
    except courtReservationForm.DoesNotExist:
        c11t1 = None
    try:
        c11t2 = courtReservationForm.objects.get(courtDate = date4,courtNumber=11, courtTime = "9:30 - 11:00")
    except courtReservationForm.DoesNotExist:
        c11t2 = None
    try:
        c11t3 = courtReservationForm.objects.get(courtDate = date4,courtNumber=11, courtTime = "11:00 - 12:30")
    except courtReservationForm.DoesNotExist:
        c11t3 = None
    try:
        c11t4 = courtReservationForm.objects.get(courtDate = date4,courtNumber=11, courtTime = "12:30 - 2:00")
    except courtReservationForm.DoesNotExist:
        c11t4 = None
    try:
        c11t5 = courtReservationForm.objects.get(courtDate = date4,courtNumber=11, courtTime = "2:00 - 3:30")
    except courtReservationForm.DoesNotExist:
        c11t5 = None
    try:
        c11t6 = courtReservationForm.objects.get(courtDate = date4,courtNumber=11, courtTime = "3:30 - 5:00")
    except courtReservationForm.DoesNotExist:
        c11t6 = None

    #court 12
    try:
        c12t1 = courtReservationForm.objects.get(courtDate = date4,courtNumber=12, courtTime = "8:00 - 9:30")
    except courtReservationForm.DoesNotExist:
        c12t1 = None
    try:
        c12t2 = courtReservationForm.objects.get(courtDate = date4,courtNumber=12, courtTime = "9:30 - 11:00")
    except courtReservationForm.DoesNotExist:
        c12t2 = None
    try:
        c12t3 = courtReservationForm.objects.get(courtDate = date4,courtNumber=12, courtTime = "11:00 - 12:30")
    except courtReservationForm.DoesNotExist:
        c12t3 = None
    try:
        c12t4 = courtReservationForm.objects.get(courtDate = date4,courtNumber=12, courtTime = "12:30 - 2:00")
    except courtReservationForm.DoesNotExist:
        c12t4 = None
    try:
        c12t5 = courtReservationForm.objects.get(courtDate = date4,courtNumber=12, courtTime = "2:00 - 3:30")
    except courtReservationForm.DoesNotExist:
        c12t5 = None
    try:
        c12t6 = courtReservationForm.objects.get(courtDate = date4,courtNumber=12, courtTime = "3:30 - 5:00")
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
               'c12t1' :c12t1, 'c12t2' : c12t2, 'c12t3' : c12t3, 'c12t4' :c12t4, 'c12t5' : c12t5, 'c12t6' : c12t6,
               'date1' :date1, 'date2':date2, 'date3':date3, 'date4':date4, 'date5':date5, 'date6':date6, 'date7':date7,
               'date1Disp':date1Disp, 'date2Disp':date2Disp,'date3Disp':date3Disp,'date4Disp':date4Disp,
               'date5Disp':date5Disp,'date6Disp':date6Disp,'date7Disp':date7Disp
               }
    return render(request, 'courts/menu4.html',context)

def menu5(request):
    #dates
    date1 = datetime.now()
    date2 = (datetime.now()+timedelta(1))
    date3 = (datetime.now()+timedelta(2))
    date4 = (datetime.now()+timedelta(3))
    date5 = (datetime.now()+timedelta(4))
    date6 = (datetime.now()+timedelta(5))
    date7 = (datetime.now()+timedelta(6))

    date1Disp = datetime.now().strftime("%b. %d, %Y")
    date2Disp = (datetime.now()+timedelta(1)).strftime("%b. %d, %Y")
    date3Disp = (datetime.now()+timedelta(2)).strftime("%b. %d, %Y")
    date4Disp = (datetime.now()+timedelta(3)).strftime("%b. %d, %Y")
    date5Disp = (datetime.now()+timedelta(4)).strftime("%b. %d, %Y")
    date6Disp = (datetime.now()+timedelta(5)).strftime("%b. %d, %Y")
    date7Disp = (datetime.now()+timedelta(6)).strftime("%b. %d, %Y")
    #court 1
    try:
        c1t1 = courtReservationForm.objects.get(courtDate = date5,courtNumber=1, courtTime = "8:00 - 9:30")
    except courtReservationForm.DoesNotExist:
        c1t1 = None
    try:
        c1t2 = courtReservationForm.objects.get(courtDate = date5,courtNumber=1, courtTime = "9:30 - 11:00")
    except courtReservationForm.DoesNotExist:
        c1t2 = None
    try:
        c1t3 = courtReservationForm.objects.get(courtDate = date5,courtNumber=1, courtTime = "11:00 - 12:30")
    except courtReservationForm.DoesNotExist:
        c1t3 = None
    try:
        c1t4 = courtReservationForm.objects.get(courtDate = date5,courtNumber=1, courtTime = "12:30 - 2:00")
    except courtReservationForm.DoesNotExist:
        c1t4 = None
    try:
        c1t5 = courtReservationForm.objects.get(courtDate = date5,courtNumber=1, courtTime = "2:00 - 3:30")
    except courtReservationForm.DoesNotExist:
        c1t5 = None
    try:
        c1t6 = courtReservationForm.objects.get(courtDate = date5,courtNumber=1, courtTime = "3:30 - 5:00")
    except courtReservationForm.DoesNotExist:
        c1t6 = None

    #court 2
    try:
        c2t1 = courtReservationForm.objects.get(courtDate = date5,courtNumber=2, courtTime = "8:00 - 9:30")
    except courtReservationForm.DoesNotExist:
        c2t1 = None
    try:
        c2t2 = courtReservationForm.objects.get(courtDate = date5,courtNumber=2, courtTime = "9:30 - 11:00")
    except courtReservationForm.DoesNotExist:
        c2t2 = None
    try:
        c2t3 = courtReservationForm.objects.get(courtDate = date5,courtNumber=2, courtTime = "11:00 - 12:30")
    except courtReservationForm.DoesNotExist:
        c2t3 = None
    try:
        c2t4 = courtReservationForm.objects.get(courtDate = date5,courtNumber=2, courtTime = "12:30 - 2:00")
    except courtReservationForm.DoesNotExist:
        c2t4 = None
    try:
        c2t5 = courtReservationForm.objects.get(courtDate = date5,courtNumber=2, courtTime = "2:00 - 3:30")
    except courtReservationForm.DoesNotExist:
        c2t5 = None
    try:
        c2t6 = courtReservationForm.objects.get(courtDate = date5,courtNumber=2, courtTime = "3:30 - 5:00")
    except courtReservationForm.DoesNotExist:
        c2t6 = None

    #court 3
    try:
        c3t1 = courtReservationForm.objects.get(courtDate = date5,courtNumber=3, courtTime = "8:00 - 9:30")
    except courtReservationForm.DoesNotExist:
        c3t1 = None
    try:
        c3t2 = courtReservationForm.objects.get(courtDate = date5,courtNumber=3, courtTime = "9:30 - 11:00")
    except courtReservationForm.DoesNotExist:
        c3t2 = None
    try:
        c3t3 = courtReservationForm.objects.get(courtDate = date5,courtNumber=3, courtTime = "11:00 - 12:30")
    except courtReservationForm.DoesNotExist:
        c3t3 = None
    try:
        c3t4 = courtReservationForm.objects.get(courtDate = date5,courtNumber=3, courtTime = "12:30 - 2:00")
    except courtReservationForm.DoesNotExist:
        c3t4 = None
    try:
        c3t5 = courtReservationForm.objects.get(courtDate = date5,courtNumber=3, courtTime = "2:00 - 3:30")
    except courtReservationForm.DoesNotExist:
        c3t5 = None
    try:
        c3t6 = courtReservationForm.objects.get(courtDate = date5,courtNumber=3, courtTime = "3:30 - 5:00")
    except courtReservationForm.DoesNotExist:
        c3t6 = None
    
    #court 4
    try:
        c4t1 = courtReservationForm.objects.get(courtDate = date5,courtNumber=4, courtTime = "8:00 - 9:30")
    except courtReservationForm.DoesNotExist:
        c4t1 = None
    try:
        c4t2 = courtReservationForm.objects.get(courtDate = date5,courtNumber=4, courtTime = "9:30 - 11:00")
    except courtReservationForm.DoesNotExist:
        c4t2 = None
    try:
        c4t3 = courtReservationForm.objects.get(courtDate = date5,courtNumber=4, courtTime = "11:00 - 12:30")
    except courtReservationForm.DoesNotExist:
        c4t3 = None
    try:
        c4t4 = courtReservationForm.objects.get(courtDate = date5,courtNumber=4, courtTime = "12:30 - 2:00")
    except courtReservationForm.DoesNotExist:
        c4t4 = None
    try:
        c4t5 = courtReservationForm.objects.get(courtDate = date5,courtNumber=4, courtTime = "2:00 - 3:30")
    except courtReservationForm.DoesNotExist:
        c4t5 = None
    try:
        c4t6 = courtReservationForm.objects.get(courtDate = date5,courtNumber=4, courtTime = "3:30 - 5:00")
    except courtReservationForm.DoesNotExist:
        c4t6 = None

    #court 5
    try:
        c5t1 = courtReservationForm.objects.get(courtDate = date5,courtNumber=5, courtTime = "8:00 - 9:30")
    except courtReservationForm.DoesNotExist:
        c5t1 = None
    try:
        c5t2 = courtReservationForm.objects.get(courtDate = date5,courtNumber=5, courtTime = "9:30 - 11:00")
    except courtReservationForm.DoesNotExist:
        c5t2 = None
    try:
        c5t3 = courtReservationForm.objects.get(courtDate = date5,courtNumber=5, courtTime = "11:00 - 12:30")
    except courtReservationForm.DoesNotExist:
        c5t3 = None
    try:
        c5t4 = courtReservationForm.objects.get(courtDate = date5,courtNumber=5, courtTime = "12:30 - 2:00")
    except courtReservationForm.DoesNotExist:
        c5t4 = None
    try:
        c5t5 = courtReservationForm.objects.get(courtDate = date5,courtNumber=5, courtTime = "2:00 - 3:30")
    except courtReservationForm.DoesNotExist:
        c5t5 = None
    try:
        c5t6 = courtReservationForm.objects.get(courtDate = date5,courtNumber=5, courtTime = "3:30 - 5:00")
    except courtReservationForm.DoesNotExist:
        c5t6 = None

    #court 6
    try:
        c6t1 = courtReservationForm.objects.get(courtDate = date5,courtNumber=6, courtTime = "8:00 - 9:30")
    except courtReservationForm.DoesNotExist:
        c6t1 = None
    try:
        c6t2 = courtReservationForm.objects.get(courtDate = date5,courtNumber=6, courtTime = "9:30 - 11:00")
    except courtReservationForm.DoesNotExist:
        c6t2 = None
    try:
        c6t3 = courtReservationForm.objects.get(courtDate = date5,courtNumber=6, courtTime = "11:00 - 12:30")
    except courtReservationForm.DoesNotExist:
        c6t3 = None
    try:
        c6t4 = courtReservationForm.objects.get(courtDate = date5,courtNumber=6, courtTime = "12:30 - 2:00")
    except courtReservationForm.DoesNotExist:
        c6t4 = None
    try:
        c6t5 = courtReservationForm.objects.get(courtDate = date5,courtNumber=6, courtTime = "2:00 - 3:30")
    except courtReservationForm.DoesNotExist:
        c6t5 = None
    try:
        c6t6 = courtReservationForm.objects.get( courtDate = date5,courtNumber=6, courtTime = "3:30 - 5:00")
    except courtReservationForm.DoesNotExist:
        c6t6 = None
    
    #court 7
    try:
        c7t1 = courtReservationForm.objects.get(courtDate = date5,courtNumber=7, courtTime = "8:00 - 9:30")
    except courtReservationForm.DoesNotExist:
        c7t1 = None
    try:
        c7t2 = courtReservationForm.objects.get(courtDate = date5,courtNumber=7, courtTime = "9:30 - 11:00")
    except courtReservationForm.DoesNotExist:
        c7t2 = None
    try:
        c7t3 = courtReservationForm.objects.get(courtDate = date5,courtNumber=7, courtTime = "11:00 - 12:30")
    except courtReservationForm.DoesNotExist:
        c7t3 = None
    try:
        c7t4 = courtReservationForm.objects.get(courtDate = date5,courtNumber=7, courtTime = "12:30 - 2:00")
    except courtReservationForm.DoesNotExist:
        c7t4 = None
    try:
        c7t5 = courtReservationForm.objects.get(courtDate = date5,courtNumber=7, courtTime = "2:00 - 3:30")
    except courtReservationForm.DoesNotExist:
        c7t5 = None
    try:
        c7t6 = courtReservationForm.objects.get(courtDate = date5,courtNumber=7, courtTime = "3:30 - 5:00")
    except courtReservationForm.DoesNotExist:
        c7t6 = None
    
    #court 8
    try:
        c8t1 = courtReservationForm.objects.get(courtDate = date5,courtNumber=8, courtTime = "8:00 - 9:30")
    except courtReservationForm.DoesNotExist:
        c8t1 = None
    try:
        c8t2 = courtReservationForm.objects.get(courtDate = date5,courtNumber=8, courtTime = "9:30 - 11:00")
    except courtReservationForm.DoesNotExist:
        c8t2 = None
    try:
        c8t3 = courtReservationForm.objects.get(courtDate = date5,courtNumber=8, courtTime = "11:00 - 12:30")
    except courtReservationForm.DoesNotExist:
        c8t3 = None
    try:
        c8t4 = courtReservationForm.objects.get(courtDate = date5,courtNumber=8, courtTime = "12:30 - 2:00")
    except courtReservationForm.DoesNotExist:
        c8t4 = None
    try:
        c8t5 = courtReservationForm.objects.get(courtDate = date5,courtNumber=8, courtTime = "2:00 - 3:30")
    except courtReservationForm.DoesNotExist:
        c8t5 = None
    try:
        c8t6 = courtReservationForm.objects.get(courtDate = date5,courtNumber=8, courtTime = "3:30 - 5:00")
    except courtReservationForm.DoesNotExist:
        c8t6 = None

    #court 9
    try:
        c9t1 = courtReservationForm.objects.get(courtDate = date5,courtNumber=9, courtTime = "8:00 - 9:30")
    except courtReservationForm.DoesNotExist:
        c9t1 = None
    try:
        c9t2 = courtReservationForm.objects.get(courtDate = date5,courtNumber=9, courtTime = "9:30 - 11:00")
    except courtReservationForm.DoesNotExist:
        c9t2 = None
    try:
        c9t3 = courtReservationForm.objects.get(courtDate = date5,courtNumber=9, courtTime = "11:00 - 12:30")
    except courtReservationForm.DoesNotExist:
        c9t3 = None
    try:
        c9t4 = courtReservationForm.objects.get(courtDate = date5,courtNumber=9, courtTime = "12:30 - 2:00")
    except courtReservationForm.DoesNotExist:
        c9t4 = None
    try:
        c9t5 = courtReservationForm.objects.get(courtDate = date5,courtNumber=9, courtTime = "2:00 - 3:30")
    except courtReservationForm.DoesNotExist:
        c9t5 = None
    try:
        c9t6 = courtReservationForm.objects.get(courtDate = date5,courtNumber=9, courtTime = "3:30 - 5:00")
    except courtReservationForm.DoesNotExist:
        c9t6 = None

    #court 10
    try:
        c10t1 = courtReservationForm.objects.get(courtDate = date5,courtNumber=10, courtTime = "8:00 - 9:30")
    except courtReservationForm.DoesNotExist:
        c10t1 = None
    try:
        c10t2 = courtReservationForm.objects.get(courtDate = date5,courtNumber=10, courtTime = "9:30 - 11:00")
    except courtReservationForm.DoesNotExist:
        c10t2 = None
    try:
        c10t3 = courtReservationForm.objects.get(courtDate = date5,courtNumber=10, courtTime = "11:00 - 12:30")
    except courtReservationForm.DoesNotExist:
        c10t3 = None
    try:
        c10t4 = courtReservationForm.objects.get(courtDate = date5,courtNumber=10, courtTime = "12:30 - 2:00")
    except courtReservationForm.DoesNotExist:
        c10t4 = None
    try:
        c10t5 = courtReservationForm.objects.get(courtDate = date5,courtNumber=10, courtTime = "2:00 - 3:30")
    except courtReservationForm.DoesNotExist:
        c10t5 = None
    try:
        c10t6 = courtReservationForm.objects.get(courtDate = date5,courtNumber=10, courtTime = "3:30 - 5:00")
    except courtReservationForm.DoesNotExist:
        c10t6 = None

    #court 11
    try:
        c11t1 = courtReservationForm.objects.get(courtDate = date5,courtNumber=11, courtTime = "8:00 - 9:30")
    except courtReservationForm.DoesNotExist:
        c11t1 = None
    try:
        c11t2 = courtReservationForm.objects.get(courtDate = date5,courtNumber=11, courtTime = "9:30 - 11:00")
    except courtReservationForm.DoesNotExist:
        c11t2 = None
    try:
        c11t3 = courtReservationForm.objects.get(courtDate = date5,courtNumber=11, courtTime = "11:00 - 12:30")
    except courtReservationForm.DoesNotExist:
        c11t3 = None
    try:
        c11t4 = courtReservationForm.objects.get(courtDate = date5,courtNumber=11, courtTime = "12:30 - 2:00")
    except courtReservationForm.DoesNotExist:
        c11t4 = None
    try:
        c11t5 = courtReservationForm.objects.get(courtDate = date5,courtNumber=11, courtTime = "2:00 - 3:30")
    except courtReservationForm.DoesNotExist:
        c11t5 = None
    try:
        c11t6 = courtReservationForm.objects.get(courtDate = date5,courtNumber=11, courtTime = "3:30 - 5:00")
    except courtReservationForm.DoesNotExist:
        c11t6 = None

    #court 12
    try:
        c12t1 = courtReservationForm.objects.get(courtDate = date5,courtNumber=12, courtTime = "8:00 - 9:30")
    except courtReservationForm.DoesNotExist:
        c12t1 = None
    try:
        c12t2 = courtReservationForm.objects.get(courtDate = date5,courtNumber=12, courtTime = "9:30 - 11:00")
    except courtReservationForm.DoesNotExist:
        c12t2 = None
    try:
        c12t3 = courtReservationForm.objects.get(courtDate = date5,courtNumber=12, courtTime = "11:00 - 12:30")
    except courtReservationForm.DoesNotExist:
        c12t3 = None
    try:
        c12t4 = courtReservationForm.objects.get(courtDate = date5,courtNumber=12, courtTime = "12:30 - 2:00")
    except courtReservationForm.DoesNotExist:
        c12t4 = None
    try:
        c12t5 = courtReservationForm.objects.get(courtDate = date5,courtNumber=12, courtTime = "2:00 - 3:30")
    except courtReservationForm.DoesNotExist:
        c12t5 = None
    try:
        c12t6 = courtReservationForm.objects.get(courtDate = date5,courtNumber=12, courtTime = "3:30 - 5:00")
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
               'c12t1' :c12t1, 'c12t2' : c12t2, 'c12t3' : c12t3, 'c12t4' :c12t4, 'c12t5' : c12t5, 'c12t6' : c12t6,
               'date1' :date1, 'date2':date2, 'date3':date3, 'date4':date4, 'date5':date5, 'date6':date6, 'date7':date7,
               'date1Disp':date1Disp, 'date2Disp':date2Disp,'date3Disp':date3Disp,'date4Disp':date4Disp,
               'date5Disp':date5Disp,'date6Disp':date6Disp,'date7Disp':date7Disp
               }
    return render(request, 'courts/menu5.html',context)

def menu6(request):
    #dates
    date1 = datetime.now()
    date2 = (datetime.now()+timedelta(1))
    date3 = (datetime.now()+timedelta(2))
    date4 = (datetime.now()+timedelta(3))
    date5 = (datetime.now()+timedelta(4))
    date6 = (datetime.now()+timedelta(5))
    date7 = (datetime.now()+timedelta(6))

    date1Disp = datetime.now().strftime("%b. %d, %Y")
    date2Disp = (datetime.now()+timedelta(1)).strftime("%b. %d, %Y")
    date3Disp = (datetime.now()+timedelta(2)).strftime("%b. %d, %Y")
    date4Disp = (datetime.now()+timedelta(3)).strftime("%b. %d, %Y")
    date5Disp = (datetime.now()+timedelta(4)).strftime("%b. %d, %Y")
    date6Disp = (datetime.now()+timedelta(5)).strftime("%b. %d, %Y")
    date7Disp = (datetime.now()+timedelta(6)).strftime("%b. %d, %Y")
    #court 1
    try:
        c1t1 = courtReservationForm.objects.get(courtDate = date6,courtNumber=1, courtTime = "8:00 - 9:30")
    except courtReservationForm.DoesNotExist:
        c1t1 = None
    try:
        c1t2 = courtReservationForm.objects.get(courtDate = date6,courtNumber=1, courtTime = "9:30 - 11:00")
    except courtReservationForm.DoesNotExist:
        c1t2 = None
    try:
        c1t3 = courtReservationForm.objects.get(courtDate = date6,courtNumber=1, courtTime = "11:00 - 12:30")
    except courtReservationForm.DoesNotExist:
        c1t3 = None
    try:
        c1t4 = courtReservationForm.objects.get(courtDate = date6,courtNumber=1, courtTime = "12:30 - 2:00")
    except courtReservationForm.DoesNotExist:
        c1t4 = None
    try:
        c1t5 = courtReservationForm.objects.get(courtDate = date6,courtNumber=1, courtTime = "2:00 - 3:30")
    except courtReservationForm.DoesNotExist:
        c1t5 = None
    try:
        c1t6 = courtReservationForm.objects.get(courtDate = date6,courtNumber=1, courtTime = "3:30 - 5:00")
    except courtReservationForm.DoesNotExist:
        c1t6 = None

    #court 2
    try:
        c2t1 = courtReservationForm.objects.get(courtDate = date6,courtNumber=2, courtTime = "8:00 - 9:30")
    except courtReservationForm.DoesNotExist:
        c2t1 = None
    try:
        c2t2 = courtReservationForm.objects.get(courtDate = date6,courtNumber=2, courtTime = "9:30 - 11:00")
    except courtReservationForm.DoesNotExist:
        c2t2 = None
    try:
        c2t3 = courtReservationForm.objects.get(courtDate = date6,courtNumber=2, courtTime = "11:00 - 12:30")
    except courtReservationForm.DoesNotExist:
        c2t3 = None
    try:
        c2t4 = courtReservationForm.objects.get(courtDate = date6,courtNumber=2, courtTime = "12:30 - 2:00")
    except courtReservationForm.DoesNotExist:
        c2t4 = None
    try:
        c2t5 = courtReservationForm.objects.get(courtDate = date6,courtNumber=2, courtTime = "2:00 - 3:30")
    except courtReservationForm.DoesNotExist:
        c2t5 = None
    try:
        c2t6 = courtReservationForm.objects.get(courtDate = date6,courtNumber=2, courtTime = "3:30 - 5:00")
    except courtReservationForm.DoesNotExist:
        c2t6 = None

    #court 3
    try:
        c3t1 = courtReservationForm.objects.get(courtDate = date6,courtNumber=3, courtTime = "8:00 - 9:30")
    except courtReservationForm.DoesNotExist:
        c3t1 = None
    try:
        c3t2 = courtReservationForm.objects.get(courtDate = date6,courtNumber=3, courtTime = "9:30 - 11:00")
    except courtReservationForm.DoesNotExist:
        c3t2 = None
    try:
        c3t3 = courtReservationForm.objects.get(courtDate = date6,courtNumber=3, courtTime = "11:00 - 12:30")
    except courtReservationForm.DoesNotExist:
        c3t3 = None
    try:
        c3t4 = courtReservationForm.objects.get(courtDate = date6,courtNumber=3, courtTime = "12:30 - 2:00")
    except courtReservationForm.DoesNotExist:
        c3t4 = None
    try:
        c3t5 = courtReservationForm.objects.get(courtDate = date6,courtNumber=3, courtTime = "2:00 - 3:30")
    except courtReservationForm.DoesNotExist:
        c3t5 = None
    try:
        c3t6 = courtReservationForm.objects.get(courtDate = date6,courtNumber=3, courtTime = "3:30 - 5:00")
    except courtReservationForm.DoesNotExist:
        c3t6 = None
    
    #court 4
    try:
        c4t1 = courtReservationForm.objects.get(courtDate = date6,courtNumber=4, courtTime = "8:00 - 9:30")
    except courtReservationForm.DoesNotExist:
        c4t1 = None
    try:
        c4t2 = courtReservationForm.objects.get(courtDate = date6,courtNumber=4, courtTime = "9:30 - 11:00")
    except courtReservationForm.DoesNotExist:
        c4t2 = None
    try:
        c4t3 = courtReservationForm.objects.get(courtDate = date6,courtNumber=4, courtTime = "11:00 - 12:30")
    except courtReservationForm.DoesNotExist:
        c4t3 = None
    try:
        c4t4 = courtReservationForm.objects.get(courtDate = date6,courtNumber=4, courtTime = "12:30 - 2:00")
    except courtReservationForm.DoesNotExist:
        c4t4 = None
    try:
        c4t5 = courtReservationForm.objects.get(courtDate = date6,courtNumber=4, courtTime = "2:00 - 3:30")
    except courtReservationForm.DoesNotExist:
        c4t5 = None
    try:
        c4t6 = courtReservationForm.objects.get(courtDate = date6,courtNumber=4, courtTime = "3:30 - 5:00")
    except courtReservationForm.DoesNotExist:
        c4t6 = None

    #court 5
    try:
        c5t1 = courtReservationForm.objects.get(courtDate = date6,courtNumber=5, courtTime = "8:00 - 9:30")
    except courtReservationForm.DoesNotExist:
        c5t1 = None
    try:
        c5t2 = courtReservationForm.objects.get(courtDate = date6,courtNumber=5, courtTime = "9:30 - 11:00")
    except courtReservationForm.DoesNotExist:
        c5t2 = None
    try:
        c5t3 = courtReservationForm.objects.get(courtDate = date6,courtNumber=5, courtTime = "11:00 - 12:30")
    except courtReservationForm.DoesNotExist:
        c5t3 = None
    try:
        c5t4 = courtReservationForm.objects.get(courtDate = date6,courtNumber=5, courtTime = "12:30 - 2:00")
    except courtReservationForm.DoesNotExist:
        c5t4 = None
    try:
        c5t5 = courtReservationForm.objects.get(courtDate = date6,courtNumber=5, courtTime = "2:00 - 3:30")
    except courtReservationForm.DoesNotExist:
        c5t5 = None
    try:
        c5t6 = courtReservationForm.objects.get(courtDate = date6,courtNumber=5, courtTime = "3:30 - 5:00")
    except courtReservationForm.DoesNotExist:
        c5t6 = None

    #court 6
    try:
        c6t1 = courtReservationForm.objects.get(courtDate = date6,courtNumber=6, courtTime = "8:00 - 9:30")
    except courtReservationForm.DoesNotExist:
        c6t1 = None
    try:
        c6t2 = courtReservationForm.objects.get(courtDate = date6,courtNumber=6, courtTime = "9:30 - 11:00")
    except courtReservationForm.DoesNotExist:
        c6t2 = None
    try:
        c6t3 = courtReservationForm.objects.get(courtDate = date6,courtNumber=6, courtTime = "11:00 - 12:30")
    except courtReservationForm.DoesNotExist:
        c6t3 = None
    try:
        c6t4 = courtReservationForm.objects.get(courtDate = date6,courtNumber=6, courtTime = "12:30 - 2:00")
    except courtReservationForm.DoesNotExist:
        c6t4 = None
    try:
        c6t5 = courtReservationForm.objects.get(courtDate = date6,courtNumber=6, courtTime = "2:00 - 3:30")
    except courtReservationForm.DoesNotExist:
        c6t5 = None
    try:
        c6t6 = courtReservationForm.objects.get(courtDate = date6,courtNumber=6, courtTime = "3:30 - 5:00")
    except courtReservationForm.DoesNotExist:
        c6t6 = None
    
    #court 7
    try:
        c7t1 = courtReservationForm.objects.get(courtDate = date6,courtNumber=7, courtTime = "8:00 - 9:30")
    except courtReservationForm.DoesNotExist:
        c7t1 = None
    try:
        c7t2 = courtReservationForm.objects.get(courtDate = date6,courtNumber=7, courtTime = "9:30 - 11:00")
    except courtReservationForm.DoesNotExist:
        c7t2 = None
    try:
        c7t3 = courtReservationForm.objects.get(courtDate = date6,courtNumber=7, courtTime = "11:00 - 12:30")
    except courtReservationForm.DoesNotExist:
        c7t3 = None
    try:
        c7t4 = courtReservationForm.objects.get(courtDate = date6,courtNumber=7, courtTime = "12:30 - 2:00")
    except courtReservationForm.DoesNotExist:
        c7t4 = None
    try:
        c7t5 = courtReservationForm.objects.get(courtDate = date6,courtNumber=7, courtTime = "2:00 - 3:30")
    except courtReservationForm.DoesNotExist:
        c7t5 = None
    try:
        c7t6 = courtReservationForm.objects.get(courtDate = date6,courtNumber=7, courtTime = "3:30 - 5:00")
    except courtReservationForm.DoesNotExist:
        c7t6 = None
    
    #court 8
    try:
        c8t1 = courtReservationForm.objects.get(courtDate = date6,courtNumber=8, courtTime = "8:00 - 9:30")
    except courtReservationForm.DoesNotExist:
        c8t1 = None
    try:
        c8t2 = courtReservationForm.objects.get(courtDate = date6,courtNumber=8, courtTime = "9:30 - 11:00")
    except courtReservationForm.DoesNotExist:
        c8t2 = None
    try:
        c8t3 = courtReservationForm.objects.get(courtDate = date6,courtNumber=8, courtTime = "11:00 - 12:30")
    except courtReservationForm.DoesNotExist:
        c8t3 = None
    try:
        c8t4 = courtReservationForm.objects.get(courtDate = date6,courtNumber=8, courtTime = "12:30 - 2:00")
    except courtReservationForm.DoesNotExist:
        c8t4 = None
    try:
        c8t5 = courtReservationForm.objects.get(courtDate = date6,courtNumber=8, courtTime = "2:00 - 3:30")
    except courtReservationForm.DoesNotExist:
        c8t5 = None
    try:
        c8t6 = courtReservationForm.objects.get(courtDate = date6,courtNumber=8, courtTime = "3:30 - 5:00")
    except courtReservationForm.DoesNotExist:
        c8t6 = None

    #court 9
    try:
        c9t1 = courtReservationForm.objects.get(courtDate = date6,courtNumber=9, courtTime = "8:00 - 9:30")
    except courtReservationForm.DoesNotExist:
        c9t1 = None
    try:
        c9t2 = courtReservationForm.objects.get(courtDate = date6,courtNumber=9, courtTime = "9:30 - 11:00")
    except courtReservationForm.DoesNotExist:
        c9t2 = None
    try:
        c9t3 = courtReservationForm.objects.get(courtDate = date6,courtNumber=9, courtTime = "11:00 - 12:30")
    except courtReservationForm.DoesNotExist:
        c9t3 = None
    try:
        c9t4 = courtReservationForm.objects.get(courtDate = date6,courtNumber=9, courtTime = "12:30 - 2:00")
    except courtReservationForm.DoesNotExist:
        c9t4 = None
    try:
        c9t5 = courtReservationForm.objects.get(courtDate = date6,courtNumber=9, courtTime = "2:00 - 3:30")
    except courtReservationForm.DoesNotExist:
        c9t5 = None
    try:
        c9t6 = courtReservationForm.objects.get(courtDate = date6,courtNumber=9, courtTime = "3:30 - 5:00")
    except courtReservationForm.DoesNotExist:
        c9t6 = None

    #court 10
    try:
        c10t1 = courtReservationForm.objects.get(courtDate = date6,courtNumber=10, courtTime = "8:00 - 9:30")
    except courtReservationForm.DoesNotExist:
        c10t1 = None
    try:
        c10t2 = courtReservationForm.objects.get(courtDate = date6,courtNumber=10, courtTime = "9:30 - 11:00")
    except courtReservationForm.DoesNotExist:
        c10t2 = None
    try:
        c10t3 = courtReservationForm.objects.get(courtDate = date6,courtNumber=10, courtTime = "11:00 - 12:30")
    except courtReservationForm.DoesNotExist:
        c10t3 = None
    try:
        c10t4 = courtReservationForm.objects.get(courtDate = date6,courtNumber=10, courtTime = "12:30 - 2:00")
    except courtReservationForm.DoesNotExist:
        c10t4 = None
    try:
        c10t5 = courtReservationForm.objects.get(courtDate = date6,courtNumber=10, courtTime = "2:00 - 3:30")
    except courtReservationForm.DoesNotExist:
        c10t5 = None
    try:
        c10t6 = courtReservationForm.objects.get(courtDate = date6,courtNumber=10, courtTime = "3:30 - 5:00")
    except courtReservationForm.DoesNotExist:
        c10t6 = None

    #court 11
    try:
        c11t1 = courtReservationForm.objects.get(courtDate = date6,courtNumber=11, courtTime = "8:00 - 9:30")
    except courtReservationForm.DoesNotExist:
        c11t1 = None
    try:
        c11t2 = courtReservationForm.objects.get(courtDate = date6,courtNumber=11, courtTime = "9:30 - 11:00")
    except courtReservationForm.DoesNotExist:
        c11t2 = None
    try:
        c11t3 = courtReservationForm.objects.get(courtDate = date6,courtNumber=11, courtTime = "11:00 - 12:30")
    except courtReservationForm.DoesNotExist:
        c11t3 = None
    try:
        c11t4 = courtReservationForm.objects.get(courtDate = date6,courtNumber=11, courtTime = "12:30 - 2:00")
    except courtReservationForm.DoesNotExist:
        c11t4 = None
    try:
        c11t5 = courtReservationForm.objects.get(courtDate = date6,courtNumber=11, courtTime = "2:00 - 3:30")
    except courtReservationForm.DoesNotExist:
        c11t5 = None
    try:
        c11t6 = courtReservationForm.objects.get(courtDate = date6,courtNumber=11, courtTime = "3:30 - 5:00")
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
               'c12t1' :c12t1, 'c12t2' : c12t2, 'c12t3' : c12t3, 'c12t4' :c12t4, 'c12t5' : c12t5, 'c12t6' : c12t6,
               'date1' :date1, 'date2':date2, 'date3':date3, 'date4':date4, 'date5':date5, 'date6':date6, 'date7':date7,
               'date1Disp':date1Disp, 'date2Disp':date2Disp,'date3Disp':date3Disp,'date4Disp':date4Disp,
               'date5Disp':date5Disp,'date6Disp':date6Disp,'date7Disp':date7Disp
               }
    return render(request, 'courts/menu6.html',context)

def menu7(request):
    #dates
    date1 = datetime.now()
    date2 = (datetime.now()+timedelta(1))
    date3 = (datetime.now()+timedelta(2))
    date4 = (datetime.now()+timedelta(3))
    date5 = (datetime.now()+timedelta(4))
    date6 = (datetime.now()+timedelta(5))
    date7 = (datetime.now()+timedelta(6))

    date1Disp = datetime.now().strftime("%b. %d, %Y")
    date2Disp = (datetime.now()+timedelta(1)).strftime("%b. %d, %Y")
    date3Disp = (datetime.now()+timedelta(2)).strftime("%b. %d, %Y")
    date4Disp = (datetime.now()+timedelta(3)).strftime("%b. %d, %Y")
    date5Disp = (datetime.now()+timedelta(4)).strftime("%b. %d, %Y")
    date6Disp = (datetime.now()+timedelta(5)).strftime("%b. %d, %Y")
    date7Disp = (datetime.now()+timedelta(6)).strftime("%b. %d, %Y")
    #court 1
    try:
        c1t1 = courtReservationForm.objects.get(courtDate = date7,courtNumber=1, courtTime = "8:00 - 9:30")
    except courtReservationForm.DoesNotExist:
        c1t1 = None
    try:
        c1t2 = courtReservationForm.objects.get(courtDate = date7,courtNumber=1, courtTime = "9:30 - 11:00")
    except courtReservationForm.DoesNotExist:
        c1t2 = None
    try:
        c1t3 = courtReservationForm.objects.get(courtDate = date7,courtNumber=1, courtTime = "11:00 - 12:30")
    except courtReservationForm.DoesNotExist:
        c1t3 = None
    try:
        c1t4 = courtReservationForm.objects.get(courtDate = date7,courtNumber=1, courtTime = "12:30 - 2:00")
    except courtReservationForm.DoesNotExist:
        c1t4 = None
    try:
        c1t5 = courtReservationForm.objects.get(courtDate = date7,courtNumber=1, courtTime = "2:00 - 3:30")
    except courtReservationForm.DoesNotExist:
        c1t5 = None
    try:
        c1t6 = courtReservationForm.objects.get(courtDate = date7,courtNumber=1, courtTime = "3:30 - 5:00")
    except courtReservationForm.DoesNotExist:
        c1t6 = None

    #court 2
    try:
        c2t1 = courtReservationForm.objects.get(courtDate = date7,courtNumber=2, courtTime = "8:00 - 9:30")
    except courtReservationForm.DoesNotExist:
        c2t1 = None
    try:
        c2t2 = courtReservationForm.objects.get(courtDate = date7,courtNumber=2, courtTime = "9:30 - 11:00")
    except courtReservationForm.DoesNotExist:
        c2t2 = None
    try:
        c2t3 = courtReservationForm.objects.get(courtDate = date7,courtNumber=2, courtTime = "11:00 - 12:30")
    except courtReservationForm.DoesNotExist:
        c2t3 = None
    try:
        c2t4 = courtReservationForm.objects.get(courtDate = date7,courtNumber=2, courtTime = "12:30 - 2:00")
    except courtReservationForm.DoesNotExist:
        c2t4 = None
    try:
        c2t5 = courtReservationForm.objects.get(courtDate = date7,courtNumber=2, courtTime = "2:00 - 3:30")
    except courtReservationForm.DoesNotExist:
        c2t5 = None
    try:
        c2t6 = courtReservationForm.objects.get(courtDate = date7,courtNumber=2, courtTime = "3:30 - 5:00")
    except courtReservationForm.DoesNotExist:
        c2t6 = None

    #court 3
    try:
        c3t1 = courtReservationForm.objects.get(courtDate = date7,courtNumber=3, courtTime = "8:00 - 9:30")
    except courtReservationForm.DoesNotExist:
        c3t1 = None
    try:
        c3t2 = courtReservationForm.objects.get(courtDate = date7,courtNumber=3, courtTime = "9:30 - 11:00")
    except courtReservationForm.DoesNotExist:
        c3t2 = None
    try:
        c3t3 = courtReservationForm.objects.get(courtDate = date7,courtNumber=3, courtTime = "11:00 - 12:30")
    except courtReservationForm.DoesNotExist:
        c3t3 = None
    try:
        c3t4 = courtReservationForm.objects.get(courtDate = date7,courtNumber=3, courtTime = "12:30 - 2:00")
    except courtReservationForm.DoesNotExist:
        c3t4 = None
    try:
        c3t5 = courtReservationForm.objects.get(courtDate = date7,courtNumber=3, courtTime = "2:00 - 3:30")
    except courtReservationForm.DoesNotExist:
        c3t5 = None
    try:
        c3t6 = courtReservationForm.objects.get(courtDate = date7,courtNumber=3, courtTime = "3:30 - 5:00")
    except courtReservationForm.DoesNotExist:
        c3t6 = None
    
    #court 4
    try:
        c4t1 = courtReservationForm.objects.get(courtDate = date7,courtNumber=4, courtTime = "8:00 - 9:30")
    except courtReservationForm.DoesNotExist:
        c4t1 = None
    try:
        c4t2 = courtReservationForm.objects.get(courtDate = date7,courtNumber=4, courtTime = "9:30 - 11:00")
    except courtReservationForm.DoesNotExist:
        c4t2 = None
    try:
        c4t3 = courtReservationForm.objects.get(courtDate = date7,courtNumber=4, courtTime = "11:00 - 12:30")
    except courtReservationForm.DoesNotExist:
        c4t3 = None
    try:
        c4t4 = courtReservationForm.objects.get(courtDate = date7,courtNumber=4, courtTime = "12:30 - 2:00")
    except courtReservationForm.DoesNotExist:
        c4t4 = None
    try:
        c4t5 = courtReservationForm.objects.get(courtDate = date7,courtNumber=4, courtTime = "2:00 - 3:30")
    except courtReservationForm.DoesNotExist:
        c4t5 = None
    try:
        c4t6 = courtReservationForm.objects.get(courtDate = date7,courtNumber=4, courtTime = "3:30 - 5:00")
    except courtReservationForm.DoesNotExist:
        c4t6 = None

    #court 5
    try:
        c5t1 = courtReservationForm.objects.get(courtDate = date7,courtNumber=5, courtTime = "8:00 - 9:30")
    except courtReservationForm.DoesNotExist:
        c5t1 = None
    try:
        c5t2 = courtReservationForm.objects.get(courtDate = date7,courtNumber=5, courtTime = "9:30 - 11:00")
    except courtReservationForm.DoesNotExist:
        c5t2 = None
    try:
        c5t3 = courtReservationForm.objects.get(courtDate = date7,courtNumber=5, courtTime = "11:00 - 12:30")
    except courtReservationForm.DoesNotExist:
        c5t3 = None
    try:
        c5t4 = courtReservationForm.objects.get(courtDate = date7,courtNumber=5, courtTime = "12:30 - 2:00")
    except courtReservationForm.DoesNotExist:
        c5t4 = None
    try:
        c5t5 = courtReservationForm.objects.get(courtDate = date7,courtNumber=5, courtTime = "2:00 - 3:30")
    except courtReservationForm.DoesNotExist:
        c5t5 = None
    try:
        c5t6 = courtReservationForm.objects.get(courtDate = date7,courtNumber=5, courtTime = "3:30 - 5:00")
    except courtReservationForm.DoesNotExist:
        c5t6 = None

    #court 6
    try:
        c6t1 = courtReservationForm.objects.get(courtDate = date7,courtNumber=6, courtTime = "8:00 - 9:30")
    except courtReservationForm.DoesNotExist:
        c6t1 = None
    try:
        c6t2 = courtReservationForm.objects.get(courtDate = date7,courtNumber=6, courtTime = "9:30 - 11:00")
    except courtReservationForm.DoesNotExist:
        c6t2 = None
    try:
        c6t3 = courtReservationForm.objects.get(courtDate = date7,courtNumber=6, courtTime = "11:00 - 12:30")
    except courtReservationForm.DoesNotExist:
        c6t3 = None
    try:
        c6t4 = courtReservationForm.objects.get(courtDate = date7,courtNumber=6, courtTime = "12:30 - 2:00")
    except courtReservationForm.DoesNotExist:
        c6t4 = None
    try:
        c6t5 = courtReservationForm.objects.get(courtDate = date7,courtNumber=6, courtTime = "2:00 - 3:30")
    except courtReservationForm.DoesNotExist:
        c6t5 = None
    try:
        c6t6 = courtReservationForm.objects.get(courtDate = date7,courtNumber=6, courtTime = "3:30 - 5:00")
    except courtReservationForm.DoesNotExist:
        c6t6 = None
    
    #court 7
    try:
        c7t1 = courtReservationForm.objects.get(courtDate = date7,courtNumber=7, courtTime = "8:00 - 9:30")
    except courtReservationForm.DoesNotExist:
        c7t1 = None
    try:
        c7t2 = courtReservationForm.objects.get(courtDate = date7,courtNumber=7, courtTime = "9:30 - 11:00")
    except courtReservationForm.DoesNotExist:
        c7t2 = None
    try:
        c7t3 = courtReservationForm.objects.get(courtDate = date7,courtNumber=7, courtTime = "11:00 - 12:30")
    except courtReservationForm.DoesNotExist:
        c7t3 = None
    try:
        c7t4 = courtReservationForm.objects.get(courtDate = date7,courtNumber=7, courtTime = "12:30 - 2:00")
    except courtReservationForm.DoesNotExist:
        c7t4 = None
    try:
        c7t5 = courtReservationForm.objects.get(courtDate = date7,courtNumber=7, courtTime = "2:00 - 3:30")
    except courtReservationForm.DoesNotExist:
        c7t5 = None
    try:
        c7t6 = courtReservationForm.objects.get(courtDate = date7,courtNumber=7, courtTime = "3:30 - 5:00")
    except courtReservationForm.DoesNotExist:
        c7t6 = None
    
    #court 8
    try:
        c8t1 = courtReservationForm.objects.get(courtDate = date7,courtNumber=8, courtTime = "8:00 - 9:30")
    except courtReservationForm.DoesNotExist:
        c8t1 = None
    try:
        c8t2 = courtReservationForm.objects.get(courtDate = date7,courtNumber=8, courtTime = "9:30 - 11:00")
    except courtReservationForm.DoesNotExist:
        c8t2 = None
    try:
        c8t3 = courtReservationForm.objects.get(courtDate = date7,courtNumber=8, courtTime = "11:00 - 12:30")
    except courtReservationForm.DoesNotExist:
        c8t3 = None
    try:
        c8t4 = courtReservationForm.objects.get(courtDate = date7,courtNumber=8, courtTime = "12:30 - 2:00")
    except courtReservationForm.DoesNotExist:
        c8t4 = None
    try:
        c8t5 = courtReservationForm.objects.get(courtDate = date7,courtNumber=8, courtTime = "2:00 - 3:30")
    except courtReservationForm.DoesNotExist:
        c8t5 = None
    try:
        c8t6 = courtReservationForm.objects.get(courtDate = date7,courtNumber=8, courtTime = "3:30 - 5:00")
    except courtReservationForm.DoesNotExist:
        c8t6 = None

    #court 9
    try:
        c9t1 = courtReservationForm.objects.get(courtDate = date7,courtNumber=9, courtTime = "8:00 - 9:30")
    except courtReservationForm.DoesNotExist:
        c9t1 = None
    try:
        c9t2 = courtReservationForm.objects.get(courtDate = date7,courtNumber=9, courtTime = "9:30 - 11:00")
    except courtReservationForm.DoesNotExist:
        c9t2 = None
    try:
        c9t3 = courtReservationForm.objects.get(courtDate = date7,courtNumber=9, courtTime = "11:00 - 12:30")
    except courtReservationForm.DoesNotExist:
        c9t3 = None
    try:
        c9t4 = courtReservationForm.objects.get(courtDate = date7,courtNumber=9, courtTime = "12:30 - 2:00")
    except courtReservationForm.DoesNotExist:
        c9t4 = None
    try:
        c9t5 = courtReservationForm.objects.get(courtDate = date7,courtNumber=9, courtTime = "2:00 - 3:30")
    except courtReservationForm.DoesNotExist:
        c9t5 = None
    try:
        c9t6 = courtReservationForm.objects.get(courtDate = date7,courtNumber=9, courtTime = "3:30 - 5:00")
    except courtReservationForm.DoesNotExist:
        c9t6 = None

    #court 10
    try:
        c10t1 = courtReservationForm.objects.get(courtDate = date7,courtNumber=10, courtTime = "8:00 - 9:30")
    except courtReservationForm.DoesNotExist:
        c10t1 = None
    try:
        c10t2 = courtReservationForm.objects.get(courtDate = date7,courtNumber=10, courtTime = "9:30 - 11:00")
    except courtReservationForm.DoesNotExist:
        c10t2 = None
    try:
        c10t3 = courtReservationForm.objects.get(courtDate = date7,courtNumber=10, courtTime = "11:00 - 12:30")
    except courtReservationForm.DoesNotExist:
        c10t3 = None
    try:
        c10t4 = courtReservationForm.objects.get(courtDate = date7,courtNumber=10, courtTime = "12:30 - 2:00")
    except courtReservationForm.DoesNotExist:
        c10t4 = None
    try:
        c10t5 = courtReservationForm.objects.get(courtDate = date7,courtNumber=10, courtTime = "2:00 - 3:30")
    except courtReservationForm.DoesNotExist:
        c10t5 = None
    try:
        c10t6 = courtReservationForm.objects.get(courtDate = date7,courtNumber=10, courtTime = "3:30 - 5:00")
    except courtReservationForm.DoesNotExist:
        c10t6 = None

    #court 11
    try:
        c11t1 = courtReservationForm.objects.get(courtDate = date7,courtNumber=11, courtTime = "8:00 - 9:30")
    except courtReservationForm.DoesNotExist:
        c11t1 = None
    try:
        c11t2 = courtReservationForm.objects.get(courtDate = date7,courtNumber=11, courtTime = "9:30 - 11:00")
    except courtReservationForm.DoesNotExist:
        c11t2 = None
    try:
        c11t3 = courtReservationForm.objects.get(courtDate = date7,courtNumber=11, courtTime = "11:00 - 12:30")
    except courtReservationForm.DoesNotExist:
        c11t3 = None
    try:
        c11t4 = courtReservationForm.objects.get(courtDate = date7,courtNumber=11, courtTime = "12:30 - 2:00")
    except courtReservationForm.DoesNotExist:
        c11t4 = None
    try:
        c11t5 = courtReservationForm.objects.get(courtDate = date7,courtNumber=11, courtTime = "2:00 - 3:30")
    except courtReservationForm.DoesNotExist:
        c11t5 = None
    try:
        c11t6 = courtReservationForm.objects.get(courtDate = date7,courtNumber=11, courtTime = "3:30 - 5:00")
    except courtReservationForm.DoesNotExist:
        c11t6 = None

    #court 12
    try:
        c12t1 = courtReservationForm.objects.get(courtDate = date7,courtNumber=12, courtTime = "8:00 - 9:30")
    except courtReservationForm.DoesNotExist:
        c12t1 = None
    try:
        c12t2 = courtReservationForm.objects.get(courtDate = date7,courtNumber=12, courtTime = "9:30 - 11:00")
    except courtReservationForm.DoesNotExist:
        c12t2 = None
    try:
        c12t3 = courtReservationForm.objects.get(courtDate = date7,courtNumber=12, courtTime = "11:00 - 12:30")
    except courtReservationForm.DoesNotExist:
        c12t3 = None
    try:
        c12t4 = courtReservationForm.objects.get(courtDate = date7,courtNumber=12, courtTime = "12:30 - 2:00")
    except courtReservationForm.DoesNotExist:
        c12t4 = None
    try:
        c12t5 = courtReservationForm.objects.get(courtDate = date7,courtNumber=12, courtTime = "2:00 - 3:30")
    except courtReservationForm.DoesNotExist:
        c12t5 = None
    try:
        c12t6 = courtReservationForm.objects.get(courtDate = date7,courtNumber=12, courtTime = "3:30 - 5:00")
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
               'c12t1' :c12t1, 'c12t2' : c12t2, 'c12t3' : c12t3, 'c12t4' :c12t4, 'c12t5' : c12t5, 'c12t6' : c12t6,
               'date1' :date1, 'date2':date2, 'date3':date3, 'date4':date4, 'date5':date5, 'date6':date6, 'date7':date7,
               'date1Disp':date1Disp, 'date2Disp':date2Disp,'date3Disp':date3Disp,'date4Disp':date4Disp,
               'date5Disp':date5Disp,'date6Disp':date6Disp,'date7Disp':date7Disp
               }
    return render(request, 'courts/menu7.html',context)

#court 1
def d1c1t1(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now(), courtNumber=1, courtTime= "8:00 - 9:30", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d1c1t2(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now(),courtNumber=1, courtTime= "9:30 - 11:00", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d1c1t3(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now(), courtNumber=1, courtTime= "11:00 - 12:30", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d1c1t4(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now(), courtNumber=1, courtTime= "12:30 - 2:00", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d1c1t5(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now(), courtNumber=1, courtTime= "2:00 - 3:30", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d1c1t6(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now(), courtNumber=1, courtTime= "3:30 - 5:00", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

#court 2
def d1c2t1(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now(), courtNumber=2, courtTime= "8:00 - 9:30", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d1c2t2(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now(), courtNumber=2, courtTime= "9:30 - 11:00", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d1c2t3(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now(), courtNumber=2, courtTime= "11:00 - 12:30", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d1c2t4(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now(), courtNumber=2, courtTime= "12:30 - 2:00", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d1c2t5(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now(), courtNumber=2, courtTime= "2:00 - 3:30", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d1c2t6(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now(), courtNumber=2, courtTime= "3:30 - 5:00", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

#court 3
def d1c3t1(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now(), courtNumber=3, courtTime= "8:00 - 9:30", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d1c3t2(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now(), courtNumber=3, courtTime= "9:30 - 11:00", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d1c3t3(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now(), courtNumber=3, courtTime= "11:00 - 12:30", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d1c3t4(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now(), courtNumber=3, courtTime= "12:30 - 2:00", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d1c3t5(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now(), courtNumber=3, courtTime= "2:00 - 3:30", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d1c3t6(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now(), courtNumber=3, courtTime= "3:30 - 5:00", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

#court 4
def d1c4t1(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now(), courtNumber=4, courtTime= "8:00 - 9:30", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d1c4t2(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now(), courtNumber=4, courtTime= "9:30 - 11:00", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d1c4t3(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now(), courtNumber=4, courtTime= "11:00 - 12:30", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d1c4t4(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now(), courtNumber=4, courtTime= "12:30 - 2:00", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d1c4t5(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now(), courtNumber=4, courtTime= "2:00 - 3:30", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d1c4t6(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now(), courtNumber=4, courtTime= "3:30 - 5:00", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

#court 5
def d1c5t1(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now(), courtNumber=5, courtTime= "8:00 - 9:30", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d1c5t2(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now(), courtNumber=5, courtTime= "9:30 - 11:00", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d1c5t3(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now(), courtNumber=5, courtTime= "11:00 - 12:30", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d1c5t4(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now(), courtNumber=5, courtTime= "12:30 - 2:00", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d1c5t5(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now(), courtNumber=5, courtTime= "2:00 - 3:30", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d1c5t6(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now(), courtNumber=5, courtTime= "3:30 - 5:00", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

#court 6
def d1c6t1(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now(), courtNumber=6, courtTime= "8:00 - 9:30", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d1c6t2(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now(), courtNumber=6, courtTime= "9:30 - 11:00", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d1c6t3(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now(), courtNumber=6, courtTime= "11:00 - 12:30", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d1c6t4(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now(), courtNumber=6, courtTime= "12:30 - 2:00", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d1c6t5(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now(), courtNumber=6, courtTime= "2:00 - 3:30", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d1c6t6(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now(), courtNumber=6, courtTime= "3:30 - 5:00", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

#court 7
def d1c7t1(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now(), courtNumber=7, courtTime= "8:00 - 9:30", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d1c7t2(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now(), courtNumber=7, courtTime= "9:30 - 11:00", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d1c7t3(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now(), courtNumber=7, courtTime= "11:00 - 12:30", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d1c7t4(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now(), courtNumber=7, courtTime= "12:30 - 2:00", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d1c7t5(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now(), courtNumber=7, courtTime= "2:00 - 3:30", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d1c7t6(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now(), courtNumber=7, courtTime= "3:30 - 5:00", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

#court 8
def d1c8t1(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now(), courtNumber=8, courtTime= "8:00 - 9:30", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d1c8t2(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now(), courtNumber=8, courtTime= "9:30 - 11:00", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d1c8t3(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now(), courtNumber=8, courtTime= "11:00 - 12:30", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d1c8t4(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now(), courtNumber=8, courtTime= "12:30 - 2:00", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d1c8t5(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now(), courtNumber=8, courtTime= "2:00 - 3:30", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d1c8t6(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now(), courtNumber=8, courtTime= "3:30 - 5:00", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

#court 9
def d1c9t1(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now(), courtNumber=9, courtTime= "8:00 - 9:30", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d1c9t2(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now(), courtNumber=9, courtTime= "9:30 - 11:00", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d1c9t3(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now(), courtNumber=9, courtTime= "11:00 - 12:30", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d1c9t4(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now(), courtNumber=9, courtTime= "12:30 - 2:00", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d1c9t5(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now(), courtNumber=9, courtTime= "2:00 - 3:30", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d1c9t6(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now(), courtNumber=9, courtTime= "3:30 - 5:00", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

#court 10
def d1c10t1(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now(), courtNumber=10, courtTime= "8:00 - 9:30", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d1c10t2(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now(), courtNumber=10, courtTime= "9:30 - 11:00", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d1c10t3(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now(), courtNumber=10, courtTime= "11:00 - 12:30", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d1c10t4(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now(), courtNumber=10, courtTime= "12:30 - 2:00", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d1c10t5(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now(), courtNumber=10, courtTime= "2:00 - 3:30", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d1c10t6(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now(), courtNumber=10, courtTime= "3:30 - 5:00", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

#court 11
def d1c11t1(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now(), courtNumber=11, courtTime= "8:00 - 9:30", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d1c11t2(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now(), courtNumber=11, courtTime= "9:30 - 11:00", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d1c11t3(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now(), courtNumber=11, courtTime= "11:00 - 12:30", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d1c11t4(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now(), courtNumber=11, courtTime= "12:30 - 2:00", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d1c11t5(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now(), courtNumber=11, courtTime= "2:00 - 3:30", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d1c11t6(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now(), courtNumber=11, courtTime= "3:30 - 5:00", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

#court 12
def d1c12t1(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now(), courtNumber=12, courtTime= "8:00 - 9:30", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d1c12t2(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now(), courtNumber=12, courtTime= "9:30 - 11:00", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d1c12t3(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now(), courtNumber=12, courtTime= "11:00 - 12:30", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d1c12t4(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now(), courtNumber=12, courtTime= "12:30 - 2:00", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d1c12t5(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now(), courtNumber=12, courtTime= "2:00 - 3:30", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d1c12t6(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now(), courtNumber=12, courtTime= "3:30 - 5:00", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d2c1t1(request,):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(1), courtNumber=1, courtTime= "8:00 - 9:30", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d2c1t2(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(1),courtNumber=1, courtTime= "9:30 - 11:00", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d2c1t3(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(1), courtNumber=1, courtTime= "11:00 - 12:30", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d2c1t4(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(1), courtNumber=1, courtTime= "12:30 - 2:00", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d2c1t5(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(1), courtNumber=1, courtTime= "2:00 - 3:30", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d2c1t6(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(1), courtNumber=1, courtTime= "3:30 - 5:00", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

#court 2
def d2c2t1(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(1), courtNumber=2, courtTime= "8:00 - 9:30", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d2c2t2(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(1), courtNumber=2, courtTime= "9:30 - 11:00", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d2c2t3(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(1), courtNumber=2, courtTime= "11:00 - 12:30", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d2c2t4(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(1), courtNumber=2, courtTime= "12:30 - 2:00", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d2c2t5(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(1), courtNumber=2, courtTime= "2:00 - 3:30", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d2c2t6(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(1), courtNumber=2, courtTime= "3:30 - 5:00", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

#court 3
def d2c3t1(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(1), courtNumber=3, courtTime= "8:00 - 9:30", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d2c3t2(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(1), courtNumber=3, courtTime= "9:30 - 11:00", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d2c3t3(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(1), courtNumber=3, courtTime= "11:00 - 12:30", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d2c3t4(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(1), courtNumber=3, courtTime= "12:30 - 2:00", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d2c3t5(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(1), courtNumber=3, courtTime= "2:00 - 3:30", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d2c3t6(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(1), courtNumber=3, courtTime= "3:30 - 5:00", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

#court 4
def d2c4t1(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(1), courtNumber=4, courtTime= "8:00 - 9:30", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d2c4t2(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(1), courtNumber=4, courtTime= "9:30 - 11:00", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d2c4t3(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(1), courtNumber=4, courtTime= "11:00 - 12:30", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d2c4t4(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(1), courtNumber=4, courtTime= "12:30 - 2:00", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d2c4t5(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(1), courtNumber=4, courtTime= "2:00 - 3:30", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d2c4t6(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(1), courtNumber=4, courtTime= "3:30 - 5:00", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

#court 5
def d2c5t1(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(1), courtNumber=5, courtTime= "8:00 - 9:30", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d2c5t2(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(1), courtNumber=5, courtTime= "9:30 - 11:00", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d2c5t3(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(1), courtNumber=5, courtTime= "11:00 - 12:30", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d2c5t4(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(1), courtNumber=5, courtTime= "12:30 - 2:00", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d2c5t5(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(1), courtNumber=5, courtTime= "2:00 - 3:30", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d2c5t6(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(1), courtNumber=5, courtTime= "3:30 - 5:00", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

#court 6
def d2c6t1(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(1), courtNumber=6, courtTime= "8:00 - 9:30", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d2c6t2(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(1), courtNumber=6, courtTime= "9:30 - 11:00", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d2c6t3(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(1), courtNumber=6, courtTime= "11:00 - 12:30", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d2c6t4(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(1), courtNumber=6, courtTime= "12:30 - 2:00", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d2c6t5(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(1), courtNumber=6, courtTime= "2:00 - 3:30", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d2c6t6(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(1), courtNumber=6, courtTime= "3:30 - 5:00", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

#court 7
def d2c7t1(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(1), courtNumber=7, courtTime= "8:00 - 9:30", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d2c7t2(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(1), courtNumber=7, courtTime= "9:30 - 11:00", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d2c7t3(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(1), courtNumber=7, courtTime= "11:00 - 12:30", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d2c7t4(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(1), courtNumber=7, courtTime= "12:30 - 2:00", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d2c7t5(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(1), courtNumber=7, courtTime= "2:00 - 3:30", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d2c7t6(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(1), courtNumber=7, courtTime= "3:30 - 5:00", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

#court 8
def d2c8t1(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(1), courtNumber=8, courtTime= "8:00 - 9:30", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d2c8t2(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(1), courtNumber=8, courtTime= "9:30 - 11:00", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d2c8t3(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(1), courtNumber=8, courtTime= "11:00 - 12:30", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d2c8t4(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(1), courtNumber=8, courtTime= "12:30 - 2:00", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d2c8t5(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(1), courtNumber=8, courtTime= "2:00 - 3:30", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d2c8t6(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(1), courtNumber=8, courtTime= "3:30 - 5:00", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

#court 9
def d2c9t1(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(1), courtNumber=9, courtTime= "8:00 - 9:30", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d2c9t2(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(1), courtNumber=9, courtTime= "9:30 - 11:00", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d2c9t3(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(1), courtNumber=9, courtTime= "11:00 - 12:30", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d2c9t4(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(1), courtNumber=9, courtTime= "12:30 - 2:00", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d2c9t5(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(1), courtNumber=9, courtTime= "2:00 - 3:30", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d2c9t6(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(1), courtNumber=9, courtTime= "3:30 - 5:00", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

#court 10
def d2c10t1(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(1), courtNumber=10, courtTime= "8:00 - 9:30", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d2c10t2(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(1), courtNumber=10, courtTime= "9:30 - 11:00", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d2c10t3(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(1), courtNumber=10, courtTime= "11:00 - 12:30", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d2c10t4(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(1), courtNumber=10, courtTime= "12:30 - 2:00", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d2c10t5(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(1), courtNumber=10, courtTime= "2:00 - 3:30", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d2c10t6(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(1), courtNumber=10, courtTime= "3:30 - 5:00", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

#court 11
def d2c11t1(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(1), courtNumber=11, courtTime= "8:00 - 9:30", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d2c11t2(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(1), courtNumber=11, courtTime= "9:30 - 11:00", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d2c11t3(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(1), courtNumber=11, courtTime= "11:00 - 12:30", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d2c11t4(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(1), courtNumber=11, courtTime= "12:30 - 2:00", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d2c11t5(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(1), courtNumber=11, courtTime= "2:00 - 3:30", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d2c11t6(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(1), courtNumber=11, courtTime= "3:30 - 5:00", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

#court 12
def d2c12t1(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(1), courtNumber=12, courtTime= "8:00 - 9:30", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d2c12t2(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(1), courtNumber=12, courtTime= "9:30 - 11:00", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d2c12t3(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(1), courtNumber=12, courtTime= "11:00 - 12:30", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d2c12t4(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(1), courtNumber=12, courtTime= "12:30 - 2:00", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d2c12t5(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(1), courtNumber=12, courtTime= "2:00 - 3:30", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d2c12t6(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(1), courtNumber=12, courtTime= "3:30 - 5:00", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d3c1t1(request,):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(2), courtNumber=1, courtTime= "8:00 - 9:30", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d3c1t2(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(2),courtNumber=1, courtTime= "9:30 - 11:00", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d3c1t3(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(2), courtNumber=1, courtTime= "11:00 - 12:30", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d3c1t4(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(2), courtNumber=1, courtTime= "12:30 - 2:00", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d3c1t5(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(2), courtNumber=1, courtTime= "2:00 - 3:30", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d3c1t6(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(2), courtNumber=1, courtTime= "3:30 - 5:00", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

#court 2
def d3c2t1(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(2), courtNumber=2, courtTime= "8:00 - 9:30", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d3c2t2(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(2), courtNumber=2, courtTime= "9:30 - 11:00", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d3c2t3(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(2), courtNumber=2, courtTime= "11:00 - 12:30", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d3c2t4(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(2), courtNumber=2, courtTime= "12:30 - 2:00", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d3c2t5(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(2), courtNumber=2, courtTime= "2:00 - 3:30", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d3c2t6(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(2), courtNumber=2, courtTime= "3:30 - 5:00", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

#court 3
def d3c3t1(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(2), courtNumber=3, courtTime= "8:00 - 9:30", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d3c3t2(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(2), courtNumber=3, courtTime= "9:30 - 11:00", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d3c3t3(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(2), courtNumber=3, courtTime= "11:00 - 12:30", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d3c3t4(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(2), courtNumber=3, courtTime= "12:30 - 2:00", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d3c3t5(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(2), courtNumber=3, courtTime= "2:00 - 3:30", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d3c3t6(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(2), courtNumber=3, courtTime= "3:30 - 5:00", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

#court 4
def d3c4t1(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(2), courtNumber=4, courtTime= "8:00 - 9:30", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d3c4t2(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(2), courtNumber=4, courtTime= "9:30 - 11:00", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d3c4t3(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(2), courtNumber=4, courtTime= "11:00 - 12:30", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d3c4t4(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(2), courtNumber=4, courtTime= "12:30 - 2:00", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d3c4t5(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(2), courtNumber=4, courtTime= "2:00 - 3:30", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d3c4t6(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(2), courtNumber=4, courtTime= "3:30 - 5:00", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

#court 5
def d3c5t1(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(2), courtNumber=5, courtTime= "8:00 - 9:30", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d3c5t2(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(2), courtNumber=5, courtTime= "9:30 - 11:00", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d3c5t3(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(2), courtNumber=5, courtTime= "11:00 - 12:30", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d3c5t4(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(2), courtNumber=5, courtTime= "12:30 - 2:00", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d3c5t5(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(2), courtNumber=5, courtTime= "2:00 - 3:30", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d3c5t6(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(2), courtNumber=5, courtTime= "3:30 - 5:00", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

#court 6
def d3c6t1(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(2), courtNumber=6, courtTime= "8:00 - 9:30", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d3c6t2(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(2), courtNumber=6, courtTime= "9:30 - 11:00", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d3c6t3(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(2), courtNumber=6, courtTime= "11:00 - 12:30", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d3c6t4(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(2), courtNumber=6, courtTime= "12:30 - 2:00", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d3c6t5(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(2), courtNumber=6, courtTime= "2:00 - 3:30", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d3c6t6(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(2), courtNumber=6, courtTime= "3:30 - 5:00", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

#court 7
def d3c7t1(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(2), courtNumber=7, courtTime= "8:00 - 9:30", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d3c7t2(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(2), courtNumber=7, courtTime= "9:30 - 11:00", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d3c7t3(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(2), courtNumber=7, courtTime= "11:00 - 12:30", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d3c7t4(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(2), courtNumber=7, courtTime= "12:30 - 2:00", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d3c7t5(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(2), courtNumber=7, courtTime= "2:00 - 3:30", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d3c7t6(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(2), courtNumber=7, courtTime= "3:30 - 5:00", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

#court 8
def d3c8t1(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(2), courtNumber=8, courtTime= "8:00 - 9:30", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d3c8t2(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(2), courtNumber=8, courtTime= "9:30 - 11:00", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d3c8t3(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(2), courtNumber=8, courtTime= "11:00 - 12:30", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d3c8t4(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(2), courtNumber=8, courtTime= "12:30 - 2:00", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d3c8t5(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(2), courtNumber=8, courtTime= "2:00 - 3:30", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d3c8t6(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(2), courtNumber=8, courtTime= "3:30 - 5:00", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

#court 9
def d3c9t1(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(2), courtNumber=9, courtTime= "8:00 - 9:30", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d3c9t2(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(2), courtNumber=9, courtTime= "9:30 - 11:00", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d3c9t3(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(2), courtNumber=9, courtTime= "11:00 - 12:30", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d3c9t4(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(2), courtNumber=9, courtTime= "12:30 - 2:00", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d3c9t5(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(2), courtNumber=9, courtTime= "2:00 - 3:30", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d3c9t6(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(2), courtNumber=9, courtTime= "3:30 - 5:00", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

#court 10
def d3c10t1(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(2), courtNumber=10, courtTime= "8:00 - 9:30", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d3c10t2(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(2), courtNumber=10, courtTime= "9:30 - 11:00", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d3c10t3(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(2), courtNumber=10, courtTime= "11:00 - 12:30", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d3c10t4(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(2), courtNumber=10, courtTime= "12:30 - 2:00", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d3c10t5(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(2), courtNumber=10, courtTime= "2:00 - 3:30", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d3c10t6(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(2), courtNumber=10, courtTime= "3:30 - 5:00", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

#court 11
def d3c11t1(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(2), courtNumber=11, courtTime= "8:00 - 9:30", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d3c11t2(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(2), courtNumber=11, courtTime= "9:30 - 11:00", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d3c11t3(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(2), courtNumber=11, courtTime= "11:00 - 12:30", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d3c11t4(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(2), courtNumber=11, courtTime= "12:30 - 2:00", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d3c11t5(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(2), courtNumber=11, courtTime= "2:00 - 3:30", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d3c11t6(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(2), courtNumber=11, courtTime= "3:30 - 5:00", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

#court 12
def d3c12t1(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(2), courtNumber=12, courtTime= "8:00 - 9:30", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d3c12t2(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(2), courtNumber=12, courtTime= "9:30 - 11:00", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d3c12t3(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(2), courtNumber=12, courtTime= "11:00 - 12:30", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d3c12t4(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(2), courtNumber=12, courtTime= "12:30 - 2:00", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d3c12t5(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(2), courtNumber=12, courtTime= "2:00 - 3:30", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d3c12t6(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(2), courtNumber=12, courtTime= "3:30 - 5:00", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d4c1t1(request,):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(3), courtNumber=1, courtTime= "8:00 - 9:30", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d4c1t2(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(3),courtNumber=1, courtTime= "9:30 - 11:00", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d4c1t3(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(3), courtNumber=1, courtTime= "11:00 - 12:30", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d4c1t4(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(3), courtNumber=1, courtTime= "12:30 - 2:00", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d4c1t5(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(3), courtNumber=1, courtTime= "2:00 - 3:30", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d4c1t6(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(3), courtNumber=1, courtTime= "3:30 - 5:00", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

#court 2
def d4c2t1(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(3), courtNumber=2, courtTime= "8:00 - 9:30", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d4c2t2(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(3), courtNumber=2, courtTime= "9:30 - 11:00", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d4c2t3(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(3), courtNumber=2, courtTime= "11:00 - 12:30", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d4c2t4(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(3), courtNumber=2, courtTime= "12:30 - 2:00", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d4c2t5(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(3), courtNumber=2, courtTime= "2:00 - 3:30", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d4c2t6(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(3), courtNumber=2, courtTime= "3:30 - 5:00", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

#court 3
def d4c3t1(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(3), courtNumber=3, courtTime= "8:00 - 9:30", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d4c3t2(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(3), courtNumber=3, courtTime= "9:30 - 11:00", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d4c3t3(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(3), courtNumber=3, courtTime= "11:00 - 12:30", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d4c3t4(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(3), courtNumber=3, courtTime= "12:30 - 2:00", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d4c3t5(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(3), courtNumber=3, courtTime= "2:00 - 3:30", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d4c3t6(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(3), courtNumber=3, courtTime= "3:30 - 5:00", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

#court 4
def d4c4t1(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(3), courtNumber=4, courtTime= "8:00 - 9:30", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d4c4t2(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(3), courtNumber=4, courtTime= "9:30 - 11:00", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d4c4t3(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(3), courtNumber=4, courtTime= "11:00 - 12:30", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d4c4t4(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(3), courtNumber=4, courtTime= "12:30 - 2:00", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d4c4t5(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(3), courtNumber=4, courtTime= "2:00 - 3:30", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d4c4t6(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(3), courtNumber=4, courtTime= "3:30 - 5:00", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

#court 5
def d4c5t1(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(3), courtNumber=5, courtTime= "8:00 - 9:30", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d4c5t2(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(3), courtNumber=5, courtTime= "9:30 - 11:00", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d4c5t3(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(3), courtNumber=5, courtTime= "11:00 - 12:30", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d4c5t4(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(3), courtNumber=5, courtTime= "12:30 - 2:00", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d4c5t5(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(3), courtNumber=5, courtTime= "2:00 - 3:30", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d4c5t6(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(3), courtNumber=5, courtTime= "3:30 - 5:00", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

#court 6
def d4c6t1(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(3), courtNumber=6, courtTime= "8:00 - 9:30", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d4c6t2(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(3), courtNumber=6, courtTime= "9:30 - 11:00", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d4c6t3(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(3), courtNumber=6, courtTime= "11:00 - 12:30", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d4c6t4(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(3), courtNumber=6, courtTime= "12:30 - 2:00", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d4c6t5(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(3), courtNumber=6, courtTime= "2:00 - 3:30", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d4c6t6(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(3), courtNumber=6, courtTime= "3:30 - 5:00", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

#court 7
def d4c7t1(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(3), courtNumber=7, courtTime= "8:00 - 9:30", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d4c7t2(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(3), courtNumber=7, courtTime= "9:30 - 11:00", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d4c7t3(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(3), courtNumber=7, courtTime= "11:00 - 12:30", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d4c7t4(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(3), courtNumber=7, courtTime= "12:30 - 2:00", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d4c7t5(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(3), courtNumber=7, courtTime= "2:00 - 3:30", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d4c7t6(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(3), courtNumber=7, courtTime= "3:30 - 5:00", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

#court 8
def d4c8t1(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(3), courtNumber=8, courtTime= "8:00 - 9:30", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d4c8t2(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(3), courtNumber=8, courtTime= "9:30 - 11:00", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d4c8t3(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(3), courtNumber=8, courtTime= "11:00 - 12:30", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d4c8t4(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(3), courtNumber=8, courtTime= "12:30 - 2:00", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d4c8t5(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(3), courtNumber=8, courtTime= "2:00 - 3:30", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d4c8t6(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(3), courtNumber=8, courtTime= "3:30 - 5:00", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

#court 9
def d4c9t1(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(3), courtNumber=9, courtTime= "8:00 - 9:30", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d4c9t2(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(3), courtNumber=9, courtTime= "9:30 - 11:00", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d4c9t3(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(3), courtNumber=9, courtTime= "11:00 - 12:30", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d4c9t4(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(3), courtNumber=9, courtTime= "12:30 - 2:00", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d4c9t5(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(3), courtNumber=9, courtTime= "2:00 - 3:30", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d4c9t6(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(3), courtNumber=9, courtTime= "3:30 - 5:00", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

#court 10
def d4c10t1(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(3), courtNumber=10, courtTime= "8:00 - 9:30", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d4c10t2(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(3), courtNumber=10, courtTime= "9:30 - 11:00", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d4c10t3(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(3), courtNumber=10, courtTime= "11:00 - 12:30", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d4c10t4(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(3), courtNumber=10, courtTime= "12:30 - 2:00", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d4c10t5(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(3), courtNumber=10, courtTime= "2:00 - 3:30", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d4c10t6(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(3), courtNumber=10, courtTime= "3:30 - 5:00", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

#court 11
def d4c11t1(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(3), courtNumber=11, courtTime= "8:00 - 9:30", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d4c11t2(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(3), courtNumber=11, courtTime= "9:30 - 11:00", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d4c11t3(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(3), courtNumber=11, courtTime= "11:00 - 12:30", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d4c11t4(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(3), courtNumber=11, courtTime= "12:30 - 2:00", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d4c11t5(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(3), courtNumber=11, courtTime= "2:00 - 3:30", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d4c11t6(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(3), courtNumber=11, courtTime= "3:30 - 5:00", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

#court 12
def d4c12t1(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(3), courtNumber=12, courtTime= "8:00 - 9:30", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d4c12t2(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(3), courtNumber=12, courtTime= "9:30 - 11:00", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d4c12t3(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(3), courtNumber=12, courtTime= "11:00 - 12:30", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d4c12t4(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(3), courtNumber=12, courtTime= "12:30 - 2:00", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d4c12t5(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(3), courtNumber=12, courtTime= "2:00 - 3:30", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d4c12t6(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(3), courtNumber=12, courtTime= "3:30 - 5:00", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d5c1t1(request,):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(4), courtNumber=1, courtTime= "8:00 - 9:30", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d5c1t2(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(4),courtNumber=1, courtTime= "9:30 - 11:00", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d5c1t3(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(4), courtNumber=1, courtTime= "11:00 - 12:30", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d5c1t4(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(4), courtNumber=1, courtTime= "12:30 - 2:00", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d5c1t5(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(4), courtNumber=1, courtTime= "2:00 - 3:30", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d5c1t6(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(4), courtNumber=1, courtTime= "3:30 - 5:00", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

#court 2
def d5c2t1(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(4), courtNumber=2, courtTime= "8:00 - 9:30", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d5c2t2(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(4), courtNumber=2, courtTime= "9:30 - 11:00", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d5c2t3(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(4), courtNumber=2, courtTime= "11:00 - 12:30", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d5c2t4(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(4), courtNumber=2, courtTime= "12:30 - 2:00", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d5c2t5(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(4), courtNumber=2, courtTime= "2:00 - 3:30", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d5c2t6(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(4), courtNumber=2, courtTime= "3:30 - 5:00", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

#court 3
def d5c3t1(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(4), courtNumber=3, courtTime= "8:00 - 9:30", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d5c3t2(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(4), courtNumber=3, courtTime= "9:30 - 11:00", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d5c3t3(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(4), courtNumber=3, courtTime= "11:00 - 12:30", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d5c3t4(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(4), courtNumber=3, courtTime= "12:30 - 2:00", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d5c3t5(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(4), courtNumber=3, courtTime= "2:00 - 3:30", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d5c3t6(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(4), courtNumber=3, courtTime= "3:30 - 5:00", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

#court 4
def d5c4t1(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(4), courtNumber=4, courtTime= "8:00 - 9:30", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d5c4t2(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(4), courtNumber=4, courtTime= "9:30 - 11:00", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d5c4t3(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(4), courtNumber=4, courtTime= "11:00 - 12:30", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d5c4t4(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(4), courtNumber=4, courtTime= "12:30 - 2:00", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d5c4t5(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(4), courtNumber=4, courtTime= "2:00 - 3:30", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d5c4t6(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(4), courtNumber=4, courtTime= "3:30 - 5:00", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

#court 5
def d5c5t1(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(4), courtNumber=5, courtTime= "8:00 - 9:30", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d5c5t2(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(4), courtNumber=5, courtTime= "9:30 - 11:00", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d5c5t3(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(4), courtNumber=5, courtTime= "11:00 - 12:30", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d5c5t4(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(4), courtNumber=5, courtTime= "12:30 - 2:00", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d5c5t5(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(4), courtNumber=5, courtTime= "2:00 - 3:30", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d5c5t6(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(4), courtNumber=5, courtTime= "3:30 - 5:00", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

#court 6
def d5c6t1(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(4), courtNumber=6, courtTime= "8:00 - 9:30", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d5c6t2(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(4), courtNumber=6, courtTime= "9:30 - 11:00", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d5c6t3(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(4), courtNumber=6, courtTime= "11:00 - 12:30", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d5c6t4(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(4), courtNumber=6, courtTime= "12:30 - 2:00", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d5c6t5(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(4), courtNumber=6, courtTime= "2:00 - 3:30", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d5c6t6(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(4), courtNumber=6, courtTime= "3:30 - 5:00", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

#court 7
def d5c7t1(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(4), courtNumber=7, courtTime= "8:00 - 9:30", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d5c7t2(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(4), courtNumber=7, courtTime= "9:30 - 11:00", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d5c7t3(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(4), courtNumber=7, courtTime= "11:00 - 12:30", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d5c7t4(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(4), courtNumber=7, courtTime= "12:30 - 2:00", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d5c7t5(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(4), courtNumber=7, courtTime= "2:00 - 3:30", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d5c7t6(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(4), courtNumber=7, courtTime= "3:30 - 5:00", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

#court 8
def d5c8t1(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(4), courtNumber=8, courtTime= "8:00 - 9:30", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d5c8t2(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(4), courtNumber=8, courtTime= "9:30 - 11:00", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d5c8t3(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(4), courtNumber=8, courtTime= "11:00 - 12:30", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d5c8t4(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(4), courtNumber=8, courtTime= "12:30 - 2:00", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d5c8t5(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(4), courtNumber=8, courtTime= "2:00 - 3:30", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d5c8t6(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(4), courtNumber=8, courtTime= "3:30 - 5:00", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

#court 9
def d5c9t1(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(4), courtNumber=9, courtTime= "8:00 - 9:30", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d5c9t2(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(4), courtNumber=9, courtTime= "9:30 - 11:00", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d5c9t3(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(4), courtNumber=9, courtTime= "11:00 - 12:30", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d5c9t4(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(4), courtNumber=9, courtTime= "12:30 - 2:00", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d5c9t5(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(4), courtNumber=9, courtTime= "2:00 - 3:30", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d5c9t6(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(4), courtNumber=9, courtTime= "3:30 - 5:00", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

#court 10
def d5c10t1(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(4), courtNumber=10, courtTime= "8:00 - 9:30", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d5c10t2(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(4), courtNumber=10, courtTime= "9:30 - 11:00", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d5c10t3(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(4), courtNumber=10, courtTime= "11:00 - 12:30", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d5c10t4(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(4), courtNumber=10, courtTime= "12:30 - 2:00", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d5c10t5(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(4), courtNumber=10, courtTime= "2:00 - 3:30", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d5c10t6(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(4), courtNumber=10, courtTime= "3:30 - 5:00", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

#court 11
def d5c11t1(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(4), courtNumber=11, courtTime= "8:00 - 9:30", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d5c11t2(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(4), courtNumber=11, courtTime= "9:30 - 11:00", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d5c11t3(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(4), courtNumber=11, courtTime= "11:00 - 12:30", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d5c11t4(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(4), courtNumber=11, courtTime= "12:30 - 2:00", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d5c11t5(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(4), courtNumber=11, courtTime= "2:00 - 3:30", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d5c11t6(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(4), courtNumber=11, courtTime= "3:30 - 5:00", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

#court 12
def d5c12t1(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(4), courtNumber=12, courtTime= "8:00 - 9:30", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d5c12t2(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(4), courtNumber=12, courtTime= "9:30 - 11:00", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d5c12t3(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(4), courtNumber=12, courtTime= "11:00 - 12:30", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d5c12t4(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(4), courtNumber=12, courtTime= "12:30 - 2:00", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d5c12t5(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(4), courtNumber=12, courtTime= "2:00 - 3:30", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d5c12t6(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(4), courtNumber=12, courtTime= "3:30 - 5:00", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d6c1t1(request,):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(5), courtNumber=1, courtTime= "8:00 - 9:30", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d6c1t2(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(5),courtNumber=1, courtTime= "9:30 - 11:00", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d6c1t3(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(5), courtNumber=1, courtTime= "11:00 - 12:30", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d6c1t4(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(5), courtNumber=1, courtTime= "12:30 - 2:00", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d6c1t5(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(5), courtNumber=1, courtTime= "2:00 - 3:30", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d6c1t6(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(5), courtNumber=1, courtTime= "3:30 - 5:00", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

#court 2
def d6c2t1(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(5), courtNumber=2, courtTime= "8:00 - 9:30", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d6c2t2(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(5), courtNumber=2, courtTime= "9:30 - 11:00", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d6c2t3(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(5), courtNumber=2, courtTime= "11:00 - 12:30", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d6c2t4(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(5), courtNumber=2, courtTime= "12:30 - 2:00", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d6c2t5(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(5), courtNumber=2, courtTime= "2:00 - 3:30", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d6c2t6(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(5), courtNumber=2, courtTime= "3:30 - 5:00", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

#court 3
def d6c3t1(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(5), courtNumber=3, courtTime= "8:00 - 9:30", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d6c3t2(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(5), courtNumber=3, courtTime= "9:30 - 11:00", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d6c3t3(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(5), courtNumber=3, courtTime= "11:00 - 12:30", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d6c3t4(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(5), courtNumber=3, courtTime= "12:30 - 2:00", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d6c3t5(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(5), courtNumber=3, courtTime= "2:00 - 3:30", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d6c3t6(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(5), courtNumber=3, courtTime= "3:30 - 5:00", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

#court 4
def d6c4t1(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(5), courtNumber=4, courtTime= "8:00 - 9:30", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d6c4t2(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(5), courtNumber=4, courtTime= "9:30 - 11:00", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d6c4t3(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(5), courtNumber=4, courtTime= "11:00 - 12:30", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d6c4t4(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(5), courtNumber=4, courtTime= "12:30 - 2:00", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d6c4t5(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(5), courtNumber=4, courtTime= "2:00 - 3:30", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d6c4t6(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(5), courtNumber=4, courtTime= "3:30 - 5:00", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

#court 5
def d6c5t1(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(5), courtNumber=5, courtTime= "8:00 - 9:30", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d6c5t2(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(5), courtNumber=5, courtTime= "9:30 - 11:00", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d6c5t3(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(5), courtNumber=5, courtTime= "11:00 - 12:30", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d6c5t4(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(5), courtNumber=5, courtTime= "12:30 - 2:00", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d6c5t5(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(5), courtNumber=5, courtTime= "2:00 - 3:30", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d6c5t6(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(5), courtNumber=5, courtTime= "3:30 - 5:00", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

#court 6
def d6c6t1(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(5), courtNumber=6, courtTime= "8:00 - 9:30", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d6c6t2(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(5), courtNumber=6, courtTime= "9:30 - 11:00", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d6c6t3(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(5), courtNumber=6, courtTime= "11:00 - 12:30", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d6c6t4(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(5), courtNumber=6, courtTime= "12:30 - 2:00", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d6c6t5(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(5), courtNumber=6, courtTime= "2:00 - 3:30", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d6c6t6(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(5), courtNumber=6, courtTime= "3:30 - 5:00", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

#court 7
def d6c7t1(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(5), courtNumber=7, courtTime= "8:00 - 9:30", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d6c7t2(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(5), courtNumber=7, courtTime= "9:30 - 11:00", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d6c7t3(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(5), courtNumber=7, courtTime= "11:00 - 12:30", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d6c7t4(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(5), courtNumber=7, courtTime= "12:30 - 2:00", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d6c7t5(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(5), courtNumber=7, courtTime= "2:00 - 3:30", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d6c7t6(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(5), courtNumber=7, courtTime= "3:30 - 5:00", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

#court 8
def d6c8t1(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(5), courtNumber=8, courtTime= "8:00 - 9:30", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d6c8t2(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(5), courtNumber=8, courtTime= "9:30 - 11:00", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d6c8t3(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(5), courtNumber=8, courtTime= "11:00 - 12:30", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d6c8t4(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(5), courtNumber=8, courtTime= "12:30 - 2:00", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d6c8t5(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(5), courtNumber=8, courtTime= "2:00 - 3:30", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d6c8t6(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(5), courtNumber=8, courtTime= "3:30 - 5:00", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

#court 9
def d6c9t1(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(5), courtNumber=9, courtTime= "8:00 - 9:30", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d6c9t2(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(5), courtNumber=9, courtTime= "9:30 - 11:00", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d6c9t3(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(5), courtNumber=9, courtTime= "11:00 - 12:30", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d6c9t4(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(5), courtNumber=9, courtTime= "12:30 - 2:00", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d6c9t5(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(5), courtNumber=9, courtTime= "2:00 - 3:30", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d6c9t6(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(5), courtNumber=9, courtTime= "3:30 - 5:00", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

#court 10
def d6c10t1(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(5), courtNumber=10, courtTime= "8:00 - 9:30", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d6c10t2(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(5), courtNumber=10, courtTime= "9:30 - 11:00", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d6c10t3(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(5), courtNumber=10, courtTime= "11:00 - 12:30", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d6c10t4(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(5), courtNumber=10, courtTime= "12:30 - 2:00", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d6c10t5(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(5), courtNumber=10, courtTime= "2:00 - 3:30", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d6c10t6(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(5), courtNumber=10, courtTime= "3:30 - 5:00", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

#court 11
def d6c11t1(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(5), courtNumber=11, courtTime= "8:00 - 9:30", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d6c11t2(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(5), courtNumber=11, courtTime= "9:30 - 11:00", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d6c11t3(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(5), courtNumber=11, courtTime= "11:00 - 12:30", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d6c11t4(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(5), courtNumber=11, courtTime= "12:30 - 2:00", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d6c11t5(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(5), courtNumber=11, courtTime= "2:00 - 3:30", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d6c11t6(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(5), courtNumber=11, courtTime= "3:30 - 5:00", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

#court 12
def d6c12t1(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(5), courtNumber=12, courtTime= "8:00 - 9:30", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d6c12t2(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(5), courtNumber=12, courtTime= "9:30 - 11:00", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d6c12t3(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(5), courtNumber=12, courtTime= "11:00 - 12:30", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d6c12t4(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(5), courtNumber=12, courtTime= "12:30 - 2:00", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d6c12t5(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(5), courtNumber=12, courtTime= "2:00 - 3:30", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d6c12t6(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(5), courtNumber=12, courtTime= "3:30 - 5:00", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d7c1t1(request,):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(6), courtNumber=1, courtTime= "8:00 - 9:30", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d7c1t2(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(6),courtNumber=1, courtTime= "9:30 - 11:00", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d7c1t3(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(6), courtNumber=1, courtTime= "11:00 - 12:30", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d7c1t4(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(6), courtNumber=1, courtTime= "12:30 - 2:00", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d7c1t5(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(6), courtNumber=1, courtTime= "2:00 - 3:30", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d7c1t6(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(6), courtNumber=1, courtTime= "3:30 - 5:00", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

#court 2
def d7c2t1(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(6), courtNumber=2, courtTime= "8:00 - 9:30", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d7c2t2(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(6), courtNumber=2, courtTime= "9:30 - 11:00", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d7c2t3(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(6), courtNumber=2, courtTime= "11:00 - 12:30", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d7c2t4(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(6), courtNumber=2, courtTime= "12:30 - 2:00", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d7c2t5(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(6), courtNumber=2, courtTime= "2:00 - 3:30", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d7c2t6(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(6), courtNumber=2, courtTime= "3:30 - 5:00", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

#court 3
def d7c3t1(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(6), courtNumber=3, courtTime= "8:00 - 9:30", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d7c3t2(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(6), courtNumber=3, courtTime= "9:30 - 11:00", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d7c3t3(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(6), courtNumber=3, courtTime= "11:00 - 12:30", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d7c3t4(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(6), courtNumber=3, courtTime= "12:30 - 2:00", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d7c3t5(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(6), courtNumber=3, courtTime= "2:00 - 3:30", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d7c3t6(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(6), courtNumber=3, courtTime= "3:30 - 5:00", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

#court 4
def d7c4t1(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(6), courtNumber=4, courtTime= "8:00 - 9:30", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d7c4t2(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(6), courtNumber=4, courtTime= "9:30 - 11:00", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d7c4t3(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(6), courtNumber=4, courtTime= "11:00 - 12:30", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d7c4t4(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(6), courtNumber=4, courtTime= "12:30 - 2:00", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d7c4t5(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(6), courtNumber=4, courtTime= "2:00 - 3:30", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d7c4t6(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(6), courtNumber=4, courtTime= "3:30 - 5:00", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

#court 5
def d7c5t1(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(6), courtNumber=5, courtTime= "8:00 - 9:30", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d7c5t2(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(6), courtNumber=5, courtTime= "9:30 - 11:00", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d7c5t3(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(6), courtNumber=5, courtTime= "11:00 - 12:30", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d7c5t4(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(6), courtNumber=5, courtTime= "12:30 - 2:00", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d7c5t5(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(6), courtNumber=5, courtTime= "2:00 - 3:30", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d7c5t6(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(6), courtNumber=5, courtTime= "3:30 - 5:00", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

#court 6
def d7c6t1(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(6), courtNumber=6, courtTime= "8:00 - 9:30", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d7c6t2(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(6), courtNumber=6, courtTime= "9:30 - 11:00", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d7c6t3(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(6), courtNumber=6, courtTime= "11:00 - 12:30", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d7c6t4(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(6), courtNumber=6, courtTime= "12:30 - 2:00", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d7c6t5(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(6), courtNumber=6, courtTime= "2:00 - 3:30", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d7c6t6(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(6), courtNumber=6, courtTime= "3:30 - 5:00", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

#court 7
def d7c7t1(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(6), courtNumber=7, courtTime= "8:00 - 9:30", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d7c7t2(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(6), courtNumber=7, courtTime= "9:30 - 11:00", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d7c7t3(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(6), courtNumber=7, courtTime= "11:00 - 12:30", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d7c7t4(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(6), courtNumber=7, courtTime= "12:30 - 2:00", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d7c7t5(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(6), courtNumber=7, courtTime= "2:00 - 3:30", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d7c7t6(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(6), courtNumber=7, courtTime= "3:30 - 5:00", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

#court 8
def d7c8t1(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(6), courtNumber=8, courtTime= "8:00 - 9:30", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d7c8t2(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(6), courtNumber=8, courtTime= "9:30 - 11:00", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d7c8t3(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(6), courtNumber=8, courtTime= "11:00 - 12:30", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d7c8t4(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(6), courtNumber=8, courtTime= "12:30 - 2:00", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d7c8t5(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(6), courtNumber=8, courtTime= "2:00 - 3:30", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d7c8t6(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(6), courtNumber=8, courtTime= "3:30 - 5:00", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

#court 9
def d7c9t1(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(6), courtNumber=9, courtTime= "8:00 - 9:30", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d7c9t2(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(6), courtNumber=9, courtTime= "9:30 - 11:00", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d7c9t3(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(6), courtNumber=9, courtTime= "11:00 - 12:30", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d7c9t4(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(6), courtNumber=9, courtTime= "12:30 - 2:00", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d7c9t5(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(6), courtNumber=9, courtTime= "2:00 - 3:30", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d7c9t6(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(6), courtNumber=9, courtTime= "3:30 - 5:00", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

#court 10
def d7c10t1(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(6), courtNumber=10, courtTime= "8:00 - 9:30", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d7c10t2(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(6), courtNumber=10, courtTime= "9:30 - 11:00", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d7c10t3(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(6), courtNumber=10, courtTime= "11:00 - 12:30", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d7c10t4(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(6), courtNumber=10, courtTime= "12:30 - 2:00", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d7c10t5(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(6), courtNumber=10, courtTime= "2:00 - 3:30", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d7c10t6(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(6), courtNumber=10, courtTime= "3:30 - 5:00", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

#court 11
def d7c11t1(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(6), courtNumber=11, courtTime= "8:00 - 9:30", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d7c11t2(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(6), courtNumber=11, courtTime= "9:30 - 11:00", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d7c11t3(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(6), courtNumber=11, courtTime= "11:00 - 12:30", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d7c11t4(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(6), courtNumber=11, courtTime= "12:30 - 2:00", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d7c11t5(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(6), courtNumber=11, courtTime= "2:00 - 3:30", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d7c11t6(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(6), courtNumber=11, courtTime= "3:30 - 5:00", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

#court 12
def d7c12t1(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(6), courtNumber=12, courtTime= "8:00 - 9:30", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d7c12t2(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(6), courtNumber=12, courtTime= "9:30 - 11:00", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d7c12t3(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(6), courtNumber=12, courtTime= "11:00 - 12:30", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d7c12t4(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(6), courtNumber=12, courtTime= "12:30 - 2:00", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d7c12t5(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(6), courtNumber=12, courtTime= "2:00 - 3:30", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)

def d7c12t6(request):
    email = request.user.email
    instance = CustomUser.objects.get(email = email)
    firstname = instance.first_name
    lastname = instance.last_name
    nonmember_guests = 0
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            guest2EMail = form.cleaned_data['guest2EMail']
            guest3EMail = form.cleaned_data['guest3EMail']
            guest4EMail = form.cleaned_data['guest4EMail']
            queryset2 = CustomUser.objects.filter(email=guest2EMail)
            queryset3 = CustomUser.objects.filter(email=guest3EMail)
            queryset4 = CustomUser.objects.filter(email=guest4EMail)

            if not queryset2.exists() and not guest2EMail == '':
                nonmember_guests +=1
            if not queryset3.exists() and not guest3EMail == '':
                nonmember_guests +=1
            if not queryset4.exists() and not guest4EMail == '':
                nonmember_guests +=1
            
            if nonmember_guests > 0:
                request.user.total_due += (nonmember_guests * 10)
                request.user.save()
            form.save()
            return render(request, 'courts/success.html', {})
    prefill= courtReservationForm(courtDate = datetime.now()+timedelta(6), courtNumber=12, courtTime= "3:30 - 5:00", guest1EMail = email, guest1FName = firstname, guest1LName = lastname)
    form = ReservationForm(instance=prefill)
    context = {'form': form}
    return render(request, 'courts/reservationform.html', context)
