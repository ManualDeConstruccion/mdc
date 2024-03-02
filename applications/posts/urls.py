from django.urls import path
from . import views

app_name = 'posts_app'

urlpatterns = [
    path('/<str:section_name>/', views.posts, name='posts'),
]