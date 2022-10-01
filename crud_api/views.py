from django.shortcuts import render
from rest_framework import generics
from . serializer import *
from . models import *

# Create your views here.


class ListTodo(generics.ListAPIView):
    queryset = ToDo.objects.all()
    serializer_class = TodoSerializer


class Details(generics.RetrieveUpdateAPIView):
    queryset = ToDo.objects.all()
    serializer_class = TodoSerializer


class CreateToDo(generics.CreateAPIView):
    queryset = ToDo.objects.all()
    serializer_class = TodoSerializer


class DeleteTodo(generics.DestroyAPIView):
    queryset = ToDo.objects.all()
    serializer_class = TodoSerializer

