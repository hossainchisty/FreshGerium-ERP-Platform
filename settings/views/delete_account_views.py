from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import View


class DeleteAccountView(LoginRequiredMixin, View):
    '''
    TODO: We need to implement the logic to delete the user account
    before delete account performs we need to verify logged in user password.
    '''

    def get(self, request):
        return render(request, 'settings/account_delete.html')
