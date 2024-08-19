from django.contrib import admin
from .models import PermitType, PermitGroup, PermitSubType


class PermitSubTypeInline(admin.TabularInline):
    model = PermitSubType
    extra = 1
    fields = ['permit_sub_type']


class PermitGroupAdmin(admin.ModelAdmin):
    list_display = ('permit_group', 'display_permit_type')
    inlines = [PermitSubTypeInline]

    def display_permit_type(self, obj):
        return obj.permit_type.permit_type

    display_permit_type.short_description = 'Tipo de Permiso'


class PermitGroupInline(admin.TabularInline):
    model = PermitGroup
    extra = 1
    show_change_link = True
    fields = ['display_permit_type', 'permit_group']

    def display_permit_type(self, obj):
        return obj.permit_type.permit_type

    display_permit_type.short_description = 'Tipo de Permiso'
    readonly_fields = ('display_permit_type',)


class PermitTypeAdmin(admin.ModelAdmin):
    list_display = ['permit_type']
    search_fields = ['permit_type']
    inlines = [PermitGroupInline]


admin.site.register(PermitType, PermitTypeAdmin)
admin.site.register(PermitGroup, PermitGroupAdmin)
