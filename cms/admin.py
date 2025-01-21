from django.contrib import admin
from .models import Category, Content


admin.site.register(Content)
admin.site.register(Category)