from django.db import models
from django.utils.translation import gettext_lazy as _
from model_utils.models import TimeStampedModel

from applications.regioncomuna.models import Comuna
from applications.architecture_projects.models import ArchitectureProject


class ArchitectureBaseType(TimeStampedModel):
    architecture_project = models.ForeignKey(ArchitectureProject, on_delete=models.CASCADE, verbose_name=_('Proyecto de arquitectura'), related_name='architecture_type')
    nombre_proyecto = models.CharField(max_length=255, verbose_name=_('Nombre del proyecto'), null=True, blank=True)
    comuna = models.ForeignKey(Comuna, on_delete=models.SET_NULL, null=True, blank=True, verbose_name=_('Comuna'), related_name='architecture_type')
    numero_solicitud = models.IntegerField(verbose_name=_('Número de solicitud'), null=True, blank=True)
    fecha_ingreso = models.DateField(verbose_name=_('Fecha de ingreso'), null=True, blank=True)
    codigo_rpi = models.CharField(max_length=100, verbose_name=_('Código Registro Proyectos Inmobiliarios'), null=True, blank=True)
    alteracion = models.BooleanField(default=False, verbose_name=_('Alteración'))
    cambio_destino = models.BooleanField(default=False, verbose_name=_('Cambio de destino'))
    demolicion = models.BooleanField(default=False, verbose_name=_('Demolición'))
    project_name = models.CharField(max_length=255, verbose_name=_('Nombre del proyecto'), null=True, blank=True)
    numero_CIP = models.CharField(max_length=100, verbose_name=_('Número Certificado de Informaciones Previas'), null=True, blank=True)
    fecha_CIP = models.DateField(verbose_name=_('Fecha Certificado de Informaciones Previas'), null=True, blank=True)

    # 4. Datos Profesionales Responsables
    calculista = models.BooleanField(default=False, verbose_name=_('Calculista'))
    constructor = models.BooleanField(default=False, verbose_name=_('Constructor'))
    inspector_tecnico = models.BooleanField(default=False, verbose_name=_('Inspector Técnico de Obra'))

    # 5. Participación de Revisores
    revisor_independiente = models.BooleanField(default=False, verbose_name=_('Revisor Independiente'))
    revisor_calculo = models.BooleanField(default=False, verbose_name=_('Revisor de Proyecto de Cálculo Estructural'))

    class Meta:
        abstract = True