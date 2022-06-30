from rest_framework import viewsets, permissions
from .models import Todo
from .serializers import TodoSerializer

class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all() # all our objects in database
    permission_classes = [permissions.AllowAny] 
    
    serializer_class = TodoSerializer # class of Serializer