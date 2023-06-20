import pytest
from django.contrib.auth.models import User


# @pytest.mark.django_db
# def test_set_check_password(user_1):
#     user_1.set_password("new-password")
#     assert user_1.check_password("new-password") is True
#
# def test_username(user_1):
#     print('check-username')
#     assert user_1.username == "test-user"
#
# def test_set_check_password2(user_1):
#     print('check-user2')
#     assert user_1.username == "test-user"

# def test_user_A(user_A):
#     print(user_A.first_name)
#     assert user_A.first_name == "My Name"

# def test_user_B(user_B):
#     print(user_B.is_staff)
#     assert user_B.is_staff

def test_user_factory(db, user):
    count = User.objects.all().count()
    print(user.username, count)
    assert True

def test_product(product_factory):
    product = product_factory.build()
    print(product.description)
    assert True