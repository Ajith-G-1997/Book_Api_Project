
from rest_framework import serializers
from .models import Author, Book,Store

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
# class StoreSerializer(serializers.ModelSerializer):
#     books = BookSerializer(many=True)  

#     class Meta:
#         model = Store
#         fields = '__all__'

class StoreSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True)  # Use BookSerializer to nest book details

    class Meta:
        model = Store
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        book_count = len(representation['books'])
        representation['name'] = f"{instance.name} has {book_count} {'book' if book_count == 1 else 'books'}"
        return representation