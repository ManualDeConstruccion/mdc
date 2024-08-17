from django.db import models
from django.utils.translation import gettext_lazy as _
from model_utils.models import TimeStampedModel

from applications.projects.models import Project


class ArchitectureProject(TimeStampedModel):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, verbose_name=_('Proyecto'), related_name='architecture_projects')
    architecture_project_name = models.CharField(max_length=100, verbose_name=_('Nombre Proyecto Arquitectura'))
    architecture_project_description = models.CharField(max_length=1000, verbose_name=_('Descripción'), null=True, blank=True)
    is_active = models.BooleanField(default=True, verbose_name=_('Activo'))
    start_date = models.DateField(verbose_name=_('Fecha de inicio'), null=True, blank=True)

    class Meta:
        verbose_name = _('Proyecto')
        verbose_name_plural = _('Proyectos')
        constraints = [
            models.UniqueConstraint(
                fields=['architecture_project_name', 'project'],
                name='unique_architecture_project_name_per_project'
            )
        ]

    def __str__(self):
        return self.architecture_project_name