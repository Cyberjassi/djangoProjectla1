from django.forms import ModelForm
from django import forms
from .models import Project

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = '__all__'  # Include all fields from the Project model
        widgets={
            'tags':forms.CheckboxSelectMultiple(),
        }
