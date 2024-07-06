from django.contrib import admin
from .models import BudgetProject, BudgetSubProject, Stage
from django.utils.translation import gettext_lazy as _

class BudgetSubProjectInline(admin.TabularInline):
    model = BudgetSubProject
    extra = 0
    fields = ['description', 'amount', 'currency', 'start_date', 'is_active', 'budget_land_area', 'price_per_square_unit']
    show_change_link = True

class StageInline(admin.TabularInline):
    model = Stage
    extra = 0
    fields = ['name', 'description', 'due_date', 'payment_trigger', 'is_payment_required', 'payment_amount', 'payment_type', 'time_frame', 'milestone']
    show_change_link = True

@admin.register(BudgetProject)
class BudgetProjectAdmin(admin.ModelAdmin):
    list_display = ['project', 'profesional', 'client', 'amount', 'currency', 'start_date', 'is_active']
    list_filter = ['is_active', 'currency', 'start_date']
    search_fields = ['project__name', 'description']
    inlines = [BudgetSubProjectInline, StageInline]

@admin.register(BudgetSubProject)
class BudgetSubProjectAdmin(admin.ModelAdmin):
    list_display = ['budget_project', 'description', 'amount', 'currency', 'start_date', 'is_active']
    list_filter = ['is_active', 'currency', 'start_date']
    search_fields = ['description']
    inlines = [StageInline]

@admin.register(Stage)
class StageAdmin(admin.ModelAdmin):
    list_display = ['name', 'budget_project', 'budget_sub_project', 'due_date', 'payment_trigger', 'is_payment_required', 'payment_amount']
    list_filter = ['payment_trigger', 'is_payment_required', 'due_date']
    search_fields = ['name', 'description', 'milestone']

