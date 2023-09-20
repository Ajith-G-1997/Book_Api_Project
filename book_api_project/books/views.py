from rest_framework import generics
from .models import Author, Book, Store
from .serializers import AuthorSerializer, BookSerializer, StoreSerializer
from rest_framework.generics import ListAPIView
from django.db.models import Count

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

class StoreListView(ListAPIView):
    serializer_class = StoreSerializer

    def get_queryset(self):
        # Use annotate to count the number of books for each store.
        return Store.objects.annotate(num_books=Count('books')).prefetch_related('books')
