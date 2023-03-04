from django import forms
from apps.teams.models import TeamUser
from apps.users.models import MyUser

class TeamUserForm(forms.ModelForm):
    user_id = forms.ModelChoiceField(queryset=MyUser.objects.all())

    class Meta:
        model = TeamUser
        fields = ('user_id',)

    def __init__(self, *args, **kwargs):
        team = kwargs.pop('team')
        super().__init__(*args, **kwargs)
        self.fields['user_id'].queryset = MyUser.objects.exclude(
            pk__in=team.team_users.values_list('user_id__pk', flat=True)
        )
