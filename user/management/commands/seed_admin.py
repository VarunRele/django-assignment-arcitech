from django.core.management.base import BaseCommand
from user.models import User

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        if not User.objects.filter(email="admin@example.com").exists():
            User.objects.create_superuser(
                username='admin',
                email="admin@example.com",
                password="AdminPassword1",
                first_name='admin',
                last_name='test',
                phone="1234567890",
                pincode="123456",
            )

        
        print("Admin user created!")
