from django import forms
from django.forms.models import inlineformset_factory
from .models import BudgetProject, BudgetSubProject


class BudgetProjectForm(forms.ModelForm):
    class Meta:
        model = BudgetProject
        fields = ['project', 'profesional', 'client', 'description', 'amount', 'currency', 'start_date', 'is_active',
                  'budget_land_area', 'land_area_unit', 'price_per_square_unit']


class BudgetSubProjectForm(forms.ModelForm):
    class Meta:
        model = BudgetSubProject
        fields = ['description', 'amount', 'currency', 'start_date', 'is_active', 'budget_land_area', 'land_area_unit',
                  'price_per_square_unit']


# Crear el FormSet para BudgetSubProject
BudgetSubProjectFormSet = inlineformset_factory(
    parent_model=BudgetProject,  # El modelo padre
    model=BudgetSubProject,      # El modelo del subproyecto
    form=BudgetSubProjectForm,   # El formulario para los subproyectos
    extra=1,                     # Número de formas en el formulario que se muestra por defecto
    can_delete=True              # Permite eliminar subproyectos existentes
)
