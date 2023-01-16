from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from book_api.models import Book
from book_api.serializer import BookSerializer

# Create your views here.
@api_view(['GET'])
def book_list(request):
    books = Book.objects.all()
    serialized = BookSerializer(books, many=True)
    return Response(serialized.data)

@api_view(['POST'])
def book_create(request):
    serialized = BookSerializer(data = request.data)
    if serialized.is_valid():
        serialized.save()
        return Response(serialized.data)
    else:
        return Response(serialized.errors, status= status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def book(request, pk):
    try:
        book = Book.objects.get(pk=pk)
    except:
        return Response({
            "error": "Book does not exist"
        }, status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = BookSerializer(book)
        return Response(serializer.data)
    if request.method == 'PUT':
        serializer = BookSerializer(book, data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'DELETE':
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)