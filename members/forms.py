from django.contrib.auth.forms import UserCreationForm
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
    age = forms.IntegerField()
    phone = forms.CharField(max_length=11)
    address = forms.CharField(max_length=100)
    did_pay = forms.ChoiceField(label="How would you like to pay?", choices=did_pay_choices)
    is_public = forms.ChoiceField(label="Would you like to join the Wigeon Tennis Club member directory?", choices=is_public_choices)
    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'age', 'phone', 'address', 'email', 'username', 'password1', 'password2', 'did_pay', 'is_public')