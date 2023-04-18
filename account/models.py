from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class Bill(models.Model):
    firstName = models.CharField(max_length= 30, blank = False)
    lastName = models.CharField(max_length=30, blank=False)
    creditCardNumber = models.IntegerField(validators=[MinValueValidator(1000000000000000), MaxValueValidator(9999999999999999)], blank = False)
    cardExpDate = models.DateField()
    cvv = models.IntegerField(validators = [MinValueValidator(100), MaxValueValidator(999)], blank=False)
    zipCode = models.IntegerField(validators = [MinValueValidator(10000), MaxValueValidator(99999)], blank = False)
    total_due = models.DecimalField(default=0.00, decimal_places=2, max_digits=9999)
    # amountCharge = models.DecimalField(decimal_places = 2, max_digits = 6, blank=False)


