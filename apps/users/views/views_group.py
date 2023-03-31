from django.shortcuts import get_object_or_404
from rest_framework import permissions, status, generics, filters
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.users.serializers import *


class CreateGroupAPIView(APIView):
    serializer_class = GroupSerializer

    def post(self, request):
        serializer = GroupSerializer(
            data=request.data, context={'request': request}
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GroupListAPIView(APIView):

    def get(self, request):
        queryset = Group.objects.all()
        serializers = GroupListSerializers(queryset, many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)


class GroupDetailAPIView(APIView):

    def get(self, request, pk):
        queryset = get_object_or_404(Group, id=pk)
        serializers = GroupDetailSerializer(queryset)
        return Response(serializers.data, status=status.HTTP_200_OK)


class GroupUpdateAPIView(APIView):
    serializer_class = GroupListSerializers

    def put(self, request, pk):
        queryset = get_object_or_404(Group, id=pk)
        serializer = GroupListSerializers(queryset, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GroupDeleteAPIView(APIView):
    serializer_class = GroupSerializer

    def delete(self, request, pk):
        queryset = get_object_or_404(Group, id=pk)
        queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
