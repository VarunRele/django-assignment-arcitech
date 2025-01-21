from django.shortcuts import render
from .models import User
from .serializers import UserSerializer
from rest_framework import generics


class UserRegisterView(generics.CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = []

    def perform_create(self, serializer):
        serializer.save()