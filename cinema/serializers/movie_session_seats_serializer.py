from rest_framework import serializers
from cinema.serializers import SeatSerializer


class MovieSessionSeatsSerializer(serializers.Serializer):
    session_id = serializers.IntegerField(source='id')
    start = serializers.TimeField()
    date = serializers.DateField()
    seats = serializers.SerializerMethodField()


    def get_seats(self, session):
        all_seats = session.room.seat_set.all()
        return [SeatSerializer(seat).data for seat in all_seats]
