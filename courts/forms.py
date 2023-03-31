from django.forms import ModelForm
from .models import courtReservationForm


class ReservationForm(ModelForm):
    class Meta:
        model = courtReservationForm
        fields = '__all__'
        labels = {
            'guest1EMail' : ("Guest 1's Email Address"),
            'guest1FName': ("Guest 1's First Name"),
            'guest1LName': ("Guest 1's Last Name"),
            'guest2EMail' :("Guest 2's Email Address"),
            'guest2FName' : ("Guest 2's First Name"),
            'guest2LName': ("Guest 1's Last Name"),
            'guest3EMail' : ("Guest 3's Email Address"),
            'guest3FName' : ("Guest 3's First Name"),
            'guest3LName': ("Guest 3's Last Name")
        }
