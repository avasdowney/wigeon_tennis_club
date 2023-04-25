from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from django.core.validators import MinValueValidator, MaxValueValidator
from django import forms
from .models import CustomUser

payment_flag_choices=(
       ("False", "Pay Online"),
       ("True", "Pay in Person"),
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
    payment_flag = forms.ChoiceField(label="How would you like to pay?", choices=payment_flag_choices, required=True)
    is_public = forms.ChoiceField(label="Would you like to join the Wigeon Tennis Club member directory?", choices=is_public_choices, required=True)
    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'age', 'phone', 'address', 'email', 'username', 'password1', 'password2', 'payment_flag', 'is_public')



class BillingForm(ModelForm):
    first_name = forms.CharField(max_length=100, required=True)
    last_name = forms.CharField(max_length=100, required=True)
    credit_card_number = forms.IntegerField(validators=[MinValueValidator(1000000000000000), MaxValueValidator(9999999999999999)], required=True)
    card_exp_date = forms.DateField(required=True)
    cvv = forms.IntegerField(validators = [MinValueValidator(100), MaxValueValidator(999)], required=True)
    zip_code = forms.IntegerField(validators = [MinValueValidator(1000), MaxValueValidator(99999)], required=True) 

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