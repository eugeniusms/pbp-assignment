from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) # https://docs.djangoproject.com/en/4.1/topics/auth/default/ && https://docs.djangoproject.com/en/4.1/ref/models/fields/#foreignkey
    date = models.DateField() # https://stackoverflow.com/questions/2771676/django-datetime-issues-default-datetime-now
    title = models.CharField(max_length=255)
    description = models.TextField()