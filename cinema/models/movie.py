from django.db import models


class Movie(models.Model):
    class Meta:
        app_label = 'cinema'


    title = models.CharField(max_length=255)
    genre = models.CharField(max_length=50)
    duration = models.TimeField()
