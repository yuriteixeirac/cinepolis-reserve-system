from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import AllowAny
from cinema.serializers import MovieSessionSeatsSerializer
from cinema.models import Movie, Session


class MovieSessionSeatsView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [AllowAny]

    def get(self, request, movie_id=None):
        if not movie_id:
            return Response({
                'error': 'No movie was provided.'
            }, status=400)
        
        movie = get_object_or_404(Movie, pk=movie_id)
        sessions = Session.objects.filter(movie=movie)

        return Response(
            MovieSessionSeatsSerializer(
                sessions, many=True
            ).data,
            status=200
        )
