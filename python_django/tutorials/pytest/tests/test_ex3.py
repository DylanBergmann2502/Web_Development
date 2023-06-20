import pytest
from django.contrib.auth import get_user_model

User = get_user_model()

@pytest.mark.django_db
def test_user_create1():
   User.objects.create_user('test', 'test@test.com', 'test')
   count = User.objects.all().count()
   print(count)
   assert User.objects.count() == 1


@pytest.mark.django_db
def test_user_create0():
   count = User.objects.all().count()
   print(count)
   assert count == 0
