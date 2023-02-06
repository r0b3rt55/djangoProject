from django import forms
from django.forms import TextInput, Textarea, DateInput

from trainer.models import Trainer


class TrainerForm(forms.ModelForm):

    class Meta:
        model = Trainer
        fields = ['first_name', 'last_name', 'course', 'description', 'start_date',
                  'end_date', 'active']

        widgets = {
            'first_name': TextInput(attrs={'class': 'form-control',
                                           'placeholder': 'Please enter your first name'}),
            'last_name': TextInput(attrs={'class': 'form-control',
                                           'placeholder': 'Please enter your last name'}),
            'course': TextInput(attrs={'class': 'form-control',
                                           'placeholder': 'Enter course name'}),
            'description': Textarea(attrs={'class': 'form-control',
                                           'placeholder': 'Please enter your description',
                                           'rows': 3, 'cols': 10}),
            'start_date': DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'end_date': DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }

    def clean(self):
        cleaned_data = self.cleaned_data  # returneaza un dictionar cu valorile introduse din formular
        if cleaned_data.get('start_date') > cleaned_data.get('end_date'):
            msg = f' The start date {cleaned_data.get("start_date")} is later than end date {cleaned_data.get("end_date")}'
            self._errors['start_date'] = self.error_class([msg])

        return cleaned_data

class TrainerUpdateForm(forms.ModelForm):
    class Meta:
        model = Trainer
        fields =['first_name', 'last_name', 'course', 'description', 'start_date',
                  'end_date', 'active']

        widgets = {
            'first_name': TextInput(attrs={'class': 'form-control',
                                           'placeholder': 'Please enter your first name'}),
            'last_name': TextInput(attrs={'class': 'form-control',
                                          'placeholder': 'Please enter your last name'}),
            'course': TextInput(attrs={'class': 'form-control',
                                       'placeholder': 'Enter course name'}),
            'description': Textarea(attrs={'class': 'form-control',
                                           'placeholder': 'Please enter your description',
                                           'rows': 3, 'cols': 10}),
            'start_date': DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'end_date': DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }