from rest_framework import serializers
from applications.properties.models import Property
import logging

logger = logging.getLogger('properties_app')


class PropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = Property
        fields = '__all__'


class PropertyUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Property
        fields = '__all__'