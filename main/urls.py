from django.urls import path
from .views import *

urlpatterns = [
    path('get_language/', get_language),
    path('get_categories/', get_categories),
    path('get_books_by_language/<int:pk>/', get_books_by_language),
    path('get_all_books/', get_all_books),
    path('get_books_by_category/<int:pk>/', get_books_by_category)
]
