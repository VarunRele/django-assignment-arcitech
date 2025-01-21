from django.urls import path
from . import views

urlpatterns = [
    path('', views.ContentListView.as_view(), name='content-list'),
    path('content/<int:pk>/', views.ContentRetriveUpdateDestroyView.as_view())
]