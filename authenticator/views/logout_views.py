from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.views.generic import View


class SignOutView(LoginRequiredMixin, View):
    ''' Logoutview will logout the current login user '''

    def get(self, request):
        logout(request)
        return redirect('/')
