from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _

from .models import User, Profession, Company, University, Role, Comuna, Region, Patent, Score


class ProfessionInline(admin.TabularInline):
    model = User.profession.through  # Usamos la relación ManyToMany
    extra = 1


class UserAdmin(BaseUserAdmin):
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal info'),
         {'fields': ('name', 'rut', 'address', 'address_number', 'comuna', 'region', 'phone', 'profession')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')})
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_staff', 'is_superuser'),
        }),
    )
    list_display = ('id','email', 'name', 'is_staff', 'rut')
    search_fields = ('email', 'name', 'rut')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'profession')
    inlines = [ProfessionInline]
    ordering = ('email',)


admin.site.register(User, UserAdmin)


### Admin para Company

class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'mail', 'owner')
    search_fields = ('name', 'mail')
    list_filter = ('comuna', 'region')


admin.site.register(Company, CompanyAdmin)


### Admin para Profession

class ProfessionAdmin(admin.ModelAdmin):
    list_display = ('profession', 'university')
    list_filter = ('profession',)
    search_fields = ('profession',)


admin.site.register(Profession, ProfessionAdmin)


### Admin para University

class UniversityAdmin(admin.ModelAdmin):
    list_display = ('name', 'region', 'type')
    list_filter = ('type', 'region')
    search_fields = ('name',)


admin.site.register(University, UniversityAdmin)


### Admin para otros modelos si es necesario

# Admin para Score
class ScoreAdmin(admin.ModelAdmin):
    list_display = ('score', 'user_owner', 'user_writer', 'comment')
    list_filter = ('score',)
    search_fields = ('comment',)


admin.site.register(Score, ScoreAdmin)


# Admin para Patent
class PatentAdmin(admin.ModelAdmin):
    list_display = ('name', 'profession', 'user_owner', 'number', 'category', 'validity_date')
    list_filter = ('profession', 'category')
    search_fields = ('name',)


admin.site.register(Patent, PatentAdmin)


# Admin para Role
class RoleAdmin(admin.ModelAdmin):
    list_display = ('role',)
    list_filter = ('role',)
    search_fields = ('role',)


admin.site.register(Role, RoleAdmin)
