from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenRefreshView
)
from apps.teams.views import (
    CreateTeamAPIView, TeamUserAPIView
)


urlpatterns = [
    path('createteam/', CreateTeamAPIView.as_view(), name='createteam'),
    path('<int:pk>/addteamuser/', TeamUserAPIView.as_view(), name='addteamuser'),


]