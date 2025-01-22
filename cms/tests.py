from rest_framework.test import APITestCase
from rest_framework import status
from user.models import User
from .models import Category, Content
from django.urls import reverse
from faker import Faker
from rest_framework.authtoken.models import Token
from django.core.files.uploadedfile import SimpleUploadedFile

class ContentTest(APITestCase):

    def setUp(self):
        faker = Faker()
        self.list_create_content_url = reverse('content-list')
        # self.token_url = reverse('authorization')
        self.author = User.objects.create_user(
            username=faker.user_name(),
            email=faker.email(),
            password=faker.password(),
            phone="1234567890",
        )
        self.author_token = Token.objects.create(user=self.author).key
        self.admin_user = User.objects.create_superuser(
            username=faker.user_name(),
            email=faker.email(),
            password=faker.password(),
            phone="1234567890",
        )
        self.admin_token = Token.objects.create(user=self.admin_user).key
        self.cat_1 = Category.objects.create(name="Test 1")
        self.cat_2 = Category.objects.create(name="Super")
        self.file = SimpleUploadedFile(name='test.pdf', content=b'file content', content_type='application/pdf')
        self.content_admin = Content.objects.create(
            title="First Content",
            body="dummy",
            summary="First summary",
            document=self.file,
            author=self.admin_user
        ) 
        return super().setUp()
    
    def test_list_content_unauthorized(self):
        response = self.client.get(self.list_create_content_url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_list_content_authorized(self):
        response = self.client.get(self.list_create_content_url, headers={"Authorization": f"Token {self.author_token}"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_admin_create_content_normal_author_cant_view(self):
        """
        Content is created by the admin user. Normal Authors can't view/update the content
        """
        response = self.client.get(self.list_create_content_url, headers={"Authorization": f"Token {self.author_token}"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), [])

    def test_admin_can_view_all_content_normal_user_can_view_own(self):
        self.author_content = Content.objects.create(
            title="Second Content",
            body="dummy",
            summary="Second summary",
            document=self.file,
            author=self.author
        ) 
        response = self.client.get(self.list_create_content_url, headers={"Authorization": f"Token {self.author_token}"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.json()), 1)
        response = self.client.get(self.list_create_content_url, headers={"Authorization": f"Token {self.admin_token}"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.json()), 2)