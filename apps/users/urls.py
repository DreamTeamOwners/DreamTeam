from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenRefreshView
)
from apps.users.views import (
    MyObtainPairView,
    RegisterApiView,
    UserDetailApiView
)


urlpatterns = [
    path('login/', MyObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', RegisterApiView.as_view(), name='register'),

    path('detail/<int:id>/', UserDetailApiView.as_view(), name='user_detail')
]