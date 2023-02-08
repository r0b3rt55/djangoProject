from random import randint

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.mail import send_mail, EmailMessage
from django.shortcuts import render, redirect
from django.template.loader import get_template
from django.urls import reverse_lazy
from django.views.generic import CreateView

from djangoProject.settings import EMAIL_HOST_USER
from userextend.forms import UserCreationNewform


class UserExtendCreateView(CreateView):
    template_name = 'userextend/create_user.html'
    model = User
    form_class = UserCreationNewform
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        if form.is_valid() and not form.errors:
            new_user = form.save(commit=False)

            username_number = "".join([str(randint(0, 9)) for _ in range(6)])
            username = f"{new_user.first_name.lower()}{new_user.last_name.lower()}_{username_number}"
            new_user.username = username

            subject = "Congratulations! You've signed up!"
            message = f"Hi, {new_user.first_name} {new_user.last_name}. \n\nYou have created an account."
            message += f"Your username is {new_user.username}."
            message += "\n\nCheers!"

            new_user.save()
            # Trimitere email fara template
            # send_mail(subject, message, EMAIL_HOST_USER, [new_user.email])

            # Trimitere email cu template

            details_user = {
                "full_name": f'{new_user.first_name} {new_user.last_name}',
                "username": new_user.username

            }
            subject = "Congratulations! You've signed up!"
            message = get_template('mail.html').render(details_user)
            msg = EmailMessage(
                subject,
                message,
                EMAIL_HOST_USER,
                [new_user.email]
            )
            msg.content_subtype = 'html'  # main content is text/html
            msg.send()

        return redirect("login")
