from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.utils.decorators import method_decorator
from django.views.generic import View
from utils.helper.decorators.filter import _currentUser


class LogoutView(LoginRequiredMixin, View):
    ''' Logoutview will logout the current login user '''

    @method_decorator(_currentUser())
    def get(self, request):
        logout(request)
        return redirect('/')
