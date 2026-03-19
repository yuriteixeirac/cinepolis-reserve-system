from django.urls import path
from accounts.views import RegisterView
from rest_framework_simplejwt.views import TokenVerifyView, TokenRefreshView, TokenObtainPairView


urlpatterns = [
    path('register/', RegisterView.as_view(), name='register_user'),
    path('login/', TokenObtainPairView.as_view(), name='login_user'),
    path('token/verify/', TokenVerifyView.as_view(), name='token-verify'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token-refresh')
]
