from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView

from apps.users.models import MyUser
from apps.users.permissions import AnonPermission
from apps.users.serializers import MyTokenObtainPairSerializer, MyUserSerializer


class LoginView(TokenObtainPairView):
    permission_classes = (AnonPermission,)
    serializer_class = MyTokenObtainPairSerializer


class RegisterAPIView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = MyUserSerializer

    def post(self, request):
        serializer = MyUserSerializer(data=request.data)
        if serializer.is_valid():
            user = MyUser.objects.create(
                email=request.data['email'],
                username=request.data['username'],
                first_name=request.data['first_name'],
                last_name=request.data['last_name'],
            )
            user.set_password(request.data['password'])
            user.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
