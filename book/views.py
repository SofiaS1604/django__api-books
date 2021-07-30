from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Book, Author
from django.http import HttpResponse
from .serializers import BookSerializer, AuthorSerializer
from rest_framework.parsers import JSONParser
from rest_framework.generics import get_object_or_404


class BookView(APIView):
    def get(self, request):
        book = Book.objects.all()
        serializer = BookSerializer(book, many=True)
        return Response({'books': serializer.data})

    def post(self, request):
        book = JSONParser().parse(request)
        serializer = BookSerializer(data=book)
        if serializer.is_valid(raise_exception=True):
            book_saved = serializer.save()
        return Response({"success": "Book '{}' created successfully".format(book_saved.title)})

    def put(self, request, pk):
        saved_book = get_object_or_404(Book.objects.all(), pk=pk)
        data = JSONParser().parse(request)
        serializer = BookSerializer(instance=saved_book, data=data, partial=True)

        if serializer.is_valid(raise_exception=True):
            book_saved = serializer.save()

        return Response({
            "success": "Book '{}' updated successfully".format(book_saved.title)
        })

    def delete(self, request, pk):
        book = get_object_or_404(Book.objects.all(), pk=pk)
        book.delete()
        return Response({
            "message": "Book with id '{}' has been deleted".format(pk)
        }, status=204)


class AuthorView(APIView):
    def get(self, request):
        author = Author.objects.all()
        serializer = AuthorSerializer(author, many=True)
        return Response({'authors': serializer.data})

    def post(self, request):
        author = JSONParser().parse(request)
        serializer = AuthorSerializer(data=author)
        if serializer.is_valid(raise_exception=True):
            author_saved = serializer.save()
        return Response({"success": "Author '{}' created successfully".format(author_saved.first_name, author_saved.last_name)})

    def put(self, request, pk):
        saved_author = get_object_or_404(Author.objects.all(), pk=pk)
        data = JSONParser().parse(request)
        serializer = AuthorSerializer(instance=saved_author, data=data, partial=True)

        if serializer.is_valid(raise_exception=True):
            author_saved = serializer.save()

        return Response({
            "success": "Author '{}' updated successfully".format(author_saved.first_name, author_saved.last_name)
        })

    def delete(self, request, pk):
        author = get_object_or_404(Author.objects.all(), pk=pk)
        author.delete()
        return Response({
            "message": "Author with id '{}' has been deleted".format(pk)
        }, status=204)