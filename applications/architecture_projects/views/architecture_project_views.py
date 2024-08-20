from django.http import HttpResponse
from django.shortcuts import redirect
from django.template.loader import render_to_string
from requests import Response
from rest_framework import status

from applications.architecture_projects.api.serializers.architecture_project_serializers import \
    ArchitectureProjectSerializer
from applications.architecture_projects.models import ArchitectureProject
from django.contrib.auth.decorators import login_required
from django.urls import reverse


def create_architecture_project(request):
    serializer = ArchitectureProjectSerializer(data=request.data)
    if serializer.is_valid():
        architecture_project = serializer.save()
        html = render_to_string('apps/architecture_projects/create_architecture_project.html', {'architecture_project': architecture_project})
        return HttpResponse(html)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
