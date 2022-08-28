from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import View


class CustomerGraphViews(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'analytics/customer_graph.html')
