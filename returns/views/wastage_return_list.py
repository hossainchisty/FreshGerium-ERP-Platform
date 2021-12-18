from django.shortcuts import render
from django.views.generic import View


class WastageReturnView(View):
    def get(self, request):
        return render(request, 'return/wastage_return.html')
