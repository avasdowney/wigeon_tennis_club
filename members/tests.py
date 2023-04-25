from django.test import TestCase, SimpleTestCase
from django.urls import reverse 
from django.conf import settings
from django.contrib.auth import get_user
from django.contrib.auth.models import User, Permission, Group
from .models import CustomUser
from .forms import SignUpForm, BillingForm

# test to ensure all pages load as expected
class MembersHomepageTests(SimpleTestCase):

    def test_members_url_exists_at_correct_location(self):
        response = self.client.get("/members")
        self.assertEqual(response.status_code, 301)

    def test_directory_template_name_correct(self):  
        response = self.client.get(reverse("members:directory"))
        self.assertTemplateUsed(response, "members/directory.html")

    def test_signup_template_name_correct(self):  
        response = self.client.get(reverse("members:signup"))
        self.assertTemplateUsed(response, "signup.html")


# test to ensure all member info is stored/used as expected
class MemberInfoTest(TestCase):

    def setUp(self):
        # define all types of users
        self.user = CustomUser.objects.create_user(
            first_name='test', 
            last_name='user', 
            age=25, 
            phone=1234567890, 
            address='123 street road city', 
            email='testuser@email.com', 
            username='test_user', 
            password='top_secret', 
            is_public=True, 
            pay_online=True
            )

        self.child = CustomUser.objects.create_user(
            first_name='test2', 
            last_name='user2', 
            age=2, 
            phone=1234567990, 
            address='123 street road city', 
            email='testuser2@email.com', 
            username='test_user2', 
            password='top_secret', 
            is_public=True, 
            pay_online=True
            )

        self.senior = CustomUser.objects.create_user(
            first_name='test3', 
            last_name='user3', 
            age=85, 
            phone=1235567890, 
            address='123 street road city', 
            email='testuser3@email.com', 
            username='test_user3', 
            password='top_secret', 
            is_public=True, 
            pay_online=True
            )
        
        # for admin testing
        self.group = Group(name="admin")
        self.group.save()

    def test_user_creation(self):
        self.assertFalse(get_user(self.client).is_authenticated)
        self.client.login(username='test_user', password='top_secret')
        self.assertTrue(get_user(self.client).is_authenticated)

    def test_user_info(self):
        self.assertEqual(self.user.first_name, 'test')
        self.assertEqual(self.user.last_name, 'user')
        self.assertEqual(self.user.age, 25)
        self.assertEqual(self.user.phone, 1234567890)
        self.assertEqual(self.user.address, '123 street road city')
        self.assertEqual(self.user.email, 'testuser@email.com')
        self.assertEqual(self.user.username, 'test_user')
        self.assertEqual(self.user.is_public, True)
        self.assertEqual(self.user.pay_online, True)

    def test_initiation_fees(self):
        self.assertEqual(self.user.total_due, 1000)
        self.assertEqual(self.child.total_due, 1000)
        self.assertEqual(self.senior.total_due, 1000)

    def test_pay_bills(self):
        self.user.total_due = 0
        self.user.save()
        form = BillingForm(data={'first_name' : 'test',
                                 'last_name' : 'user',
                                 'credit_card_number' : 1234567890123456,
                                 'card_exp_date' : '12-01-2025',
                                 'cvv' : 666,
                                 'zip_code' : 12317,
        })
        self.assertEqual(self.user.total_due, 0)

