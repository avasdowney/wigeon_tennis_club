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
    payment_flag = models.BooleanField(default=True)
    total_due = models.DecimalField(default=1000.00, decimal_places=2, max_digits=9999)
    renewal = models.BooleanField(default=False)
    credit_card_number = models.IntegerField(validators=[MinValueValidator(1000000000000000), MaxValueValidator(9999999999999999)], null=True)
    card_exp_date = models.DateField(null=True)
    cvv = models.IntegerField(validators = [MinValueValidator(100), MaxValueValidator(999)], blank=False, null=True)
    zip_code = models.IntegerField(validators = [MinValueValidator(1000), MaxValueValidator(99999)], blank = False, null=True)

    def save(self, *args, **kwargs):
        if self.age is not None:
            if (self.age < 18) and self.renewal == True:
                self.total_due = 250.00
                self.renewal = False
            elif (self.age >=18) and (self.age < 65) and self.renewal == True:
                self.total_due = 400.00
                self.renewal = False
            elif (self.age >= 65) and self.renewal == True:
                self.total_due = 300.00
                self.renewal = False

        if CustomUser.objects.filter(username=self.username).exists() == False:
            super(CustomUser, self).save(*args, **kwargs)
        else:
            CustomUser.objects.filter(pk=self.pk).update(total_due=self.total_due, payment_flag=self.payment_flag) 