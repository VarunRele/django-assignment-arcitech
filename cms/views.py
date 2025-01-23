from django.shortcuts import render
from .models import Content, Category
from .serializers import ContentSerializer, QueryParameterSerializer, CategorySerializer
from rest_framework import generics
from django.core.files.uploadedfile import InMemoryUploadedFile
from rest_framework import exceptions
from .permissions import IsOwnerOrAdmin
from rest_framework import permissions
from rest_framework import parsers
from .mixins import PDFFileTypeMixin
from django.db.models import Q
from drf_spectacular.utils import extend_schema, extend_schema_view, OpenApiParameter, OpenApiExample
from drf_spectacular.types import OpenApiTypes

from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from django.utils.decorators import method_decorator


class ContentListView(PDFFileTypeMixin, generics.ListCreateAPIView):
    queryset = Content.objects.all()
    serializer_class = ContentSerializer
    permission_classes = [permissions.IsAuthenticated]
    parser_classes = [parsers.MultiPartParser]

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


    @swagger_auto_schema(
        operation_description="List all Content",
        manual_parameters=[
            openapi.Parameter(
                name='title',
                in_=openapi.IN_QUERY,
                description='Title of the content',
                required=False,
                type=openapi.TYPE_STRING
            ),
            openapi.Parameter(
                name='body',
                in_=openapi.IN_QUERY,
                description='Body of the Content',
                required=False,
                type=openapi.TYPE_STRING
            ),
            openapi.Parameter(
                name='summary',
                in_=openapi.IN_QUERY,
                description='Summary of the Content',
                required=False,
                type=openapi.TYPE_STRING
            ),
            openapi.Parameter(
                name='category',
                in_=openapi.IN_QUERY,
                description='Category',
                required=False,
                type=openapi.TYPE_STRING
            ),
        ]
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


    @swagger_auto_schema(
        operation_description="Create Content",
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class ContentRetriveUpdateDestroyView(PDFFileTypeMixin, generics.RetrieveUpdateDestroyAPIView):
    queryset = Content.objects.all()
    serializer_class = ContentSerializer
    permission_classes = [IsOwnerOrAdmin]


class CategoryListCreateView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAdminUser]


    @swagger_auto_schema(
        operation_description="Gets all category options"
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


    @swagger_auto_schema(
        operation_description="Create a category"
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)