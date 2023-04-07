from django.shortcuts import get_object_or_404
from rest_framework import permissions, status, generics, filters
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.users.serializers import *


class CommentCreateAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = CommentPostSerializer

    def post(self, request, group_id):
        group = get_object_or_404(Group, id=group_id)
        serializer = CommentPostSerializer(
            data=request.data,
            context={'request': request,
                     'group': group
                     }
        )
        if serializer.is_valid():
            serializer.save()
            return Response(status=201)
        return Response(status=404)


class CommentUpdateAPIView(APIView):
    """
    Only authorized and author can put a comment
    """
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = CommentUpdateSerializer

    def put(self, request, pk, format=None):
        snippet = get_object_or_404(Comment, id=pk)
        serializer = CommentUpdateSerializer(
            snippet,
            data=request.data,
            context={'request': request}
        )
        if serializer.is_valid():
            if request.user == snippet.username:
                serializer.save()
                return Response(serializer.data)
            return Response("you are not author")
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


class CommentDeleteAPIView(APIView):
    """
    Only authorized and author can delete a comment
    """
    permission_classes = [permissions.IsAuthenticated]

    def delete(self, request, pk, format=None):
        snippet = get_object_or_404(Comment, id=pk)

        if request.user == snippet.username:
            snippet.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(
            {"you are not author"},
            status=status.HTTP_400_BAD_REQUEST
        )
