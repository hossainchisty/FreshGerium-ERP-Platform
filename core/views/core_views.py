from django.shortcuts import render
from django.template import RequestContext
from django.views.generic import View


class Dashboard(View):
    def get(self, request):
        ''''
        Main dashboard view for the application.
        '''

        return render(request, 'core/dashboard.html')
