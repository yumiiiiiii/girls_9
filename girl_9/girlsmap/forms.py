from django import forms
from .models import bar

class barform(forms.ModelForm):
    class Meta:
        model=bar
        fields=['name','location','information','photo']
