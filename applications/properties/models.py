from django.db import models
from django.utils.translation import gettext_lazy as _

from applications.regioncomuna.models import Region, Comuna


# Create your models here.

class Property(models.Model):
    name = models.CharField(max_length=200, verbose_name=_("Nombre de la Propiedad"))
    rol = models.CharField(max_length=100, verbose_name=_("Rol de la Propiedad"))
    description = models.TextField(verbose_name=_("Descripción"))
    owner = models.ForeignKey('users.User', on_delete=models.SET_NULL, null=True, verbose_name=_("Propietario"))
    address = models.CharField(max_length=255, verbose_name=_("Dirección"))
    region = models.ForeignKey(Region, on_delete=models.SET_NULL, null=True, verbose_name=_("Región"))
    comuna = models.ForeignKey(Comuna, on_delete=models.SET_NULL, null=True, verbose_name=_("Comuna"))
    localidad = models.CharField(max_length=100, blank=True, null=True, verbose_name=_("Localidad"))
    block = models.CharField(max_length=100, blank=True, null=True, verbose_name=_("Cuadra"))
    allotment = models.CharField(max_length=100, blank=True, null=True, verbose_name=_("Lote"))
    neighborhood = models.CharField(max_length=100, blank=True, null=True, verbose_name=_("Población, Loteo, Villa"))
    subdivision_plan = models.CharField(max_length=255, blank=True, null=True, verbose_name=_("Plano de loteo N°"))

    def __str__(self):
        return self.name + " - " + self.rol

    class Meta:
        verbose_name = _("Propiedad")
        verbose_name_plural = _("Propiedades")


class BuildingPermit(models.Model):
    TYPE_CHOICES = (
        ('Obra Menor', 'Obra Menor'),
        ('Anteproyecto', 'Anteproyecto'),
        ('Obra Nueva', 'Obra Nueva')
    )

    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='building_permit')
    permit_date = models.DateField(verbose_name=_("Fecha de Permiso"))
    permit_number = models.CharField(max_length=100, verbose_name=_("Número de Permiso"))
    file = models.FileField(upload_to='permits/', null=True, blank=True, verbose_name=_("Archivo de Permiso"))
    land_area = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, verbose_name=_("Superficie Permiso"))
    type = models.CharField(max_length=20, choices=TYPE_CHOICES, default='Construcción', verbose_name=_("Tipo de Permiso"))
    permit_comment = models.CharField(max_length=255, blank=True, null=True, verbose_name=_("Comentario de Permiso"))

    def __str__(self):
        return self.property.name + " - " + _("Permiso")

    class Meta:
        verbose_name = _("Permiso de la Propiedad")
        verbose_name_plural = _("Permisos de la Propiedad")

        ordering = ['permit_date']


class BuildingReception(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='bulding_reception')
    reception_number = models.CharField(
        max_length=100, verbose_name=_("Número de Recepción"))
    reception_date = models.DateField(verbose_name=_("Fecha de Recepción"))
    partial_reception = models.BooleanField(default=False, verbose_name=_("Recepción Parcial"))
    building_permit = models.ForeignKey(BuildingPermit, on_delete=models.SET_NULL, null=True, blank=True, verbose_name=_("Permiso de Construcción"))
    file = models.FileField(upload_to='receptions/', null=True, blank=True, verbose_name=_("Archivo de Recepción"))
    land_area = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, verbose_name=_("Superficie Terreno"))
    reception_comment = models.CharField(max_length=255, blank=True, null=True, verbose_name=_("Comentario de Recepción"))

    def __str__(self):
        return self.property.name + " - " + _("Recepción")

    class Meta:
        verbose_name = _("Recepción de la Propiedad")
        verbose_name_plural = _("Recepciones de la Propiedad")

        ordering = ['reception_date']


class WaterCertificate(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='water_certificate')
    certificate_number = models.CharField(max_length=100, verbose_name=_("Número de Certificado"))
    certificate_date = models.DateField(verbose_name=_("Fecha de Certificado"))
    file = models.FileField(upload_to='certificates/', null=True, blank=True, verbose_name=_("Archivo de Certificado"))
    certificate_comment = models.CharField(max_length=255, blank=True, null=True, verbose_name=_("Comentario de Certificado"))

    def __str__(self):
        return self.property.name + " - " + _("Certificado de Agua")

    class Meta:
        verbose_name = _("Certificado de Agua")
        verbose_name_plural = _("Certificados de Agua")

        ordering = ['certificate_date']


