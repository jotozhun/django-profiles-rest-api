import requests

from django.test import TestCase
from profiles_api.models import UserProfile


# Create your tests here.
class UserProfile(TestCase):
    def setUp(self) -> None:
        UserProfile.objects.create_user(email="jojojo@hotmail.com",
                                        name="jojojo",
                                        password="jojojo")
        print("Yikes")


    def test_created_user(self):
        data= requests.get("localhost:8000/api/hello-view")
        print(data)
        assert True
