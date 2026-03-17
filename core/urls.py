from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView, TokenRefreshView
)

urlpatterns = [
    path('api/', include('accounts.urls')),
    path('cinema/', include('cinema.urls')),
]
