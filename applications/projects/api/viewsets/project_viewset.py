from rest_framework import viewsets

from applications.projects.api.serializers.project_serializer import ProjectSerializer
from applications.projects.models import Project


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
