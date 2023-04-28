from django.contrib.auth.models import User
from django.contrib.auth import get_user
from django.test import TestCase, Client
from django.urls import reverse
from users.models import Profile

# These are integration tests
class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.register = reverse('register')
        self.profile = reverse('profile')
        self.data_invalid = {
                    'username': 'tim',
                    'email': 'tim@gmail.com',
                    'password1': 'testing123',
                    'password2': 'testing123'
                }
        self.data_valid = {
            'username': 'dylan',
            'email': 'dylan@gmail.com',
            'password1': '@DylanBergmanN1!',
            'password2': '@DylanBergmanN1!'
        }

    # test register view
    def test_register_GET(self):
        response = self.client.get(self.register)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/register.html')

    def test_register_POST_no_data(self):
        response = self.client.post(self.register)
        self.assertEquals(response.status_code, 200)
        self.assertNotEquals(response.status_code, 302)
        self.assertEquals(User.objects.all().count(), 0)

    def test_register_POST_invalid_data(self):
        response = self.client.post(self.register,data=self.data_invalid)
        self.assertEquals(response.status_code, 200)
        self.assertNotEquals(response.status_code, 302)
        self.assertEquals(User.objects.all().count(), 0)

    def test_register_POST_valid_data(self):
        response = self.client.post(self.register,data=self.data_valid)
        self.assertEquals(response.status_code, 302) # 302 = redirect response code
        self.assertNotEquals(response.status_code, 200)

        self.assertEquals(User.objects.get(id=1).username, 'dylan')
        self.client.login(username='dylan', password='@DylanBergmanN1!')
        self.assertTrue(get_user(self.client).is_authenticated)  # log the user in

        self.assertEquals(Profile.objects.all().count(), 1)
        self.assertNotEquals(Profile.objects.all().count(), 0)

    # test profile view
    def test_profile(self):
        user = User.objects.create(username="dylan", email="dylan@gmail.com")
        self.client.force_login(user)
        self.client.post(self.profile,
                         data={'username': 'new_dylan',
                               'email': 'newdylan@gmail.com',
                               'image': 'default.jpg'}) # have to specify all kwargs, else it won't work
        user.refresh_from_db()
        self.assertEquals(user.username, 'new_dylan')