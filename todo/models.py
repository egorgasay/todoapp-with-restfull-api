from pydoc import describe
from turtle import title
from django.db import models
import datetime
# Create your models here.

class Todo(models.Model):
    title = models.CharField(max_length=200, blank=False)
    description = models.CharField(max_length=300, blank=False)
    date = models.DateField(max_length=30, blank=False)
    done = models.BooleanField(default=False)
    
    def __str__(self) -> str:
        return self.title
