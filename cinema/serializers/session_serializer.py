from rest_framework import serializers
from cinema.serializers import MovieSerializer
from cinema.models import Session

class SessionSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    date = serializers.DateField()
    start_time = serializers.TimeField(source='start')
    end_time = serializers.SerializerMethodField()
    movie = serializers.SerializerMethodField()
    room = serializers.IntegerField(source='room.id')
    

    def get_movie(self, session: Session):
        movie = session.movie
        return MovieSerializer(movie).data


    def get_end_time(self, session: Session):
        return session.get_end_time()
