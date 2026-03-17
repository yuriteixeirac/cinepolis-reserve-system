from django.db import models
from django.db.models import enums

class Seat(models.Model):
    class Meta:
        app_label = 'cinema'


    class Status(enums.TextChoices):
        AVALIABLE = ('avaliable', 'Avaliable')
        RESERVED = ('reserved', 'Reserved')
        PURCHASED = ('purchased', 'Purchased')


    room = models.ForeignKey('Room', on_delete=models.CASCADE)
    status = models.CharField(max_length=9, choices=Status.choices, default=Status.AVALIABLE)
