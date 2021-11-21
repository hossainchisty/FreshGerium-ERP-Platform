from django.urls import path
from leads.api.views import leads_views as views

urlpatterns = [
    path('list/', views.LeadAPIList.as_view()),
    path('create/', views.CreateLead.as_view()),
    path('update/<int:pk>/', views.UpdateLead.as_view()),
    path('retrieve/<int:pk>/', views.RetrieveLead.as_view()),
    path('destory/<int:pk>/', views.DestroyLead.as_view())
]
