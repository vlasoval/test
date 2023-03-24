from .models import Author,Book
from rest_framework import serializers

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['pk', 'name']

class BookSerializer(serializers.ModelSerializer):
    author=AuthorSerializer(many=True)
    class Meta:
        model = Book
        fields = ['pk', 'title', 'author']