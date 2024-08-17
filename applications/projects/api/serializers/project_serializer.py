from rest_framework import serializers
from applications.projects.models import Project
from django.utils.translation import gettext_lazy as _
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
                    'non_field_errors':  'Ya existe un proyecto con este nombre para el mismo propietario.'
                }
            },
            'project_description': {
                'error_messages': {
                    'max_length': 'La descripción no puede tener más de 1000 caracteres.',
                    'blank': 'Este campo es obligatorio'
                }
            }
        }

        def validate(self, attrs):
            project_name = attrs.get('project_name')
            project_owner = attrs.get('project_owner')
            if self.instance:
                # Check if project name changed for updates
                if self.instance.project_name != project_name and Project.objects.filter(project_name=project_name,
                                                                                         project_owner=project_owner).exists():
                    raise serializers.ValidationError(
                        {'project_name': _('Ya existe un proyecto con este nombre para el mismo propietario.')})
            else:
                # Check for creation
                if Project.objects.filter(project_name=project_name, project_owner=project_owner).exists():
                    raise serializers.ValidationError(
                        {'project_name': _('Ya existe un proyecto con este nombre para el mismo propietario.')})
            return attrs

