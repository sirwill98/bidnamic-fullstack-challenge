from django import forms
from .models import ClientApplicationData
from datetime import datetime, timedelta
from phonenumber_field.formfields import PhoneNumberField

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
        date = self.cleaned_data['date_of_birth']
        if date > (datetime.now() - timedelta(days=18*365)).date():
            raise forms.ValidationError("Must be 18 or older to submit a bid")
        return date


class ApplicationDataForm_part2(forms.ModelForm):
    google_ads_account_id = forms.CharField(max_length=10,min_length=10)
    telephone = PhoneNumberField()

    class Meta:
        model = ClientApplicationData
        fields = '__all__'
        exclude = ['title', 'first_name', 'last_name',  
        'date_of_birth', 'added', 'updated', 'user']

    def clean_date_of_birth(self):
        #raise forms.ValidationError("Must be 18 or older to submit a bid")
        date = self.cleaned_data['date_of_birth']
        if date > (datetime.now() - timedelta(days=18*365)).date():
            raise forms.ValidationError("Must be 18 or older to submit a bid")
        return date