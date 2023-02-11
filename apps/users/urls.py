from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenRefreshView
)
from apps.users.views import (
    MyObtainPairView,
    RegisterApiView,
)


urlpatterns = [
    path('login/', MyObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', RegisterApiView.as_view(), name='vendor_register'),
]