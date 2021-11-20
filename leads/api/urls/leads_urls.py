from django.urls import path
from leads.api.views import leads_views

urlpatterns = [
    path('list/', leads_views.LeadAPIList.as_view()),
    path('create/', leads_views.CreateLead.as_view()),
    path('update/<int:pk>/', leads_views.UpdateLead.as_view()),
    path('retrieve/<int:pk>/', leads_views.RetrieveLead.as_view()),
    path('destory/<int:pk>/', leads_views.DestroyLead.as_view())
]
