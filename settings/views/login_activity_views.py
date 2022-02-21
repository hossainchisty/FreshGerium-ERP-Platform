from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import View


class LoginActivityView(LoginRequiredMixin, View):
    '''
    TODO: We need to get user login activity device type from IP address and location map.
    '''

    def get(self, request):
        return render(request, 'settings/login_activity.html')
