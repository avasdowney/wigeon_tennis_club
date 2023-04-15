from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    age = models.IntegerField(null=True)
    address = models.CharField(max_length=200, null=True)
    phone = models.IntegerField(null=True)
    is_public = models.BooleanField(default=False)
    did_pay = models.BooleanField(default=False)
    total_due = models.DecimalField(default=0.00, decimal_places=2, max_digits=9999)

    def save(self, *args, **kwargs):
            if self.age < 18:
                self.total_due = 250.00
            elif self.age >=18 and self.age < 65:
                self.total_due = 400.00
            elif self.age >= 65:
                self.total_due = 300.00
            super(CustomUser, self).save(*args, **kwargs)

    def base(request):
        # grab all users from database:
        all_stories = CustomUser.objects.all()
        return render(request, 'directory.html', 
            {
            'age': age, 
            'address': address,
            'phone': phone,
            })
