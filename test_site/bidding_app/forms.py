from django import forms
from .models import ClientApplicationData

class DateInput(forms.DateInput):
    input_type = 'date'

class ApplicationDataForm_part1(forms.ModelForm):
    class Meta:
        model = ClientApplicationData
        fields = 'title', 'first_name', 'last_name', 'date_of_birth'
        exclude = ['added', 'updated', 'user']
        widgets = {
            'date_of_birth': DateInput()
            }


class ApplicationDataForm_part2(forms.ModelForm):
    class Meta:
        model = ClientApplicationData
        fields = '__all__'
        exclude = ['title', 'first_name', 'last_name', 
        'date_of_birth', 'added', 'updated', 'user']