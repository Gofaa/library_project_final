from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import Book


class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = ('title', 'subtitle', 'author', 'isbn', 'price','id')

    # def validate(self, data):
    #     title = data.get('title', None)
    #     author = data.get('author', None)
        # if not title.isalpha():
        #     raise ValidationError(
        #         {
        #             "status": False,
        #             "message": "Kitobni sarlavhasi harflardan tashkil topishi kerak",
        #         }
        #     )
        # return data
        # if Book.objects.filter(title=title, author=author).exists():
        #     raise ValidationError(
        #         {
        #             "status": False,
        #             "message": "Kitob muallifi va sarlavhasi bir hil bo'lgan kitobni yuklay olmaysiz"
        #         }
        #     )
        # return data

