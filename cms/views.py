from django.shortcuts import render
from .models import Content
from .serializers import ContentSerializer, QueryParameterSerializer
from rest_framework import generics
from django.core.files.uploadedfile import InMemoryUploadedFile
from rest_framework import exceptions
from .permissions import IsOwnerOrAdmin
from rest_framework import permissions
from .mixins import PDFFileTypeMixin
from django.db.models import Q
from drf_spectacular.utils import extend_schema, extend_schema_view, OpenApiParameter, OpenApiExample
from drf_spectacular.types import OpenApiTypes

@extend_schema_view(
    get = extend_schema(
        description="Get all Content",
        parameters=[
            OpenApiParameter(
                "title", str, required=False, 
                description="Title of the content"
            ),
            OpenApiParameter(
                "body", str, required=False, 
                description="Body of the content"
            ),
            OpenApiParameter(
                "Summary", str, required=False, 
                description="Summary of the content"
            ),
            OpenApiParameter(
                "Category", str, required=False, 
                description="Category of the content"
            )
        ]
    ),
    post = extend_schema(
        description="Create Content."    
    )
)
class ContentListView(PDFFileTypeMixin, generics.ListCreateAPIView):
    queryset = Content.objects.all()
    serializer_class = ContentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        serializer = QueryParameterSerializer(data=self.request.GET)
        title = None
        body = None
        summary = None
        category = None
        if serializer.is_valid(raise_exception=True):
            title = serializer.validated_data.get('title') # type: ignore
            body = serializer.validated_data.get('body') # type: ignore
            summary = serializer.validated_data.get('summary')# type: ignore
            category = serializer.validated_data.get('category')# type: ignore
        if user.is_superuser: # type: ignore
            content = Content.objects.all()
        else:
            content = Content.objects.filter(author = user)
        query = Q()
        if title is not None:
            query = query | Q(title__icontains=title) 
        if body is not None:
            query = query | Q(body__icontains=body)
        if summary is not None:
            query = query | Q(summary__icontains=summary)
        if category is not None:
            query = query | Q(categories__name__icontains=category) | Q(categories__description__icontains=category)
        return content.filter(query)


class ContentRetriveUpdateDestroyView(PDFFileTypeMixin, generics.RetrieveUpdateDestroyAPIView):
    queryset = Content.objects.all()
    serializer_class = ContentSerializer
    permission_classes = [IsOwnerOrAdmin]