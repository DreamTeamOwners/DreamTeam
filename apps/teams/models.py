from django.db import models
from apps.users.models import MyUser


class Team(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False, unique=True)
    owner_id = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    description = models.CharField(max_length=255, null=False, blank=False)
    experience = models.CharField(max_length=255, null=False, blank=False)
    links = models.CharField(max_length=255, null=False, blank=False)


class TeamUser(models.Model):
    user_id = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name='team_users')
    team_id = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='team_users')

