from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializer import *


@api_view(['GET'])
def get_language(request):
    return Response(LanguageSerializer(Language.objects.all(), many=True).data)


@api_view(['GET'])
def get_categories(request):
    return Response(CategorySerializer(Category.objects.all(), many=True).data)


@api_view(['GET'])
def get_books_by_language(request, pk):
    return Response(BookSerializer(Book.objects.filter(language_id=pk), many=True).data)


@api_view(['GET'])
def get_all_books(request):
    return Response(BookSerializer(Book.objects.all(), many=True).data)


@api_view(['GET'])
def get_books_by_category(request, pk):
    return Response(BookSerializer(Book.objects.filter(category_id=pk), many=True).data)

