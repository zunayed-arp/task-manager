from django.shortcuts import render
from rest_framework import viewsets
from .serializers import TodoSerializer
from .models import Todo

class TodoView(viewsets.ModelViewSet):
    "Viewset for CRUD API"
    serializer_class = TodoSerializer
    queryset = Todo.objects.all()
