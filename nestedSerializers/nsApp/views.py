from django.shortcuts import render
from .models import Author,Book
from .serializers import AuthorSerializer,BookSerializer
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination,LimitOffsetPagination
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated,DjangoModelPermissions
# Create your views here.
class AuthorPagination(PageNumberPagination):
    page_size = 2
    
class AuthorListView(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    pagination_class = AuthorPagination
    #authentication_classes = [BasicAuthentication]
    #permission_classes = [IsAuthenticated,DjangoModelPermissions]

class AuthorDetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class BookListView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookDetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer