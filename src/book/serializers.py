from .models import Author,Book
from rest_framework import serializers

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['pk', 'name']

class BookSerializer(serializers.ModelSerializer):
    author=AuthorSerializer(many=True, allow_empty=False)

    class Meta:
        model = Book
        fields = ['pk', 'title', 'author']

    def create(self, validated_data):
        author_data = validated_data.pop('author')
        book = Book.objects.create(**validated_data)

        for author in author_data:
            author = Author.objects.create(**author)
            book.author.add(author)

        book.save()
        return book