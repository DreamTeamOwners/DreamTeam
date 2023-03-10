from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from .models import MyUser, Profile


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        token['email'] = user.email

        return token


class MyUserRegisterSerializer(serializers.ModelSerializer):

    class Meta:
        model = MyUser
        fields = [
            'id',
            'email',
            'username',
            'password',
        ]


class MyUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = MyUser
        fields = ['id', 'username', 'email']


class ProfileDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = '__all__'


class ProfileUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields =['first_name', 'job_position',
                 'last_name', 'phone_number', 'country', 'description', 'experience', 'github']






