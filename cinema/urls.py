from django.urls import path
from rest_framework.routers import DefaultRouter
from cinema.views import MovieViewSet, SessionView, SeatView, MovieSessionSeatsView

router = DefaultRouter()
router.register(r'movies', MovieViewSet)

urlpatterns = [
    # seats from all sessions of given movie
    path('movies/<int:movie_id>/seats-per-session', MovieSessionSeatsView.as_view()),

    # seats from a given session
    path('seats/<int:session_id>', SeatView.as_view()), 

    # sessions that are playing a given movie
    path('session/<int:movie_id>', SessionView.as_view()),
]

urlpatterns += router.urls
