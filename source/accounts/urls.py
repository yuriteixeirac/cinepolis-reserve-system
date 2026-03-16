from django.urls import path
from source.accounts.views import register_user, login_user
from rest_framework_simplejwt.views import TokenVerifyView, TokenRefreshView


urlpatterns = [
    path('register/', register_user, name='register_user'),
    path('login/', login_user, name='login_user'),
    path('token/verify/', TokenVerifyView.as_view(), name='token-verify'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token-refresh')
]
