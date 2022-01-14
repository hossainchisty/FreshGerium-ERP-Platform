from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
# from django.utils.decorators import method_decorator
from django.views.generic import View

# from utils.helper.decorators.filter import _currentUser


class NotificationView(LoginRequiredMixin, View):
    '''
    TODO:

    '''
    # @method_decorator(_currentUser())

    def get(self, request):
        return render(request, 'notifications/notifications.html')
