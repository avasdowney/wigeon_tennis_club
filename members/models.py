from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    age = models.IntegerField(null=True)
    address = models.CharField(max_length=200, null=True)
    phone = models.IntegerField(null=True)
    is_public = models.BooleanField(default=False)
    did_pay = models.BooleanField(default=False)