from django import forms
from .models import Projects,Profile

class NewProjectsForm(forms.ModelForm):
    class Meta:
        model = Projects
        exclude = ['profile', 'post_date', 'poster', 'description']
        
class NewProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['username']        
       