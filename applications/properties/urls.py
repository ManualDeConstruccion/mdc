from django.urls import path
from .views import (
    PropertyCreateView,
    PropertyListView,
    PropertyDetailView,
    PropertyUpdateView,
    PropertyDeleteView
)

app_name = 'properties'

urlpatterns = [
    path('properties/', PropertyListView.as_view(), name='list'),
    path('properties/create/', PropertyCreateView.as_view(), name='create'),
    path('properties/<int:pk>/', PropertyDetailView.as_view(), name='detail'),
    path('properties/<int:pk>/update/', PropertyUpdateView.as_view(), name='update'),
    path('properties/<int:pk>/delete/', PropertyDeleteView.as_view(), name='delete'),
]
