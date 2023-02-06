from django import forms
from django.forms import TextInput, NumberInput, EmailInput, Textarea, DateInput, DateTimeInput, Select

from student.models import Student


class StudentForm(forms.ModelForm):
    #Class Meta: este o clasa interioara a clasei StudentForm. Folosit pentru a schimba comportamentul campurilor modelului
    # cum ar fi schimbarea ordinii fieldurilor din formular, adaugare de atribute(clase, placeholder etc)
    # Este optional adaugarea acestei clase.
    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'trainer', 'age', 'email', 'description', 'start_date', 'end_date', 'gender',
                  'active']  # asa le in ordinea in care le pun eu
        # fields = '__all__' asa le cum sunt scrise in model si le ia pe toate


        widgets = {
            'first_name': TextInput(attrs={'class': 'form-control',
                                           'placeholder': 'Please enter your first name'}),
            'last_name': TextInput(attrs={'class': 'form-control',
                                           'placeholder': 'Please enter your last name'}),
            'age': NumberInput(attrs={'class': 'form-control',
                                           'placeholder': 'Please enter your age'}),
            'email': EmailInput(attrs={'class': 'form-control',
                                      'placeholder': 'Please enter your email'}),
            'description': Textarea(attrs={'class': 'form-control',
                                       'placeholder': 'Please enter your description',
                                           'rows': 3, 'cols': 10}),
            'start_date': DateInput(attrs={'class': 'form-control', 'type': 'date'}),  # DateTimeInput -> type="datetime-local"
            'end_date': DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'gender': Select(attrs={'class': 'form-select'}),
            'trainer': Select(attrs={'class': 'form-select'})

        }

    def clean(self):
        cleaned_data = self.cleaned_data  # returneaza un dictionar cu valorile introduse din formular
        students = Student.objects.filter(email__icontains=cleaned_data.get('email'))
        if students:
            msg = f'This email {cleaned_data.get("email")} exists already in the database.'
            self._errors['email'] = self.error_class([msg])
            # self.errors['email'] -> specificam pe ce field va fi afisata eroarea
        if cleaned_data.get('start_date') > cleaned_data.get('end_date'):
            msg = f' The start date {cleaned_data.get("start_date")} is later than end date {cleaned_data.get("end_date")}'
            self._errors['start_date'] = self.error_class([msg])

        return cleaned_data


class StudentUpdateForm(forms.ModelForm):
    #Class Meta: este o clasa interioara a clasei StudentForm. Folosit pentru a schimba comportamentul campurilor modelului
    # cum ar fi schimbarea ordinii fieldurilor din formular, adaugare de atribute(clase, placeholder etc)
    # Este optional adaugarea acestei clase.
    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'trainer', 'age', 'email', 'description', 'start_date', 'end_date', 'gender',
                  'active']  # asa le in ordinea in care le pun eu
        # fields = '__all__' asa le cum sunt scrise in model si le ia pe toate


        widgets = {
            'first_name': TextInput(attrs={'class': 'form-control',
                                           'placeholder': 'Please enter your first name'}),
            'last_name': TextInput(attrs={'class': 'form-control',
                                           'placeholder': 'Please enter your last name'}),
            'age': NumberInput(attrs={'class': 'form-control',
                                           'placeholder': 'Please enter your age'}),
            'email': EmailInput(attrs={'class': 'form-control',
                                      'placeholder': 'Please enter your email'}),
            'description': Textarea(attrs={'class': 'form-control',
                                       'placeholder': 'Please enter your description',
                                           'rows': 3, 'cols': 10}),
            'start_date': DateInput(attrs={'class': 'form-control', 'type': 'date'}),  # DateTimeInput -> type="datetime-local"
            'end_date': DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'gender': Select(attrs={'class': 'form-select'}),
            'trainer': Select(attrs={'class': 'form-select'})

        }