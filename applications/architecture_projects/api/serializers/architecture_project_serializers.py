from rest_framework import serializers
from applications.projects.models import Project
from applications.architecture_projects.models import ArchitectureProject
import logging

logger = logging.getLogger('architecture_projects_app')


class ArchitectureProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArchitectureProject
        fields = '__all__'


class ArchitectureProjectUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArchitectureProject
        fields = '__all__'

        extra_kwargs = {
            'architecture_project_name': {
                'error_messages': {
                    'max_length': 'El nombre del proyecto no puede tener más de 100 caracteres.',
                    'blank': 'Este campo es obligatorio'
                }
            }
        }


