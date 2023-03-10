from django.http import Http404
from django.shortcuts import get_object_or_404
from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView

from apps.users.models import MyUser, Profile
from apps.users.permissions import AnonPermission, IsOwnerOrReadOnly
from apps.users.serializers import (MyTokenObtainPairSerializer,
                                    MyUserRegisterSerializer,
                                    MyUserSerializer, ProfileDetailSerializer, ProfileUpdateSerializer)


class LoginView(TokenObtainPairView):
    permission_classes = (AnonPermission,)
    serializer_class = MyTokenObtainPairSerializer


class UserRegisterAPIView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = MyUserRegisterSerializer

    def post(self, request):
        serializer = MyUserRegisterSerializer(data=request.data)
        if serializer.is_valid():

            user = MyUser.objects.create(
                email=request.data['email'],
                username=request.data['username'],
                is_company=False
            )
            user.set_password(request.data['password'])
            user.save()
            profile = Profile.objects.create(
                user=user,
            )
            profile.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProfileDetailAPIView(APIView):
    permission_classes = [permissions.AllowAny]

    def get_object(self, id):
        try:
            return Profile.objects.get(user=id)
        except Profile.DoesNotExist:
            raise Http404

    def get(self, request, id):
        profile = self.get_object(id)
        serializers = ProfileDetailSerializer(profile)
        data = serializers.data
        return Response(data)


class ProfileUpdateAPIView(APIView):
    serializer_class = ProfileUpdateSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return get_object_or_404(Profile, user=self.request.user)

    def put(self, request):
        profile = self.get_object()
        serializer = ProfileUpdateSerializer(profile, data=request.data)
        if serializer.is_valid():
            serializer.save(user=self.request.user)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
