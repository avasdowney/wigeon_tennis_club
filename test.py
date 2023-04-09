# admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    list_display = (
            'username', 'email', 'first_name', 'last_name', 'age',
            'phone', ' address', 'is_public', 'did_pay', 'is_staff'
            )

    fieldsets = (
        (None, {
            'fields': ('username', 'password')
        }),
        ('Personal info', {
            'fields': ('first_name', 'last_name', 'email', 'phone', 'address', 'age')
        }),
        ('Permissions', {
            'fields': (
                'is_active', 'is_staff', 'is_superuser',
                'groups', 'user_permissions'
                )
        }),
        ('Important dates', {
            'fields': ('last_login', 'date_joined')
        }),
        ('Flags', {
            'fields': ('is_public', 'did_pay')
        })
    )

    add_fieldsets = (
        (None, {
            'fields': ('username', 'password')
        }),
        ('Personal info', {
            'fields': ('first_name', 'last_name', 'email', 'phone', 'address', 'age')
        }),
        ('Permissions', {
            'fields': (
                'is_active', 'is_staff', 'is_superuser',
                'groups', 'user_permissions'
                )
        }),
        ('Important dates', {
            'fields': ('last_login', 'date_joined')
        }),
        ('Flags', {
            'fields': ('is_public', 'did_pay')
        })
    )

admin.site.register(CustomUser, CustomUserAdmin)





# models.py

from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    age = models.IntegerField(blank=True)
    address = models.CharField(max_length=200, blank=True)
    phone = models.IntegerField(blank=True)
    is_public = models.BooleanField(default=False)
    did_pay = models.BooleanField(default=False)




# views.py

from .forms import SignUpForm
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def update_user_data(user):
    Profile.objects.update_or_create(user=user, defaults={'phone': user.profile.mob},)

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()

            user.profile.mob = form.cleaned_data.get('phone')
            update_user_data(user)  

            # load the profile instance created by the signal
            user.save()
            raw_password = form.cleaned_data.get('password1')

            # login user after signing up
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)

            # redirect user to home page
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def index(request):
    template = loader.get_template('signup.html')
    return HttpResponse(template.render())




# forms.py

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
 
class SignUpForm(UserCreationForm):
    phone = forms.IntegerField()
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'phone', 'username', 'password1', 'password2', )



# signup.html

{% load static %}
{% load custom_tags %}
<link rel="stylesheet" type="text/css" href="{% static 'members/styles.css' %}">

<h2>Sign up</h2>
<form method="post">
    {% csrf_token %}
    {% for field in form %}
        <p>
            {{ field.label_tag }}<br>
            {{ field }}
            {% if field.help_text %}
                <small style="color: grey">{{ field.help_text }}</small>
            {% endif %}
            {% for error in field.errors %}
                <p style="color: red">{{ error }}</p>
            {% endfor %}
        </p>
    {% endfor %}
    <button type="submit">Sign up</button>
</form>