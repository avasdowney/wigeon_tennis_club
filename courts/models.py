from django.db import models

# Create your models here.

class courtReservationForm(models.Model):
    guest1EMail = models.EmailField(max_length=254)
    guest1FName = models.CharField(max_length=100)
    guest1LName = models.CharField(max_length=100)
    guest2EMail = models.EmailField(max_length=254)
    guest2FName = models.CharField(max_length=100)
    guest2LName = models.CharField(max_length=100)
    guest3EMail = models.EmailField(max_length=254)
    guest3FName = models.CharField(max_length=100)
    guest3LName = models.CharField(max_length=100)