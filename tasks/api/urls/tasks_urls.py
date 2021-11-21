from django.urls import path
from tasks.api.views import tasks_views as views

urlpatterns = [
    path('list/', views.TaskAPIList.as_view()),
    path('create/', views.CreateTask.as_view()),
    path('update/<int:pk>/', views.UpdateTask.as_view()),
    path('retrieve/<int:pk>/', views.RetrieveTask.as_view()),
    path('destory/<int:pk>/', views.DestroyTask.as_view())
]
