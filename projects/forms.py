from django.forms import ModelForm
from django import forms
from .models import Project

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'description', 'source_link', 'demo_link', 'featured_image', 'tags']
        widgets = {
            'tags':forms.CheckboxSelectMultiple(),

        }

    def __init__(self, *args, **kwargs):
        super(ProjectForm, self).__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs.update({'class':'input'})

       # self.fields['title'].widget.attrs.update({'class':'input', 'placeholder':'Add title'})
      #  self.fields['description'].widget.attrs.update({'class':'input', 'placeholder':'Add a description for your project'})
      #  self.fields['source_link'].widget.attrs.update({'class': 'input', 'placeholder': 'Add the source link for your project'})
       # self.fields['demo_link'].widget.attrs.update({'class': 'input', 'placeholder': 'Add a demo link for your project'})