from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from djangoProject.settings import EMAIL_HOST_USER
from userextend.forms import UserCreationNewform


class UserExtendCreateView(CreateView):
    template_name = 'userextend/create_user.html'
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        if form.is_valid() and not form.errors:
            new_user = form.save()

            subject = 'Congratulations! You have created an account.'
            message = f'Hi, {new_user.first_name} {new_user.last_name}. You have created an account'
            send_mail(subject, message, EMAIL_HOST_USER, [new_user.emial])

        return redirect('login')

