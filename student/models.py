from django.db import models

from trainer.models import Trainer


# Create your models here.

class Student(models.Model):

    gender_opstion = (('male', 'Male'), ('female', 'Female'))

    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    age = models.IntegerField()
    email = models.EmailField(max_length=50)
    description = models.TextField(max_length=300)
    start_date = models.DateField()
    end_date = models.DateField()
    gender = models.CharField(max_length=6, choices=gender_opstion )
    active = models.BooleanField(default=True)

    trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'