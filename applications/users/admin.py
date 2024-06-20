from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _

from .models import User

class UserAdmin(BaseUserAdmin):
    # Esto define lo que se mostrará en la pantalla de edición de usuarios
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal info'), {'fields': ('nombre_completo',)}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'created_at', 'updated_at')}),
    )
    # Esto define lo que se mostrará en la pantalla de creación de usuarios
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )
    # Esto define los filtros que aparecerán en el lado derecho del panel de administración
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')
    # Esto define cómo se listan los usuarios en la vista general; puedes ajustarlo como prefieras
    list_display = ('email', 'nombre_completo', 'is_staff')
    # Esto permite buscar usuarios por campos específicos
    search_fields = ('email', 'nombre_completo')
    # Orden predeterminado de los usuarios en la vista general
    ordering = ('email',)
    # Si has añadido fechas u otros campos, puedes incluirlos aquí
    readonly_fields = ('last_login', 'created_at', 'updated_at')

admin.site.register(User, UserAdmin)

