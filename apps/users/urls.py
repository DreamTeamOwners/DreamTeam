from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenRefreshView
)
from apps.users.views import (
    RegisterAPIView,
    LoginView
)


urlpatterns = [
    path('register/', RegisterAPIView.as_view(), name='register'),

    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('login/', LoginView.as_view(), name='token'),
]
