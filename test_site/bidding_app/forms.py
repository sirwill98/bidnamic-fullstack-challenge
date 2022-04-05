from django import forms
from .models import ClientApplicationData
from datetime import datetime, timedelta

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

    def clean_date_of_birth(self):
        #raise forms.ValidationError("Must be 18 or older to submit a bid")
        form_data = self.cleaned_data['date_of_birth']
        if form_data > (datetime.now() - timedelta(days=18*365)).date():
            raise forms.ValidationError("Must be 18 or older to submit a bid")
        return form_data


class ApplicationDataForm_part2(forms.ModelForm):
    class Meta:
        model = ClientApplicationData
        fields = '__all__'
        exclude = ['title', 'first_name', 'last_name', 
        'date_of_birth', 'added', 'updated', 'user']

    def clean_date_of_birth(self):
        #raise forms.ValidationError("Must be 18 or older to submit a bid")
        form_data = self.cleaned_data['date_of_birth']
        if form_data > (datetime.now() - timedelta(days=18*365)).date():
            raise forms.ValidationError("Must be 18 or older to submit a bid")
        return form_data