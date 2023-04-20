from django.test import TestCase, SimpleTestCase
from django.urls import reverse 
from django.conf import settings
from .models import courtReservationForm

# Create your tests here.

class CourtMenuTests(SimpleTestCase):
    
    def test_court_menu1_url_exists_at_correct_location(self):
        response = self.client.get("/courts")
        self.assertEqual(response.status_code, 301)
        
class CourtReservationFormTests(TestCase):

    def setUp(self):
        self.courtDetails = courtReservationForm.objects.create(
        courtDate = "1990-01-01", courtNumber = "12", courtTime = "3:30 - 5:00")

        self.singleReservation = courtReservationForm.objects.create(
        courtDate = "1990-01-01", courtNumber = "1", courtTime = "11:00 - 12:30",
        guest1EMail = 'test1@gmail.com', guest1FName = 'test', guest1LName = 'one')

        self.fullCourtReservation = courtReservationForm.objects.create(
        courtDate = "2021-03-15", courtNumber = "8", courtTime = "2:00 - 3:30",
        guest1EMail = 'test1@gmail.com', guest1FName = 'test', guest1LName = 'one',
        guest2EMail = 'test2@gmail.com', guest2FName = 'test', guest2LName = 'two',
        guest3EMail = 'test3@gmail.com', guest3FName = 'test', guest3LName = 'three',
        guest4EMail = 'test4@gmail.com', guest4FName = 'test', guest4LName = 'four'
        )

        self.faultyReservation = courtReservationForm.objects.create(
            courtDate = "1900-01-01", courtNumber = '0', courtTime = "10:00 - 10:00",
            guest1EMail = "testatgmaildotcom", guest1FName = 'Adam', guest1LName = 'Adam'
        )

    def testCourtDetails(self):
        self.assertEqual(self.courtDetails.courtDate, "1990-01-01")
        self.assertEqual(self.courtDetails.courtNumber, "12")
        self.assertEqual(self.courtDetails.courtTime, "3:30 - 5:00")

    def testSingleReservation(self):
        self.assertEqual(self.singleReservation.courtDate, "1990-01-01")
        self.assertEqual(self.singleReservation.courtNumber, "1")
        self.assertEqual(self.singleReservation.courtTime, "11:00 - 12:30")
        self.assertEqual(self.singleReservation.guest1EMail, "test1@gmail.com")
        self.assertEqual(self.singleReservation.guest1FName, 'test')
        self.assertEqual(self.singleReservation.guest1LName, 'one')

    def testFullCourtReservation(self):
        self.assertEqual(self.fullCourtReservation.courtDate, "2021-03-15")
        self.assertEqual(self.fullCourtReservation.courtNumber, "8")
        self.assertEqual(self.fullCourtReservation.courtTime, "2:00 - 3:30")
        self.assertEqual(self.fullCourtReservation.guest1EMail, "test1@gmail.com")
        self.assertEqual(self.fullCourtReservation.guest1FName, 'test')
        self.assertEqual(self.fullCourtReservation.guest1LName, 'one')
        self.assertEqual(self.fullCourtReservation.guest2EMail, "test2@gmail.com")
        self.assertEqual(self.fullCourtReservation.guest2FName, 'test')
        self.assertEqual(self.fullCourtReservation.guest2LName, 'two')
        self.assertEqual(self.fullCourtReservation.guest3EMail, "test3@gmail.com")
        self.assertEqual(self.fullCourtReservation.guest3FName, 'test')
        self.assertEqual(self.fullCourtReservation.guest3LName, 'three')
        self.assertEqual(self.fullCourtReservation.guest4EMail, "test4@gmail.com")
        self.assertEqual(self.fullCourtReservation.guest4FName, 'test')
        self.assertEqual(self.fullCourtReservation.guest4LName, 'four')

    def testFaultyEmail(self):
        self.assertFalse(self.faultyReservation.guest1EMail == 'test1@email.com')
    
    def testFaultyCourtNumber(self):
        self.assertFalse(int(self.faultyReservation.courtNumber) > 0 and int(self.faultyReservation.courtNumber) < 13)