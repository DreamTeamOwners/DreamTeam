from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenRefreshView
)
from apps.users.views import (
    UserRegisterAPIView,
    CompanyRegisterAPIView,
    LoginView,
    UserDetailAPIView
)


urlpatterns = [
    path('register/', UserRegisterAPIView.as_view(), name='register'),
    path('company_register/', CompanyRegisterAPIView.as_view(), name='register'),

    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('login/', LoginView.as_view(), name='token'),

    path('user_detail/<int:id>/', UserDetailAPIView.as_view(), name='user_detail'),
]
