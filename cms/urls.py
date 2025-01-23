from django.urls import path
from . import views

urlpatterns = [
    path('content', views.ContentListView.as_view(), name='content-list'),
    path('content/<int:pk>/', views.ContentRetriveUpdateDestroyView.as_view()),
    path('category/', views.CategoryListCreateView.as_view(), name='category-list')
]