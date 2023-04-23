from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    list_display = (
            'username', 'email', 'first_name', 'last_name', 'age',
            'phone', 'address', 'zip_code', 'total_due', 'credit_card_number', 'card_exp_date', 
            'cvv', 'pay_online', 'is_public', 'did_pay', 'renewal', 'is_staff'
            )

    fieldsets = (
        (None, {
            'fields': ('username', 'password')
        }),
        ('Personal info', {
            'fields': ('first_name', 'last_name', 'email', 'phone', 'address', 'zip_code', 'age', 
            'total_due', 'credit_card_number', 'card_exp_date', 'cvv')
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
            'fields': ('is_public', 'did_pay', 'renewal')
        })
    )

    add_fieldsets = (
        (None, {
            'fields': ('username', 'password')
        }),
        ('Personal info', {
            'fields': ('first_name', 'last_name', 'email', 'phone', 'address', 'zip_code', 'age', 
            'total_due', 'credit_card_number', 'card_exp_date', 'cvv')
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
            'fields': ('is_public', 'did_pay', 'renewal')
        })
    )

admin.site.register(CustomUser, CustomUserAdmin)