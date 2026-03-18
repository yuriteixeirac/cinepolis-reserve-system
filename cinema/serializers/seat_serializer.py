from rest_framework import serializers
from cinema.models import Ticket
from redis import Redis

redis = Redis()

class SeatSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    room = serializers.IntegerField()
    status = serializers.SerializerMethodField()


    def get_status(self, seat):
        session_id = self.context.get('session_id')

        if Ticket.objects.filter(seat_id=seat.id, session_id=session_id).exists():
            return 'purchased'
        
        if redis.exists(f'seat_lock:{session_id}:{seat.id}'):
            return 'reserved'
        
        return 'available'
        