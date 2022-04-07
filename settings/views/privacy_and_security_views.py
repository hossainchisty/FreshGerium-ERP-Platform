from analytics.models import DeviceTrack
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import View


class PrivacyAndSecurityView(LoginRequiredMixin, View):
    '''
    TODO: 
    '''

    def get(self, request):
        context = {
            'device': DeviceTrack.objects.all()
        }
        return render(request, 'settings/privacy_and_security.html', context)
