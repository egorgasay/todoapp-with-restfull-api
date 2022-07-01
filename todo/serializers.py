from rest_framework import serializers
from .models import Todo

# def required(value):
#     if value is None:
#         raise serializers.ValidationError('This field is required')
class TodoSerializer(serializers.ModelSerializer): # in documentation
    
    class Meta:
        model = Todo
        fields = '__all__'

class TodoListSerializer(serializers.ModelSerializer): # in documentation
    
    class Meta:
        model = Todo
        fields = '__all__'
        
class TaskSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Todo
        fields = '__all__'

class TodoSerializer2(serializers.ModelSerializer): # in documentation
    
    class Meta:
        model = Todo
        fields = ('done', )