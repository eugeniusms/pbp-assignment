from datetime import datetime
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class MyWatchList(models.Model):
    watched = models.BooleanField(default=False)
    title = models.CharField(default="Judul",max_length=255)
    rating = models.IntegerField(default=1,validators=[MaxValueValidator(5), MinValueValidator(1)]) # https://stackoverflow.com/questions/849142/how-to-limit-the-maximum-value-of-a-numeric-field-in-a-django-model
    release_date = models.DateField(default=datetime.now, blank=True) # https://stackoverflow.com/questions/2771676/django-datetime-issues-default-datetime-now
    review = models.TextField(default="Review")