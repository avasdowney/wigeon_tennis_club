from django.forms import ModelForm
from .models import Bill

class BillingForm(ModelForm):
    class Meta:
        model = Bill
        fields = '__all__'
        labels = {
            'firstName' : ("First Name"),
            'lastName' : ("Last Name"),
            'creditCardNumber' : ('Card Number'),
            'cardExpDate' : ('Expiration Date'),
            'cvv' : ('Security Code'),
            'zipCode' : ("Zip Code"),
            'amountCharge' : ("Amount to be Charged")
        }
