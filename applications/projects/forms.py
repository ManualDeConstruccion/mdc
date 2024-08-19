from django import forms
from .models import Project


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['project_name', 'project_description']
        widgets = {
            'project_name': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'project_name',
            }),
            'project_description': forms.Textarea(attrs={
                'class': 'form-control',
                'id': 'project_description',
            })
        }
