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
                 'last_name', 'phone_number', 'country', 'description', 'city', 'github',
                 'experience_start_time', 'experience_end_time', 'experience_title', 'experience_description',
                 'education_end_year', 'education_place', 'education_title', 'image']


class MyProfileSerializer(serializers.ModelSerializer):
    completion_percentage = serializers.SerializerMethodField()

    class Meta:
        model = Profile
        fields = ['user', 'job_position', 'first_name', 'last_name', 'phone_number', 'country', 'city', 'description', 'github', 'image', 'experience_start_time', 'experience_end_time', 'experience_title', 'experience_description', 'education_end_year', 'education_place', 'education_title', 'completion_percentage']

    def get_completion_percentage(self, obj):
        return obj.get_completion_percentage()


