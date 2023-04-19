from members.models import CustomUser
from django.test import TestCase

from django.contrib.auth import get_user

class LoginTests(TestCase):

    def setUp(self):
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
    
    def test_login(self):
        self.assertFalse(get_user(self.client).is_active)
        self.client.login(username='test_user', password='top_secret')
        self.assertTrue(get_user(self.client).is_active)

    def test_logout(self):
        self.client.login(username='test_user', password='top_secret')
        self.assertTrue(get_user(self.client).is_active)
        self.client.logout()
        self.assertFalse(get_user(self.client).is_active)

    def test_login_url_exists_at_correct_location(self):
        response = self.client.get("/login")
        self.assertEqual(response.status_code, 301)