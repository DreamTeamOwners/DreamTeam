from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from .models import Team, TeamUser
from ..users.models import MyUser


class TeamSerializer(serializers.ModelSerializer):

    class Meta:
        model = Team
        fields = [
            'id',
            'name',
            'description',
            'experience',
            'links',
        ]
class TeamUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamUser
        fields = ('user_id',)

    def validate_user_id(self, value):
        # Check that the user with the given ID exists in the database
        if not MyUser.objects.filter(pk=value).exists():
            raise serializers.ValidationError('User with ID {} does not exist'.format(value))
        return value
