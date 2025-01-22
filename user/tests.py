from rest_framework.test import APITestCase
from rest_framework import status
from .models import User
from django.urls import reverse

class UserRegistrationTest(APITestCase):

    def setUp(self) -> None:
        self.register_url = reverse('register')
        self.auth = reverse('authentication')
        self.user_data = {
            "username": "sit",
            "email": "author@example.com",
            "password": "Password1",
            "phone": "1234567890",
            "first_name": "test",
            "last_name": "test",
            "pincode": "123456",
        }
        return super().setUp()

    def test_register_author(self):
        response = self.client.post(self.register_url, self.user_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(User.objects.filter(email="author@example.com").exists())

    def test_cannot_register_with_no_data(self):
        response = self.client.post(self.register_url)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_register_user_authenticate(self):
        creds = {"username": self.user_data["username"], "password": self.user_data["password"]}
        self.client.post(self.register_url, self.user_data, format='json')
        response = self.client.post(self.auth, creds, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_unregister_user_cannot_authorized(self):
        creds = {"username": self.user_data["username"], "password": self.user_data["password"]}
        response = self.client.post(self.auth, creds, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
