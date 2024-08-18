from django.db.models import Q
from rest_framework import serializers
from rest_framework.views import exception_handler

from applications.projects.models import Project
from django.utils.translation import gettext_lazy as _
from django.db import IntegrityError
import logging


logger = logging.getLogger('project_app')


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'


class ProjectUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'

        extra_kwargs = {
            'project_name': {
                'error_messages': {
                    'max_length': 'El nombre del proyecto no puede tener más de 100 caracteres.',
                    'blank': 'Este campo es obligatorio',
                }
            },
            'project_description': {
                'error_messages': {
                    'max_length': 'La descripción no puede tener más de 1000 caracteres.',
                    'blank': 'Este campo es obligatorio'
                }
            }

        }

    def validate(self, data):
        project_name = data.get('project_name')
        project_owner = data.get('project_owner', self.context['request'].user)

        if self.instance:
            # Asegúrate de excluir el ID actual para permitir la actualización del proyecto
            if Project.objects.filter(project_name=project_name, project_owner=project_owner).exclude(
                    id=self.instance.id).exists():
                raise serializers.ValidationError({
                    'project_name': _(
                        "Este nombre de proyecto ya existe para este propietario. Debes escoger otro.")
                })
        else:
            # Validación para la creación de un nuevo proyecto
            if Project.objects.filter(project_name=project_name, project_owner=project_owner).exists():
                raise serializers.ValidationError({
                    'project_name': _(
                        "Este nombre de proyecto ya existe para este propietario. Debes escoger otro.")
                })

        return data