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


class GroupAddAPIView(APIView):

    def post(self, request, group_id):
        search_terms = request.data.get('search_terms')
        if search_terms:
            users = MyUser.objects.filter(username__in=search_terms)
            if users:
                group = Group.objects.get(id=group_id)
                for user in users:
                    group.members.add(user)
                return Response(
                    {'message': f'Successfully added {len(users)} members to the group.'},
                    status=status.HTTP_200_OK)
        return Response(
            {'message': 'No users found.'},
            status=status.HTTP_404_NOT_FOUND
        )


class GroupRemoveAPIView(APIView):

    def post(self, request, group_id):
        users = request.data.get('user_id')
        if users:
            try:
                group = Group.objects.get(id=group_id)
                users = MyUser.objects.filter(username__in=users)
                for user in users:
                    group.members.remove(user)
                return Response(
                    {'message': f'Successfully removed user {users} from group {group_id}.'},
                    status=status.HTTP_200_OK)
            except Group.DoesNotExist:
                return Response(
                    {'message': 'Group does not exist.'},
                    status=status.HTTP_404_NOT_FOUND)
            except MyUser.DoesNotExist:
                return Response(
                    {'message': 'User does not exist.'},
                    status=status.HTTP_404_NOT_FOUND)
        return Response(
            {'message': 'No user ID provided.'},
            status=status.HTTP_400_BAD_REQUEST)
