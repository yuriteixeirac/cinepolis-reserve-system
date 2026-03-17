from django.db import models


class Room(models.Model):
    class Meta:
        app_label = 'cinema'


    code = models.IntegerField()
    capacity = models.IntegerField()
