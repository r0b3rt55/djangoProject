from django.db import models

# Create your models here.

class Trainer(models.Model):

    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    course = models.CharField(max_length=50)
    description = models.TextField(max_length=300)
    start_date = models.DateField()
    end_date = models.DateField()
    active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
