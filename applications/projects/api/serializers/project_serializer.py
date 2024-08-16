from rest_framework import serializers
from applications.projects.models import Project
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
            'name': {
                'error_messages': {
                    'max_length': 'El nombre del proyecto no puede tener más de 100 caracteres.',
                    'blank': 'Este campo es obligatorio'
                }
            },
            'description': {
                'error_messages': {
                    'max_length': 'La descripción no puede tener más de 1000 caracteres.',
                    'blank': 'Este campo es obligatorio'
                }
            }
        }
