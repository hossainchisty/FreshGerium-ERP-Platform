from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from tasks.api.serializers.tasks_serializers import TaskSerializer
from tasks.models import Task


class TaskAPIList(generics.ListAPIView):
    '''
    ♻API endpoint that display all task.
    '''
    permission_classes = [IsAuthenticated]
    queryset = Task.objects.all().order_by('-created_on')
    serializer_class = TaskSerializer


class CreateTask(generics.CreateAPIView):
    '''
    ♻API endpoint that allows task to be created.
    '''
    permission_classes = [IsAuthenticated]
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class UpdateTask(generics.UpdateAPIView):
    '''
    ♻API endpoint that allows task to be updated.
    '''
    permission_classes = [IsAuthenticated]
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class RetrieveTask(generics.RetrieveAPIView):
    '''
    ♻API endpoint that allows task to be retrieved.
    '''
    permission_classes = [IsAuthenticated]
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class DestroyTask(generics.DestroyAPIView):
    '''
    ♻API endpoint that allows task to be deleted.
    '''
    permission_classes = [IsAuthenticated]
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
