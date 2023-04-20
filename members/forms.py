from django.contrib.auth.forms import UserCreationForm
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