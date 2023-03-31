from django.forms import ModelForm
from .models import courtReservationForm


class ReservationForm(ModelForm):
    class Meta:
        model = courtReservationForm
        fields = '__all__'
