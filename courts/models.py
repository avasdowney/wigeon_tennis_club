from django.db import models

# Create your models here.

class courtReservationForm(models.Model):
    guest1EMail = models.EmailField(max_length=254, blank = True)
    guest1FName = models.CharField(max_length=100, blank = True)
    guest1LName = models.CharField(max_length=100, blank = True)
    guest2EMail = models.EmailField(max_length=254, blank = True)
    guest2FName = models.CharField(max_length=100, blank = True)
    guest2LName = models.CharField(max_length=100, blank = True)
    guest3EMail = models.EmailField(max_length=254, blank = True)
    guest3FName = models.CharField(max_length=100, blank = True)
    guest3LName = models.CharField(max_length=100, blank = True)