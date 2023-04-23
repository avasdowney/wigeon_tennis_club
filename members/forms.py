from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from django.core.validators import MinValueValidator, MaxValueValidator
from django import forms
from .models import CustomUser

did_pay_choices=(
       ("True", "Pay Online"),
       ("False", "Pay in Person"),
    )

is_public_choices=(
       ("True", "Add myself to club directory"),
       ("False", "Keep my info private")
    )
 
class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=100, required=True)
    last_name = forms.CharField(max_length=100, required=True)
    age = forms.IntegerField(required=True)
    email = forms.EmailField(required=True)
    phone = forms.IntegerField(validators = [MinValueValidator(1000000000), MaxValueValidator(9999999999)], required=True)
    address = forms.CharField(max_length=100, required=True)
    pay_online = forms.ChoiceField(label="How would you like to pay?", choices=did_pay_choices, required=True)
    is_public = forms.ChoiceField(label="Would you like to join the Wigeon Tennis Club member directory?", choices=is_public_choices, required=True)
    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'age', 'phone', 'address', 'email', 'username', 'password1', 'password2', 'pay_online', 'is_public')



class BillingForm(ModelForm):
    first_name = forms.CharField(max_length=100, required=True)
    last_name = forms.CharField(max_length=100, required=True)
    credit_card_number = forms.IntegerField(required=True) #validators=[MinValueValidator(1000000000000000), MaxValueValidator(9999999999999999)],
    card_exp_date = forms.DateField(required=True)
    cvv = forms.IntegerField(validators = [MinValueValidator(100), MaxValueValidator(999)], required=True)
    zip_code = forms.IntegerField(required=True) #validators = [MinValueValidator(10000), MaxValueValidator(99999)],

    class Meta:
        model = CustomUser
        fields = 'first_name', 'last_name', 'credit_card_number', 'card_exp_date', 'cvv', 'zip_code'
        labels = {
            'first_name' : ("First Name"),
            'last_name' : ("Last Name"),
            'credit_card_number' : ('Card Number'),
            'card_exp_date' : ('Expiration Date'),
            'cvv' : ('Security Code'),
            'zip_code' : ("Zip Code"),
        }
