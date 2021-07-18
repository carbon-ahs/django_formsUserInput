from django import forms
from django.forms import fields
from django.forms.fields import CharField
from . models import Snippet

class ContactForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField(label='E-mail')
    

class SnippetForm(forms.ModelForm):
    
    class Meta:
        model = Snippet
        fields = ['name', 'email', 'msg']
