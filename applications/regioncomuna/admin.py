from django.contrib import admin
from .models import Region, Comuna

class ComunaInline(admin.TabularInline):
    model = Comuna
    extra = 1  # Número de formas extra para comunas

class RegionAdmin(admin.ModelAdmin):
    list_display = ('region',)
    inlines = [
        ComunaInline,
    ]

class ComunaAdmin(admin.ModelAdmin):
    list_display = ('comuna', 'region')
    list_filter = ('region',)
    search_fields = ('comuna',)

admin.site.register(Region, RegionAdmin)
admin.site.register(Comuna, ComunaAdmin)
