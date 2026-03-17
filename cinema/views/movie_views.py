from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import AllowAny
from cinema.models import Movie
from cinema.serializers import MovieSerializer


class MovieViewSet(ReadOnlyModelViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [AllowAny]

    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
