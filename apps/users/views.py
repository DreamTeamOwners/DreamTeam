from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView

from .models import Account
from .permissions import AnonPermissionOnly
from .serializers import MyTokenObtainPairSerializer
from django.contrib.auth.models import User
from .serializers import AccountSerializers
from rest_framework import permissions


class MyObtainPairView(TokenObtainPairView):
    permission_classes = (AnonPermissionOnly,)
    serializer_class = MyTokenObtainPairSerializer


class RegisterApiView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = AccountSerializers

    def post(self, request):
        serializers = AccountSerializers(data=request.data)
        if serializers.is_valid():
            user = User.objects.create()
            user.set_password(request.data['password'])
            user.save()
            account = Account.objects.create(
                user=user,
                phone_number=request.data['phone_number'],
                username=request.data['username'],
                email=request.data['email'],
                first_name=request.data['first_name'],
                last_name=request.data['last_name'],
            )
            account.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


