from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .api.viewsets.project_viewset import ProjectViewSet
from .views import *

app_name = 'projects'

router = DefaultRouter()
router.register(r'projects', ProjectViewSet)

urlpatterns = [
    path('projects/', ProjectListView.as_view(), name='project_list'),
    path('projects/create_and_edit/', create_and_edit_project, name='create_and_edit_project'),
    path('projects/<int:pk>/create/', ProjectCreateView.as_view(), name='create_project'),
    path('projects/<int:pk>/', ProjectDetailView.as_view(), name='project_detail'),
    path('projects/<int:pk>/delete/', ProjectDeleteView.as_view(), name='delete_project'),
    path('api/', include(router.urls)),
]