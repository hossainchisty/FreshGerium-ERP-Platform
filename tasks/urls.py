from django.urls import include, path

urlpatterns = [
    path('api/v1/', include('tasks.api.urls.tasks_urls'))
]
