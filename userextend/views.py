from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView


class UserExtendCreateView(CreateView):
    template_name = 'userextend/create_user.html'
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy('login')

