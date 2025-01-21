from rest_framework.test import APITestCase
from rest_framework import status
from .models import User

class UserRegistrationTest(APITestCase):
    def test_register_author(self):
        data = {
            "username": "sit",
            "email": "author@example.com",
            "password": "Password1",
            "phone": "1234567890",
            "first_name": "test",
            "last_name": "test",
            "pincode": "123456",
        }
        response = self.client.post("/register/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(User.objects.filter(email="author@example.com").exists())