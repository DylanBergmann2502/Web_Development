from django.test import TestCase
from users.models import Profile
from django.contrib.auth.models import User

# These are unit tests
class TestModels(TestCase):

    def setUp(self):
        self.user1 = User.objects.create(username="Tester1", password="testing1")

    def test_profile_exists(self): # the profile is created when the user is created
        self.assertEquals(Profile.objects.all().count(), 1)
        self.assertNotEquals(Profile.objects.all().count(), 0)

    def test_profile_str(self):  # string method
        self.profile1 = Profile.objects.first()
        self.assertEquals(str(self.profile1), 'Tester1 Profile')
        self.assertNotEquals(str(self.profile1), 'Profile Object 1')

    def test_profile_deleted(self):  # the profile is deleted when the user is deleted
        User.objects.first().delete()
        self.assertEquals(Profile.objects.all().count(), 0)
        self.assertNotEquals(Profile.objects.all().count(), 1)