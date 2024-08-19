from django.db import models
from django.utils.translation import gettext_lazy as _
from model_utils.models import TimeStampedModel

from applications.projects.models import Project


class PermitType(models.Model):
    permit_type = models.CharField(max_length=255, verbose_name=_('Tipo de Permiso'))

    def __str__(self):
        return self.permit_type


class PermitGroup(models.Model):
    permit_type = models.ForeignKey(PermitType, on_delete=models.CASCADE, verbose_name=_('Tipo de Permiso'), related_name='permit_groups')
    permit_group = models.CharField(max_length=255, verbose_name=_('Grupo de Permisos'))

    def __str__(self):
        return f'{self.permit_group} - {self.permit_type.permit_type}'


class PermitSubType(models.Model):
    permit_group = models.ForeignKey(PermitGroup, on_delete=models.CASCADE, verbose_name=_('Grupo de Permisos'), related_name='permit_subtypes')
    permit_sub_type = models.CharField(max_length=255, verbose_name=_('Subtipo de Permiso'))

    def __str__(self):
        return f'{self.permit_sub_type} - {self.permit_group.permit_group}'


class ArchitectureProject(TimeStampedModel):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, verbose_name=_('Proyecto'), related_name='architecture_projects')
    architecture_project_name = models.CharField(max_length=100, verbose_name=_('Nombre Proyecto Arquitectura'), null=True, blank=True)
    architecture_project_description = models.CharField(max_length=1000, verbose_name=_('Descripción'), null=True, blank=True)
    is_active = models.BooleanField(default=True, verbose_name=_('Activo'))
    start_date = models.DateField(verbose_name=_('Fecha de inicio'), null=True, blank=True)

    class Meta:
        verbose_name = _('Proyecto')
        verbose_name_plural = _('Proyectos')

    def __str__(self):
        return self.architecture_project_name