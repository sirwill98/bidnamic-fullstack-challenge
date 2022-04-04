from tkinter import Widget
from django import forms
from .models import Client

class DateInput(forms.DateInput):
    input_type = 'date'

class SignUpClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = '__all__'
        exclude = ['user']
        widgets = {
            'date_of_birth': DateInput(),
        }