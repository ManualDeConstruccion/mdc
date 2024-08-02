from django.urls import path
from .views import *

app_name = 'projects'

urlpatterns = [
    path('projects/', ProjectListView.as_view(), name='project_list'),
    path('projects/create_and_edit/', create_and_edit_project, name='create_and_edit_project'),
    path('projects/<int:project_id>/update/', update_project, name='update_project'),
    path('projects/<int:pk>/create/', ProjectCreateView.as_view(), name='create_project'),
    path('projects/<int:pk>/', ProjectDetailView.as_view(), name='project_detail'),
    path('projects/<int:pk>/edit/', ProjectUpdateView.as_view(), name='edit_project'),
    path('projects/<int:pk>/delete/', ProjectDeleteView.as_view(), name='delete_project'),
]