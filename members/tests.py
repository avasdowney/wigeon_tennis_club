from django.test import TestCase, SimpleTestCase
from django.urls import reverse 
from django.conf import settings
from django.contrib.auth import get_user
from django.contrib.auth.models import User, Permission, Group
from .models import CustomUser

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
        self.assertEqual(self.user.total_due, 400)
        self.assertEqual(self.child.total_due, 250)
        self.assertEqual(self.senior.total_due, 300)

        