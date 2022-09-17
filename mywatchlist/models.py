from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class MyWatchList(models.Model):
    watched = models.BooleanField()
    title = models.CharField(max_length=255)
    rating = models.IntegerField(validators=[MaxValueValidator(5), MinValueValidator(1)]) # https://stackoverflow.com/questions/849142/how-to-limit-the-maximum-value-of-a-numeric-field-in-a-django-model
    release_date = models.DateField() # https://stackoverflow.com/questions/2771676/django-datetime-issues-default-datetime-now
    review = models.TextField()