from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from apps.teams.models import Team,TeamUser
from apps.teams.serializers import TeamSerializer, TeamUserSerializer
from apps.users.models import MyUser
from django.views.generic.edit import FormView, CreateView
from django.urls import reverse_lazy
from .forms import TeamUserForm
from django.contrib import messages
from django.shortcuts import redirect
class CreateTeamAPIView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = TeamSerializer

    def post(self, request):
        serializer = TeamSerializer(data=request.data)
        if serializer.is_valid():
            team = Team.objects.create(
                name=request.data['name'],
                owner_id=request.user,
                description=request.data['description'],
                experience=request.data['experience'],
                links=request.data['links']
            )
            team.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#
# class TeamUserAPIView(APIView):
#     def post(self, request, team_id):
#         team = Team.objects.get(pk=team_id)
#         serializer = TeamUserSerializer(data=request.data)
#         if serializer.is_valid():
#             team_user = serializer.save(team_id=team)
#             return Response({'id': team_user.id}, status=status.HTTP_201_CREATED)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# class TeamUserAPIView(APIView):
#     def post(self, request, team_id):
#         team = Team.objects.get(pk=team_id)
#         serializer = TeamUserSerializer(data=request.data)
#         if serializer.is_valid():
#             team_user = serializer.save(team=team)
#             return Response({'id': team_user.id}, status=status.HTTP_201_CREATED)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TeamUserAPIView(LoginRequiredMixin, SuccessMessageMixin, FormView):
    form_class = TeamUserForm
    success_message = "Team member added successfully!"

    def get_success_url(self):
        return reverse_lazy('team-detail', kwargs={'pk': self.kwargs.get('pk')})

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['team'] = Team.objects.get(pk=self.kwargs.get('pk'))
        return kwargs

    def form_valid(self, form):
        team_user = form.save(commit=False)
        team_user.team = Team.objects.get(pk=self.kwargs.get('pk'))
        team_user.save()
        messages.success(self.request, self.success_message)
        return redirect(self.get_success_url())

    def form_invalid(self, form):
        messages.error(self.request, 'Error adding team member.')
        return redirect(self.get_success_url())
