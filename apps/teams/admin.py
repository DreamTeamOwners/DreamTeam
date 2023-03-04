from django.contrib import admin
from apps.teams.models import Team, TeamUser

# Register your models here.
admin.site.register(Team)
admin.site.register(TeamUser)

