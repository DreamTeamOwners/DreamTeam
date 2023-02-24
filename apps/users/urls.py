from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenRefreshView
)
from apps.users.views import (
    RegisterAPIView,
    LoginView,
    UserDetailAPIView,
    ProfileAPIView
)


urlpatterns = [
    path('register/', RegisterAPIView.as_view(), name='register'),

    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('login/', LoginView.as_view(), name='token'),

    path('user_detail/<int:id>/', UserDetailAPIView.as_view(), name='user_detail'),
    path('profile/', ProfileAPIView.as_view(), name='user_profile'),

]
