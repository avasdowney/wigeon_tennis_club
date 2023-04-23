from django.test import TestCase
from django.urls import reverse
from members.models import CustomUser
from django.contrib.auth import get_user
from .models import Bill

# Create your tests here.
class AccountHomepageTests(TestCase):
    def test_account_url_exists_at_correct_location(self):
         response = self.client.get("/account")
         self.assertEqual(response.status_code, 301) 

class MemberAccountInfo(TestCase):
    def setUp(self):
        # define a typical member
        self.user = CustomUser.objects.create_user(
            first_name='test2', 
            last_name='user2', 
            age=66, 
            phone=1234567890, 
            address='123 street road city', 
            email='test2user2@gmail.com', 
            username='test2_user2', 
            password='password123', 
            is_public=True, 
            pay_online=True
            )
        # define treasurer superuser
        self.treasurer = CustomUser.objects.create_user(
            first_name='treasurer', 
            last_name='tennisclub', 
            age=65, 
            phone=1234567890, 
            address='123 street road city', 
            email='treasurer@email.com', 
            username='treasurer', 
            password='pbkdf2_sha256$390000$OCcGBVKYajVeZruB1fdoy[42 chars]G0w=',
            is_public=True, 
            pay_online=True
            )
        # define admin superuser
        self.admin = CustomUser.objects.create_user(
            first_name='admin', 
            last_name='tennisclub', 
            age=12, 
            phone=1234567890, 
            address='123 street road city', 
            email='admin@email.com', 
            username='admin', 
            password='password', 
            is_public=True, 
            pay_online=True
            )
            
    def test_account_user_info(self):
            self.assertEqual(self.user.first_name, 'test2')
            self.assertEqual(self.user.last_name, 'user2')
            self.assertEqual(self.user.age, 66)
            self.assertEqual(self.user.phone, 1234567890)
            self.assertEqual(self.user.address, '123 street road city')
            self.assertEqual(self.user.email, 'test2user2@gmail.com')
            self.assertEqual(self.user.username, 'test2_user2')
            self.assertEqual(self.user.is_public, True)
            self.assertEqual(self.user.pay_online, True)

    def test_treasurer_login_and_correct_user_profile(self):
        self.assertFalse(get_user(self.client).is_active)
        self.client.login(username='treasurer', password='pbkdf2_sha256$390000$OCcGBVKYajVeZruB1fdoy[42 chars]G0w=')
        self.assertTrue(get_user(self.client).is_active)
        self.client.get("account/treasurerProfile.html")

    def test_admin_login_and_correct_user_profile(self):
        self.assertFalse(get_user(self.client).is_active)
        self.client.login(username='admin', password='password')
        self.assertTrue(get_user(self.client).is_active)
        self.client.get("account/adminProfile.html")

    def test_admin_profile_template_name_used(self):  
        response = self.client.get("account")
        self.assertTemplateNotUsed(response, "account/adminProfile.html")

    def test_treasurer_profile_template_name_used(self):  
        response = self.client.get("account")
        self.assertTemplateNotUsed(response, "account/treasurerProfile.html")

class AddBillTest(TestCase):
     def create_bill(self, 
        firstName="Test", 
        lastName="Bill", 
        creditCardNumber=1234567890123456, 
        cardExpDate='2025-05-5',
        cvv=666, 
        zipCode=12345, 
        total_due=100):
        return Bill.objects.create(firstName=firstName, lastName=lastName, creditCardNumber=creditCardNumber, cardExpDate=cardExpDate, cvv=cvv, zipCode=zipCode, total_due=total_due)

     def test_bills_first_name(self):
        bills = self.create_bill()
        self.assertTrue(isinstance(bills, Bill))
        self.assertEqual("Test", bills.firstName)

     def test_bills_card_number(self):
        bills = self.create_bill()
        self.assertTrue(isinstance(bills, Bill))
        self.assertEqual(1234567890123456, bills.creditCardNumber)

