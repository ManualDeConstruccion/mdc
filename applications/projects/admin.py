from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from .models import Project, ProjectCollaborator
from applications.users.models import Role


class ProjectCollaboratorInline(admin.TabularInline):
    model = ProjectCollaborator
    extra = 1
    autocomplete_fields = ['collaborator', 'role', 'company']


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'project_name', 'project_description', 'property', 'is_active')
    list_filter = ('is_active', 'property__region')
    search_fields = ('project_name', 'project_description', 'property__name')
    inlines = [ProjectCollaboratorInline]
    fieldsets = (
        (None, {
            'fields': ('project_name', 'project_description', 'property', 'is_active')
        }),
    )


class ProjectCollaboratorAdmin(admin.ModelAdmin):
    list_display = ('project', 'collaborator', 'role', 'can_edit', 'is_legal_rep', 'company')
    list_filter = ('project', 'role', 'company', 'can_edit', 'is_legal_rep')
    search_fields = ('project__project_name', 'collaborator__name', 'role__role')
    autocomplete_fields = ['project', 'collaborator', 'role', 'company']


admin.site.register(Project, ProjectAdmin)
admin.site.register(ProjectCollaborator, ProjectCollaboratorAdmin)
