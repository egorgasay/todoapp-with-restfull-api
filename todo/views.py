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
    serializer_class = TodoListSerializer
    queryset = Todo.objects.all()

# class TodoDeleteView(generics.DeleteAPIView):
#     serializer_class = TodoSerializer
    
class TodoCreateView(generics.CreateAPIView):
    serializer_class = TodoSerializer

class TodoTasksViewSet(viewsets.ModelViewSet): 
    queryset = Todo.objects.all().order_by('title')
    serializer_class = TodoSerializer

class TodoMarkAsDoneViewSet(mixins.DestroyModelMixin): 
    queryset = Todo.objects.all().order_by('title')
    serializer_class = TodoSerializer

class DestroyView(generics.DestroyAPIView): 
    serializer_class = TodoSerializer
    queryset = Todo.objects.all()

class UpdateView(generics.UpdateAPIView): 
    serializer_class = TodoSerializer2
    queryset = Todo.objects.all()

class RetrieveUpdateDeleteItem(
    mixins.DestroyModelMixin,
    GenericAPIView
):

    serializer_class = TodoSerializer
    queryset = Todo.objects.all()

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

class Step2ViewSet(viewsets.ModelViewSet):
    serializer_class = TodoSerializer

    def get_queryset(self):
        return Todo.objects.filter(pk=self.request.Todo.done)