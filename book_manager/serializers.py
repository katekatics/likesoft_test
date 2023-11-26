from rest_framework import serializers

from .models import Book


class BookSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=200)
    author = serializers.CharField(max_length=100)
    pub_year = serializers.IntegerField()
    isbn = serializers.CharField(max_length=13)

    class Meta:
        model = Book
        fields = ('id', 'name', 'author', 'pub_year', 'isbn')

