from django.db import models

# Create your models here.

account_standing_choices=(
       ("GS", "Good Standing"),
       ("FD", "Fees Due"),
       ("FOD", "Fees Overdue"),
    )

class Member(models.Model):
    email_address = models.CharField(max_length=100, primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=10)
    address = models.CharField(max_length=100)
    age = models.IntegerField()
    member_id = models.IntegerField()
    account_standing = models.CharField(
        max_length = 20,
        choices = account_standing_choices
        )

class New(models.Model):
    text_content = models.TextField()
    image = models.ImageField()

    

 

