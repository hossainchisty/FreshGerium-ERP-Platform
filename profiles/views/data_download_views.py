from django.contrib.auth.decorators import login_required
from django.core.validators import validate_email
from django.shortcuts import redirect, render


@login_required
def data_download(request):
    return render(request, 'profiles/data_download.html')
