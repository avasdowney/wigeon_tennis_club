from django.forms import ModelForm
from .models import *
from django.core.exceptions import ValidationError

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

class TournamentForm(ModelForm):
    class Meta:
        model = tournamentForm
        fields = '__all__'
        labels={
            'tournyTime' : ("Tournament Time"),
            'tournyDate' : ("Tournament Date YYY-MM-DD"),
            'team1' : ("Team 1's Name"),
            'team2' : ("Team 2's Name"),
            'court1' : ("Court for Double's Match 1 "),
            'court2' : ("Court for Double's Match 2 "),
            'court3' : ("Court for Double's Match 3 "),
            'court4' : ("Court for Single's Match 1 "),
            'court5' : ("Court for Single's Match 2 ")

        } 
