# books/views.py
from rest_framework import generics
from .models import Author, Book
from .serializers import AuthorSerializer, BookSerializer
from rest_framework.views import APIView
from rest_framework.response import Response

class AuthorList(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class AuthorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class BookList(generics.ListCreateAPIView):
    queryset = Book.objects.select_related('author').all() 
    serializer_class = BookSerializer

class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.select_related('author').all()  
    serializer_class = BookSerializer


class First(APIView):
    def get(self, request):
        first_book = Book.objects.select_related('author').first()
        if first_book:
            author_name = first_book.author.name
            return Response({'author': author_name})
        else:
            return Response({'message': 'No movies found'})