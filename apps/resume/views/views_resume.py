from django.http import Http404
from django.shortcuts import get_object_or_404
from rest_framework import permissions, status, generics, filters
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import status

from apps.resume.models import Resume
from apps.resume.serializers import ResumeSerializer, LanguageSerializer, MyResumeSerializer


class ResumeCreateView(APIView):
    serializer_class = ResumeSerializer

    def post(self, request):
        serializer = ResumeSerializer(
            data=request.data,
            context={"request": request}
        )
        if serializer.is_valid():
            serializer.save()
            return Response(status=201)
        return Response(status=404)


class LanguageCreatView(APIView):
    serializer_class = LanguageSerializer

    def post(self, request):
        serializer = LanguageSerializer(
            data=request.data,
            context={"request": request}
        )
        if serializer.is_valid():
            serializer.save()
            return Response(status=201)
        return Response(status=404)


class MyResumeView(APIView):

    def get(self, request):
        resume = Resume.objects.filter(user=request.user).first()
        serializer = MyResumeSerializer(resume)
        return Response(serializer.data)
