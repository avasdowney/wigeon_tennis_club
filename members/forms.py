from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms

def update_user_data(user):
    Profile.objects.update_or_create(user=user, defaults={'phone': user.profile.phone},)
 
class SignUpForm(UserCreationForm):
    phone = forms.IntegerField()
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'phone', 'username', 'password1', 'password2', )
        labels = {'phone': 'Mobile Number',}