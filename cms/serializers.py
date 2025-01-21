from rest_framework import serializers
from .models import Content, Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name', 'description']

class ContentSerializer(serializers.ModelSerializer):
    categories_list = CategorySerializer(many=True, read_only=True, source='categories')
    class Meta:
        model = Content
        fields = [
            'id',
            'title',
            'body',
            'summary',
            'document',
            'categories',
            'categories_list',
            'author'
        ]
        extra_kwargs = {
            'categories': {'write_only': True},
            'author': {'read_only': True}
        }


class QueryParameterSerializer(serializers.Serializer):
    title = serializers.CharField(required=False)
    body = serializers.CharField(required=False)
    summary = serializers.CharField(required=False)
    category = serializers.CharField(required=False)