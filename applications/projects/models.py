from django.db import models
from django.utils.translation import gettext_lazy as _
from model_utils.models import TimeStampedModel

from applications.users.models import User


class Project(TimeStampedModel):
    project_name = models.CharField(max_length=100, verbose_name=_('Nombre del proyecto'))
    project_description = models.CharField(max_length=1000, verbose_name=_('Descripción'))
    property = models.ForeignKey('properties.Property', on_delete=models.SET_NULL, null=True, blank=True,  verbose_name=_('Propiedad'), related_name='projects')
    project_owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_('Creador'))
    is_active = models.BooleanField(default=True, verbose_name=_('Activo'))

    class Meta:
        verbose_name = _('Proyecto')
        verbose_name_plural = _('Proyectos')
        constraints = [
            models.UniqueConstraint(
                fields=['project_name', 'project_owner'],
                name='unique_project_name_per_owner',
            )
        ]

    def __str__(self):
        return self.project_name


class ProjectCollaborator(TimeStampedModel):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, verbose_name=_('Proyecto'), related_name='collaborators')
    collaborator = models.ForeignKey('users.User', on_delete=models.CASCADE, verbose_name=_('Colaborador'))
    role = models.ForeignKey('users.Role', on_delete=models.SET_NULL, null=True, verbose_name=_('Rol'))
    can_edit = models.BooleanField(default=False, verbose_name=_('Puede editar'))
    company = models.ForeignKey('users.Company', on_delete=models.SET_NULL, null=True, verbose_name=_('Empresa'), related_name='collaborators')
    is_legal_rep = models.BooleanField(default=False, verbose_name=_('Es representante legal'))

    def __str__(self):
        return f'{self.project.name} - {self.collaborator.name}'

    class Meta:
        verbose_name = _('Colaborador de Proyecto')
        verbose_name_plural = _('Colaboradores de Proyecto')
