from rest_framework import serializers
from applications.projects.models import Project
from django.utils.translation import gettext_lazy as _
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

    def validate(self, data):
        # Obtener los valores necesarios para la validación
        architecture_project_name = data.get('architecture_project_name')
        project = data.get('project')

        # En caso de que esté actualizando una instancia, necesitas obtener el proyecto desde la instancia si no se provee en el request
        if self.instance:
            project = project or self.instance.project

        # Comprueba si el nombre de proyecto de arquitectura ya existe para el mismo proyecto
        if ArchitectureProject.objects.filter(
                architecture_project_name=architecture_project_name,
                project=project
        ).exclude(id=self.instance.id if self.instance else None).exists():
            raise serializers.ValidationError({
                'architecture_project_name': _(
                    "Este nombre de proyecto de arquitectura ya existe para este proyecto. Debes escoger otro.")
            })

        return data

