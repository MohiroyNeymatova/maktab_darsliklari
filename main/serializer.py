from rest_framework import serializers
from .models import *


class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name']


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 1
        model = Book
        fields = '__all__'


