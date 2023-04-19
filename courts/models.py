from django.db import models

# Create your models here.

courtNumber =(
    (1, 'Court 1'),
    (2, 'Court 2'),
    (3, 'Court 3'),
    (4, 'Court 4'),
    (5, 'Court 5'),
    (6, 'Court 6'),
    (7, 'Court 7'),
    (8, 'Court 8'),
    (9, 'Court 9'),
    (10, 'Court 10'),
    (11, 'Court 11'),
    (12, 'Court 12'),
)
timeBlocks=(
       ("8:00 - 9:30", "8:00 - 9:30"),
       ("9:30 - 11:00", "9:30 - 11:00"),
       ("11:00 - 12:30", "11:00 - 12:30"),
       ("12:30 - 2:00", "12:30 - 2:00"),
       ("2:00 - 3:30", "2:00 - 3:30"),
       ("3:30 - 5:00", "3:30 - 5:00"),
    )

class courtReservationForm(models.Model):
    courtDate = models.DateField()
    courtNumber = models.IntegerField(
        choices = courtNumber,
        blank = False,
    )
    courtTime = models.CharField(
        max_length = 20,
        choices = timeBlocks,
        blank = False,
    )
    guest1EMail = models.EmailField(max_length=254, blank = True)
    guest1FName = models.CharField(max_length=100, blank = True)
    guest1LName = models.CharField(max_length=100, blank = True)
    guest2EMail = models.EmailField(max_length=254, blank = True)
    guest2FName = models.CharField(max_length=100, blank = True)
    guest2LName = models.CharField(max_length=100, blank = True)
    guest3EMail = models.EmailField(max_length=254, blank = True)
    guest3FName = models.CharField(max_length=100, blank = True)
    guest3LName = models.CharField(max_length=100, blank = True)
    guest4EMail = models.EmailField(max_length=254, blank = True)
    guest4FName = models.CharField(max_length=100, blank = True)
    guest4LName = models.CharField(max_length=100, blank = True)
