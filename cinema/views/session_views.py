from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import AllowAny
from cinema.models import Session
from cinema.serializers import SessionSerializer


class SessionView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [AllowAny]


    def get(self, request, movie_id=None):
        if not movie_id:
            return Response({
                'error': 'No movie was specified.'
            }, status=200)
        
        sessions = Session.objects.filter(movie=movie_id)
        serialized_sessions = SessionSerializer(sessions, many=True)
        
        return Response(serialized_sessions.data, status=200)
