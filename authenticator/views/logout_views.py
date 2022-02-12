from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.utils import timezone
from django.views.generic import View


class LogoutView(LoginRequiredMixin, View):
    ''' Logoutview will logout the current login user '''

    def get(self, request):
        logout(request)
        # Track logout time of user
        request.user.logout_datetime = timezone.now()
        request.user.save()
        return redirect('/')
