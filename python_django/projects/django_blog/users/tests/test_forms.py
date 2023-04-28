from django.test import TestCase
from users.forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.http import HttpRequest
from django.contrib.auth import get_user

# These are unit tests
class TestForms(TestCase):

    def setUp(self):
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

    #User Registration Form = URU
    def test_URU_valid(self):
        form1 = UserRegisterForm(data=self.data_invalid)
        print(form1.errors)
        self.assertFalse(form1.is_valid()) #password is too common => fails validation

        form2 = UserRegisterForm(data=self.data_valid)
        self.assertTrue(form2.is_valid())  # Validated

        form3 = UserRegisterForm(data={})
        print(form3.errors)
        self.assertFalse(form3.is_valid())


    def test_URU_validated_data(self):
         form = UserRegisterForm(data=self.data_valid)
         form.save()
         self.assertEquals(form.cleaned_data.get('email'), 'dylan@gmail.com')
         self.assertNotEquals(form.cleaned_data.get('email'), 'DYLAN@gmail.com')

#User Update Form and Profile Update Form will be tested with the views