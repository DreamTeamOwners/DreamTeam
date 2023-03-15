from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenRefreshView
)
from apps.users.views import (
    UserRegisterAPIView,
    LoginView,
    ProfileDetailAPIView,
    ProfileUpdateAPIView,
    MyProfileAPIView
    )


urlpatterns = [
    path('register/', UserRegisterAPIView.as_view(), name='register'),

    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('login/', LoginView.as_view(), name='token'),

    path('profile_detail/<int:id>/', ProfileDetailAPIView.as_view(), name='profile_detail'),
    path('my_profile_detail/', MyProfileAPIView.as_view(), name='my_profile_detail'),
    path('profile_update/', ProfileUpdateAPIView.as_view(), name='profile_update')
]
