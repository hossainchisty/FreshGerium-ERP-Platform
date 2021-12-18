from django.shortcuts import render
from django.views.generic import View


class ReturnView(View):
    def get(self, request):
        return render(request, 'return/return.html')
