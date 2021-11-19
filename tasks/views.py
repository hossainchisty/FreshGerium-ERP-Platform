from django.shortcuts import render
from .models import Task
from .serializers import TaskSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated


class TaskAPIList(generics.ListAPIView):
    # permission_classes = [IsAuthenticated]
    queryset = Task.objects.all().order_by('-created_on')
    serializer_class = TaskSerializer

class CreateTask(generics.CreateAPIView):
    # permission_classes = [IsAuthenticated]
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class UpdateTask(generics.UpdateAPIView):
    # permission_classes = [IsAuthenticated]
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class RetrieveTask(generics.RetrieveAPIView):
    # permission_classes = [IsAuthenticated]
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class DestroyTask(generics.DestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Task.objects.all()
    serializer_class = TaskSerializer



