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

    def validate_name(self, value):
        if Project.objects.filter(name=value).exists():
            raise serializers.ValidationError("El nombre del proyecto debe ser único.")
        return value
