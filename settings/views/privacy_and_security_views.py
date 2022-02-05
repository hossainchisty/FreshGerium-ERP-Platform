from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import View


class PrivacyAndSecurityView(LoginRequiredMixin, View):
    '''
    TODO: 
    '''

    def get(self, request):
        return render(request, 'settings/privacy_and_security.html')
