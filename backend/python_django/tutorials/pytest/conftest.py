import pytest

from pytest_factoryboy import register
from tests.factories import UserFactory, ProductFactory, CategoryFactory

register(UserFactory)
register(ProductFactory)
register(CategoryFactory)

@pytest.fixture
def new_user1(db, user_factory):
    # user = user_factory.build() # this wont save to the database
    user = user_factory.create()  # this will save to the database
    return user









# from django.contrib.auth import get_user_model
#
# User = get_user_model()
#
# @pytest.fixture()
# def user_1(db):
#     print("Create user")
#     return User.objects.create_user("test-user")
#
# @pytest.fixture()
# def new_user_factory(db):
#     def create_app_user(
#             username: str,
#             password: str = None,
#             first_name: str = "firstname",
#             last_name: str = "lastname",
#             email: str = "test@test.com",
#             is_staff: bool = False,
#             is_superuser: bool = False,
#             is_active: bool = True
#     ):
#         return User.objects.create_user(
#             username=username,
#             password=password,
#             first_name=first_name,
#             last_name=last_name,
#             email=email,
#             is_staff=is_staff,
#             is_superuser=is_superuser,
#             is_active=is_active
#         )
#     return create_app_user
#
# @pytest.fixture
# def user_A(db, new_user_factory):
#     return new_user_factory(username="Test User", password="password", first_name="My Name")
#
# @pytest.fixture
# def user_B(db, new_user_factory):
#     return new_user_factory(username="Test User", password="password", first_name="My Name", is_staff=True)
