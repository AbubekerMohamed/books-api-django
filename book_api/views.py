from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from book_api.models import Book
from book_api.serializer import BookSerializer

class BookList(APIView):
    def get(self, request):
        books = Book.objects.all()
        serialized = BookSerializer(books, many=True)
        return Response(serialized.data)

class BookCreate(APIView):
    def post(self, request):
        serialized = BookSerializer(data = request.data)
        if serialized.is_valid():
            serialized.save()
            return Response(serialized.data)
        else:
            return Response(serialized.errors, status= status.HTTP_400_BAD_REQUEST)

class BookMutate(APIView):
    def get_book_by_pk(self,pk):
        try:
            book = Book.objects.get(pk=pk)
            return book
        except:
            return Response({
                "error": "Book does not exist"
            }, status=status.HTTP_404_NOT_FOUND)
    def get(self,request,pk):
        book = self.get_book_by_pk(pk)
        serializer = BookSerializer(book)
        return Response(serializer.data)
    def put(self, request, pk):
        book = self.get_book_by_pk(pk)
        serializer = BookSerializer(book, data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk):
        book = self.get_book_by_pk(pk)
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

        