class ElectricCertificate(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='electric_certificate')
    certificate_number = models.CharField(max_length=100, verbose_name=_("Número de Certificado"))
    certificate_date = models.DateField(verbose_name=_("Fecha de Certificado"))
    file = models.FileField(upload_to='certificates/', null=True, blank=True, verbose_name=_("Archivo de Certificado"))
    certificate_comment = models.CharField(max_length=255, blank=True, null=True, verbose_name=_("Comentario de Certificado"))

    def __str__(self):
        return self.property.name + " - " + _("Certificado Eléctrico")

    class Meta:
        verbose_name = _("Certificado Eléctrico")
        verbose_name_plural = _("Certificados Eléctricos")

        ordering = ['certificate_date']


class GasCertificate(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='gas_certificate')
    certificate_number = models.CharField(max_length=100, verbose_name=_("Número de Certificado"))
    certificate_date = models.DateField(verbose_name=_("Fecha de Certificado"))
    file = models.FileField(upload_to='certificates/', null=True, blank=True, verbose_name=_("Archivo de Certificado"))
    certificate_comment = models.CharField(max_length=255, blank=True, null=True, verbose_name=_("Comentario de Certificado"))

    def __str__(self):
        return self.property.name + " - " + _("Certificado de Gas")

    class Meta:
        verbose_name = _("Certificado de Gas")
        verbose_name_plural = _("Certificados de Gas")

        ordering = ['certificate_date']


class OtherCertificate(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='other_certificate')
    certificate_name = models.CharField(max_length=100, verbose_name=_("Nombre del Certificado"))
    certificate_number = models.CharField(max_length=100, verbose_name=_("Número de Certificado"))
    certificate_date = models.DateField(verbose_name=_("Fecha de Certificado"))
    file = models.FileField(upload_to='certificates/', null=True, blank=True, verbose_name=_("Archivo de Certificado"))
    certificate_comment = models.CharField(max_length=255, blank=True, null=True, verbose_name=_("Comentario de Certificado"))

    def __str__(self):
        return self.property.name + " - " + self.certificate_name

    class Meta:
        verbose_name = _("Otros Certificados")
        verbose_name_plural = _("Otros Certificados")

        ordering = ['certificate_date']

        unique_together = ('property', 'certificate_name')


class CountyRecorder(models.Model):
    name = models.CharField(max_length=255, verbose_name=_("Nombre del Conservador"))
    comuna = models.ForeignKey(Comuna, on_delete=models.CASCADE, verbose_name=_("Comuna"))

    def __str__(self):
        return 'Conservador de Bienes Raíces de ' + self.comuna.comuna


class OwnershipCertificate(models.Model):
    TYPE_CHOICES = (
        ('Hipotecas y Gravámenes', 'Hipotecas y Gravámenes'),
        ('Propiedad',  'Propiedad'),
        ('Prohibiciones', 'Prohibiciones')
    )

    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='ownership_certificate')
    county_recorder = models.ForeignKey(CountyRecorder, on_delete=models.CASCADE, verbose_name=_("county_recorder"))
    type = models.CharField(max_length=30, choices=TYPE_CHOICES, default='Propiedad', verbose_name=_("Tipo de Certificado"))
    leaves = models.CharField(max_length=100, verbose_name=_("Fojas"))
    number = models.CharField(max_length=100, verbose_name=_("Número"))
    year = models.CharField(max_length=100, verbose_name=_("Año"))
    file = models.FileField(upload_to='certificates/', null=True, blank=True, verbose_name=_("Archivo de Certificado"))
    certificate_comment = models.CharField(max_length=255, blank=True, null=True, verbose_name=_("Comentario de Certificado"))

    def __str__(self):
        return self.property.name + " - " + _("Certificado de Patente")

    class Meta:
        verbose_name = _("Certificado de Patente")
        verbose_name_plural = _("Certificados de Patente")

        ordering = ['year']
