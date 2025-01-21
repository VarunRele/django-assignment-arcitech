from rest_framework import permissions
from user.models import User
from rest_framework.request import Request
from .models import Content


class IsOwnerOrAdmin(permissions.BasePermission):
    def has_object_permission(self, request: Request, view, obj: Content):
        user: User = request.user
        if obj.author == user or user.is_superuser:
            return True
        return False