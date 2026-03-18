from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from cinema.serializers import SeatSerializer
from cinema.models import Seat, Session


class SeatView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]


    def get(self, request, session_id: int):
        if not session_id:
            return Response({
                'error': 'No session id provided.'
            }, status=400)
        
        session = get_object_or_404(Session, pk=session_id)
        seats = Seat.objects.filter(room=session.room)

        serialized_seats = SeatSerializer(seats, many=True)

        return Response(serialized_seats.data, status=200)
