from django.test import SimpleTestCase
from django.urls import resolve, reverse
from users.views import register, profile

# These are unit tests

# Should have also tested the LoginView, LogoutView, and 4 password reset views
# However, I am using Django's built-in views themselves, so I trust that I don't need to test them
class TestUrls(SimpleTestCase):

    def test_register(self):
        url = reverse('register')
        self.assertEquals(resolve(url).func, register)

    def test_profile(self):
        url = reverse('profile')
        self.assertEquals(resolve(url).func, profile)