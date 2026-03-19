from rest_framework import serializers
from accounts.serializers import UserSerializer
from cinema.serializers import SessionSerializer


class TicketSerializer(serializers.Serializer):
    user = serializers.SerializerMethodField()
    seat = serializers.IntegerField()
    session = serializers.SerializerMethodField()


    def get_user(self, ticket):
        return UserSerializer(ticket.user).data
    

    def get_session(self, ticket):
        return SessionSerializer(ticket.session).data
