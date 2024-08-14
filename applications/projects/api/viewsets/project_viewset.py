from rest_framework import viewsets, permissions
from rest_framework.permissions import BasePermission

from django.contrib.auth.models import User
from applications.projects.api.serializers.project_serializer import ProjectSerializer, ProjectCreateSerializer
from applications.projects.models import Project


class IsOwnerOrReadOnly(BasePermission):
    """
    Permiso personalizado para permitir solo a los propietarios de un proyecto
    realizar operaciones de escritura.
    """

    def has_permission(self, request, view):
        # Permitir acceso seguro a cualquier usuario autenticado
        if request.method in permissions.SAFE_METHODS:
            return True
        # Solo permitir la creación de proyectos a usuarios autenticados
        if request.method == 'POST':
            return request.user.is_authenticated
        return False  # Por defecto, no permitir otras acciones

    def has_object_permission(self, request, view, obj):
        # Permitir métodos seguros (lectura) a cualquier usuario
        if request.method in permissions.SAFE_METHODS:
            return True
        # Permitir acciones de escritura solo si el usuario es el propietario del proyecto
        return obj.project_owner == request.user


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()

    def get_permissions(self):
        """
        Asigna permisos basados en la acción que se esté realizando en el viewset.
        """
        if self.action in ['create', 'update', 'patch', 'destroy']:
            permission_classes = [IsOwnerOrReadOnly]
        else:
            permission_classes = [permissions.IsAuthenticated]
        return [permission() for permission in permission_classes]

    def get_serializer_class(self):
        """
        Asigna diferentes serializadores para las acciones de creación y otras acciones.
        """
        if self.action == 'create':
            return ProjectCreateSerializer
        return ProjectSerializer
