from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator

class CustomUser(AbstractUser):
    first_name = models.CharField(max_length=100, null=True)
    last_name = models.CharField(max_length=100, null=True)
    age = models.IntegerField(null=True)
    email = models.CharField(max_length=200, null=True)
    address = models.CharField(max_length=200, null=True)
    phone = models.IntegerField(null=True)
    is_public = models.BooleanField(default=False)
    pay_online = models.BooleanField(default=True)
    did_pay = models.BooleanField(default=False)
    total_due = models.DecimalField(default=0.00, decimal_places=2, max_digits=9999)
    renewal = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if self.age < 18 and self.did_pay == False and self.renewal == True:
            self.total_due = 250.00
        elif self.age >=18 and self.age < 65 and self.did_pay == False and self.renewal == True:
            self.total_due = 400.00
        elif self.age >= 65 and self.did_pay == False and self.renewal == True:
            self.total_due = 300.00
        super(CustomUser, self).save(*args, **kwargs)



class Bill(models.Model):
    firstName = models.CharField(max_length= 30, blank = False)
    lastName = models.CharField(max_length=30, blank=False)
    creditCardNumber = models.IntegerField(blank = False, null=True) #validators=[MinValueValidator(1000000000000000), MaxValueValidator(9999999999999999)]
    cardExpDate = models.DateField(null=True)
    cvv = models.IntegerField(validators = [MinValueValidator(100), MaxValueValidator(999)], blank=False, null=True)
    zipCode = models.IntegerField(validators = [MinValueValidator(10000), MaxValueValidator(99999)], blank = False, null=True)

