from django.shortcuts import render
from rest_framework.authentication import TokenAuthentication, SessionAuthentication

from rest_framework.viewsets import ModelViewSet


from .models import Category, Video, File
from .serializers import CategorySerializer, VideoSerializer, FileSerializer

# Create your views here.


""" This view for Category model with using ModelViewSet """


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    authentication_classes = (TokenAuthentication, SessionAuthentication)


""" This view for Video model with using ModelViewSet """


class VideoViewSet(ModelViewSet):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    authentication_classes = (TokenAuthentication, SessionAuthentication)


""" This view for File model with using ModelViewSet """


class FileViewSet(ModelViewSet):
    queryset = File.objects.all()
    serializer_class = FileSerializer
    authentication_classes = (TokenAuthentication, SessionAuthentication)
