from django.db import models


class Ticket(models.Model):
    user = models.ForeignKey('accounts.User', on_delete=models.CASCADE)
    seat = models.ForeignKey('Seat', on_delete=models.CASCADE)
    session = models.ForeignKey('Session', on_delete=models.CASCADE)
