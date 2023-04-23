from django.forms import ModelForm
from .models import *

class ReservationForm(ModelForm):
    class Meta:
        model = courtReservationForm
        fields = '__all__'
        labels = {
            'courtDate' : ('Date YYYY-MM-DD'),
            'courtNumber' : ('Court Number'),
            "courtTime" : ('Time'),
            'guest1EMail' : ("Guest 1's Email Address"),
            'guest1FName': ("Guest 1's First Name"),
            'guest1LName': ("Guest 1's Last Name"),
            'guest2EMail' :("Guest 2's Email Address"),
            'guest2FName' : ("Guest 2's First Name"),
            'guest2LName': ("Guest 2's Last Name"),
            'guest3EMail' : ("Guest 3's Email Address"),
            'guest3FName' : ("Guest 3's First Name"),
            'guest3LName': ("Guest 3's Last Name"),
            'guest4EMail' : ("Guest 4's Email Address"),
            'guest4FName' : ("Guest 4's First Name"),
            'guest4LName': ("Guest 4's Last Name")
        }

