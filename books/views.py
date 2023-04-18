from django.shortcuts import render
from rest_framework.views import APIView

from .models import Book
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import BookSerializer
from rest_framework import generics
from rest_framework.generics import get_object_or_404
from rest_framework.viewsets import ModelViewSet


# Create your views here.


@api_view(['GET'])
def book_list_View(request, *args, **kwargs):
    books = Book.objects.all()
    serializer = BookSerializer(books, many=True)
    return Response(serializer.data)


# class BookListApi(generics.ListAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer

class BookListApiView(APIView):
    def get(self, request):
        books = Book.objects.all()
        serializer_data = BookSerializer(books, many=True).data
        data = {
            "status": f"Returned {len(books)} books",
            "books": serializer_data
        }
        return Response(data)


class BookCreateApiView(APIView):
    def post(self, request):
        data = request.data
        serializ_data = BookSerializer(data=data)
        if serializ_data.is_valid():
            books = serializ_data.save()
            context = {
                "status": "books are saved to the database",
                "books": data
            }
            return Response(context)


# class BookDetailApiView(generics.RetrieveAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer

class BookDetailApiView(APIView):
    def get(self,  request, pk):
        try:
            book = Book.objects.get(id=pk)
            serializer_data = BookSerializer(book).data
            context = {
                "status": "Succesful",
                "serializer_data": serializer_data
            }
            print(serializer_data)
            return Response(context)
        except Exception:
            context = {
                "status": "Doas not exists",
                "message": "book is not found"
            }
            return Response(context)


# class BookDeleteApiView(generics.DestroyAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer
class BookDeleteApiView(APIView):
    def delete(self, request, pk):
        try:
            book = Book.objects.get(id=pk)
            book.delete()
            return Response({
                "status": True,
                "message": "succesfully deleted",
            })
        except Exception:

            return Response({
                "status": False,
                "message": "book is not found",
            })


# class BookUpdateApiView(generics.UpdateAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer
class BookUpdateApiView(APIView):
    def put(self, request, pk):
        book = get_object_or_404(Book.objects.all(), id=pk)
        data = request.data
        serializer = BookSerializer(instance=book, data=data, partial=True)
        if serializer.is_valid():
            book_saved = serializer.save()
        return (Response(
            {
                "status": True,
                "message": "Book updated successfully"
            }
        )
        )




class BookListCreateApiView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookViewset(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

