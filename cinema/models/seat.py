from django.db import models
from django.db.models import enums

class Seat(models.Model):
    class Meta:
        app_label = 'cinema'

    room = models.ForeignKey('Room', on_delete=models.CASCADE)
