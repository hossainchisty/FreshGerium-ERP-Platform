from django.urls import path

from . views import (
    TaskAPIList,
    CreateTask,
    UpdateTask,
    RetrieveTask,
    DestroyTask,
)

urlpatterns = [
    path('list/', TaskAPIList.as_view()),
    path('create/', CreateTask.as_view()),
    path('update/<int:pk>/', UpdateTask.as_view()),
    path('retrieve/<int:pk>/', RetrieveTask.as_view()), 
    path('destory/<int:pk>/', DestroyTask.as_view())                          
]

'''
#? API endpoint of tasks
http://127.0.0.1:8000/tasks/list/
http://127.0.0.1:8000/tasks/create
http://127.0.0.1:8000/tasks/update/<int:pk>/
http://127.0.0.1:8000/tasks/retrieve/<int:pk>/
http://127.0.0.1:8000/tasks/destory/<int:pk>/
'''