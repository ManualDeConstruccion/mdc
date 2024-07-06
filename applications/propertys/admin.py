from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from .models import Property, BuildingPermit, BuildingReception, WaterCertificate, ElectricCertificate, GasCertificate, OtherCertificate, CountyRecorder, OwnershipCertificate

# Inline definitions
class BuildingPermitInline(admin.TabularInline):
    model = BuildingPermit
    extra = 0
    fields = ['permit_number', 'permit_date', 'type']

class BuildingReceptionInline(admin.TabularInline):
    model = BuildingReception
    extra = 0
    fields = ['reception_number', 'reception_date', 'partial_reception']

class CertificateInline(admin.TabularInline):
    model = WaterCertificate
    extra = 0
    fields = ['certificate_number', 'certificate_date']

class ElectricCertificateInline(admin.TabularInline):
    model = ElectricCertificate
    extra = 0
    fields = ['certificate_number', 'certificate_date']

class GasCertificateInline(admin.TabularInline):
    model = GasCertificate
    extra = 0
    fields = ['certificate_number', 'certificate_date']

class OtherCertificateInline(admin.TabularInline):
    model = OtherCertificate
    extra = 0
    fields = ['certificate_name', 'certificate_number', 'certificate_date']

class OwnershipCertificateInline(admin.TabularInline):
    model = OwnershipCertificate
    extra = 0
    fields = ['type', 'number', 'year']

# Admin for Property
class PropertyAdmin(admin.ModelAdmin):
    list_display = ('name', 'rol', 'owner', 'address', 'region', 'comuna')
    list_filter = ('region', 'comuna')
    search_fields = ('name', 'rol', 'address')
    inlines = [BuildingPermitInline, BuildingReceptionInline, CertificateInline, ElectricCertificateInline, GasCertificateInline, OtherCertificateInline, OwnershipCertificateInline]

# Admin for BuildingPermit
class BuildingPermitAdmin(admin.ModelAdmin):
    list_display = ('property', 'permit_number', 'permit_date', 'type')
    list_filter = ('type',)
    search_fields = ('permit_number',)

# Register models and their admins
admin.site.register(Property, PropertyAdmin)
admin.site.register(BuildingPermit, BuildingPermitAdmin)
admin.site.register(BuildingReception)
admin.site.register(WaterCertificate)
admin.site.register(ElectricCertificate)
admin.site.register(GasCertificate)
admin.site.register(OtherCertificate)
admin.site.register(CountyRecorder)
admin.site.register(OwnershipCertificate)
