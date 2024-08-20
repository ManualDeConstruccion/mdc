from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .api.viewsets.architecture_project_viewset import ArchitectureProjectViewSet

app_name = "architecture_projects"

router = DefaultRouter()
router.register(r'architecture-projects', ArchitectureProjectViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]