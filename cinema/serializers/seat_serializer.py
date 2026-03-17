from rest_framework import serializers
from cinema.models import Seat

class SeatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seat
        fields = ['id', 'room', 'status']
