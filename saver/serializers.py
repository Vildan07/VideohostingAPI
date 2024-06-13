from rest_framework import serializers
from .models import Category, Video, File


""" This serializer is used to serialize Category objects """


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


""" This serializer is used to serialize Video objects """


class VideoSerializer(serializers.ModelSerializer):
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Video
        fields = '__all__'


""" This serializer is used to serialize File objects """


class FileSerializer(serializers.ModelSerializer):
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = File
        fields = '__all__'

