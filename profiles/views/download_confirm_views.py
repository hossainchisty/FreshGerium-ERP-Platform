from django.shortcuts import render


def download_confirm(request):
    return render(request, 'profiles/download_confirm.html')
