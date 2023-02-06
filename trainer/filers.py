import django_filters
from django import forms
from django_filters import DateFilter

from trainer.models import Trainer

# lookup_expr -> icontains, startswith, endswith, lte, lt ,gte, gt

#lte - lower than or equal to
#lt - lower than

#gte - greater than or equal to
#gt - greater than


class TrainerFilter(django_filters.FilterSet):
    first_name = django_filters.CharFilter(lookup_expr='icontains', label='First name')
    last_name = django_filters.CharFilter(lookup_expr='icontains', label='Last name')
    email = django_filters.CharFilter(lookup_expr='icontains', label='Email address')

    start_date_gte = DateFilter(field_name='start_date', lookup_expr='gte', label='From start date',
                                widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))
    start_date_lte = DateFilter(field_name='start_date', lookup_expr='lte', label='To start date',
                                widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))

    end_date_gte = DateFilter(field_name='end_date', lookup_expr='gte', label='From end date',
                                widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))
    end_date_lte = DateFilter(field_name='end_date', lookup_expr='lte', label='To end date',
                                widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))

    class Meta:
        model = Trainer
        fields = ['first_name', 'last_name', 'start_date_gte', 'start_date_lte', 'end_date_gte',
                  'end_date_lte']


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.filters['first_name'].field.widget.attrs.update({'class': 'form-control', 'placeholder': 'Please enter first name'})
        self.filters['last_name'].field.widget.attrs.update({'class': 'form-control', 'placeholder': 'Please enter last name'})

