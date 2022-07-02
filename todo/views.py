from django.http import HttpResponse, HttpResponseNotAllowed, HttpResponseNotFound
from django.shortcuts import render
from rest_framework import viewsets, generics
from .serializers import *
from .models import Todo
from rest_framework import mixins
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
class TodoListView(generics.ListAPIView):
    serializer_class = TodoSerializer
    queryset = Todo.objects.all()

class TodoIdsView(generics.ListAPIView):
    serializer_class = TodoSerializerIdOnly
    queryset = Todo.objects.all()

class TodoCreateView(generics.CreateAPIView):
    serializer_class = TodoSerializer


class TodoTasksViewSet(viewsets.ModelViewSet): 
    queryset = Todo.objects.all().order_by('title')
    serializer_class = TodoSerializer


class DestroyView(generics.DestroyAPIView): 
    serializer_class = TodoSerializer
    queryset = Todo.objects.all()


class UpdateView(generics.UpdateAPIView): 
    serializer_class = TodoSerializer2
    queryset = Todo.objects.all()

def pageNotFound(request, exception):
    return HttpResponseNotFound("<h1>Page Not Found<h1>")