# test to ensure all signup works as expected
class SignupTest(TestCase):    

    def test_signup_form_password_valid(self):
        form = SignUpForm(data={'first_name' : 'test', 
                                'last_name' : 'user', 
                                'age' : 25,
                                'phone' : 1234567890, 
                                'address' : '123 street road city', 
                                'email' : 'testuser@email.com', 
                                'username' : 'test_user', 
                                'password1' : 'Top_secret123!',
                                'password2' : 'Top_secret123!',
                                'is_public' : True, 
                                'payment_flag' : False
        })

        self.assertTrue(form.is_valid())

    def test_signup_form_password_invalid(self):
        form = SignUpForm(data={'first_name' : 'test', 
                                'last_name' : 'user', 
                                'age' : 25,
                                'phone' : 1234567890, 
                                'address' : '123 street road city', 
                                'email' : 'testuser@email.com', 
                                'username' : 'test_user', 
                                'password1' : 'password',
                                'password2' : 'password',
                                'is_public' : True, 
                                'payment_flag' : False
        })
        form2 = SignUpForm(data={'first_name' : 'test', 
                                'last_name' : 'user', 
                                'age' : 25,
                                'phone' : 1234567890, 
                                'address' : '123 street road city', 
                                'email' : 'testuser@email.com', 
                                'username' : 'test_user', 
                                'password1' : 'Top_secret123!',
                                'password2' : 'password!',
                                'is_public' : True, 
                                'payment_flag' : False
        })

        self.assertFalse(form.is_valid())
        self.assertFalse(form2.is_valid())

    def test_signup_form_incomplete(self):
        form = SignUpForm(data={'last_name' : 'user', 
                                'phone' : 1234567890, 
                                'address' : '123 street road city',  
                                'email' : 'testuser@email.com', 
                                'username' : 'test_user', 
                                'password1' : 'Top_secret123!',
                                'password2' : 'Top_secret123!',
                                'is_public' : True, 
                                'payment_flag' : False
        })
        self.assertFalse(form.is_valid())

        form2 = SignUpForm(data={'first_name' : 'test', 
                                'phone' : 1234567890, 
                                'address' : '123 street road city',  
                                'email' : 'testuser@email.com', 
                                'username' : 'test_user', 
                                'password1' : 'Top_secret123!',
                                'password2' : 'Top_secret123!',
                                'is_public' : True, 
                                'payment_flag' : False
        })
        self.assertFalse(form2.is_valid())

        form3 = SignUpForm(data={'first_name' : 'test',
                                'last_name' : 'user', 
                                'address' : '123 street road city',  
                                'email' : 'testuser@email.com', 
                                'username' : 'test_user', 
                                'password1' : 'Top_secret123!',
                                'password2' : 'Top_secret123!',
                                'is_public' : True, 
                                'payment_flag' : False
        })
        self.assertFalse(form3.is_valid())

        form4 = SignUpForm(data={'first_name' : 'test',
                                'last_name' : 'user', 
                                'phone' : 1234567890,   
                                'email' : 'testuser@email.com', 
                                'username' : 'test_user', 
                                'password1' : 'Top_secret123!',
                                'password2' : 'Top_secret123!',
                                'is_public' : True, 
                                'payment_flag' : False
        })
        self.assertFalse(form4.is_valid())

        form5 = SignUpForm(data={'first_name' : 'test',
                                'last_name' : 'user', 
                                'phone' : 1234567890, 
                                'address' : '123 street road city',  
                                'username' : 'test_user', 
                                'password1' : 'Top_secret123!',
                                'password2' : 'Top_secret123!',
                                'is_public' : True, 
                                'payment_flag' : False
        })
        self.assertFalse(form5.is_valid())

        form6 = SignUpForm(data={'first_name' : 'test',
                                'last_name' : 'user', 
                                'phone' : 1234567890, 
                                'address' : '123 street road city',  
                                'email' : 'testuser@email.com', 
                                'password1' : 'Top_secret123!',
                                'password2' : 'Top_secret123!',
                                'is_public' : True, 
                                'payment_flag' : False
        })
        self.assertFalse(form6.is_valid())

        form7 = SignUpForm(data={'first_name' : 'test',
                                'last_name' : 'user', 
                                'phone' : 1234567890, 
                                'address' : '123 street road city',  
                                'email' : 'testuser@email.com', 
                                'username' : 'test_user', 
                                'password1' : 'Top_secret123!',
                                'password2' : 'Top_secret123!',
                                'payment_flag' : False
        })
        self.assertFalse(form7.is_valid())

        form8 = SignUpForm(data={'first_name' : 'test',
                                'last_name' : 'user', 
                                'phone' : 1234567890, 
                                'address' : '123 street road city',  
                                'email' : 'testuser@email.com', 
                                'username' : 'test_user', 
                                'password1' : 'Top_secret123!',
                                'password2' : 'Top_secret123!',
                                'is_public' : True, 
        })
        self.assertFalse(form8.is_valid())

    def test_signup_form_age_invalid(self):
        form = SignUpForm(data={'first_name' : 'test', 
                                'last_name' : 'user', 
                                'age' : 'abc',
                                'phone' : 1234567890, 
                                'address' : '123 street road city', 
                                'email' : 'testuser@email.com', 
                                'username' : 'test_user', 
                                'password1' : 'Top_secret123!',
                                'password2' : 'Top_secret123!',
                                'is_public' : True, 
                                'payment_flag' : False
        })

        self.assertFalse(form.is_valid())

    def test_signup_form_phone_invalid(self):
        form = SignUpForm(data={'first_name' : 'test', 
                                'last_name' : 'user', 
                                'age' : 25,
                                'phone' : 12345678901234567, 
                                'address' : '123 street road city', 
                                'email' : 'testuser@email.com', 
                                'username' : 'test_user', 
                                'password1' : 'Top_secret123!',
                                'password2' : 'Top_secret123!',
                                'is_public' : True, 
                                'payment_flag' : False
        })
        self.assertFalse(form.is_valid())

        form2 = SignUpForm(data={'first_name' : 'test', 
                                'last_name' : 'user', 
                                'age' : 25,
                                'phone' : "abc", 
                                'address' : '123 street road city', 
                                'email' : 'testuser@email.com', 
                                'username' : 'test_user', 
                                'password1' : 'Top_secret123!',
                                'password2' : 'Top_secret123!',
                                'is_public' : True, 
                                'payment_flag' : False
        })
        self.assertFalse(form2.is_valid())

        form3 = SignUpForm(data={'first_name' : 'test', 
                                'last_name' : 'user', 
                                'age' : 25,
                                'phone' : 1234, 
                                'address' : '123 street road city', 
                                'email' : 'testuser@email.com', 
                                'username' : 'test_user', 
                                'password1' : 'Top_secret123!',
                                'password2' : 'Top_secret123!',
                                'is_public' : True, 
                                'payment_flag' : False
        })
        self.assertFalse(form3.is_valid())

class AddBillTest(TestCase):
     def create_bill(self, 
        first_name="Test", 
        last_name="Bill", 
        credit_card_number=1234567890123456, 
        card_exp_date='2025-05-5',
        cvv=666, 
        zip_code=12345, 
        total_due=100):
        return CustomUser.objects.create(first_name=first_name, last_name=last_name, credit_card_number=credit_card_number, card_exp_date=card_exp_date, cvv=cvv, zip_code=zip_code, total_due=total_due)

     def test_bills_first_name(self):
        bills = self.create_bill()
        self.assertTrue(isinstance(bills, CustomUser))
        self.assertEqual("Test", bills.first_name)

     def test_bills_card_number(self):
        bills = self.create_bill()
        self.assertTrue(isinstance(bills, CustomUser))
        self.assertEqual(1234567890123456, bills.credit_card_number)