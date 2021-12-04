from django.shortcuts import render
from django.views.generic import View


class Dashboard(View):
    def get(self, request):
        ''''
        Main dashboard view 👈🏻
        '''
        return render(request, 'core/dashboard.html')
