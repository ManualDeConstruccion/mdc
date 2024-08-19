from django.db import models
from django.utils.translation import gettext_lazy as _

from applications.architecture_projects.models import ArchitectureBaseType


class ObraNueva(ArchitectureBaseType):
    # 6. Características del Proyecto de Obra Nueva
    loteo_contruccion_simultanea = models.BooleanField(blank=True, null=True, default=None, verbose_name=_('Loteo con construcción simultánea'))
    loteo_dfl2 = models.BooleanField(blank=True, null=True, default=None, verbose_name=_('Loteo DFL2'))
    class Meta:
        verbose_name = _('Permiso de Edificación - Obra Nueva')
