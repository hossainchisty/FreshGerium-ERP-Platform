from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required
def password_verification(request):
    ''' Verify user previous password '''
    if request.method == "POST":
        valid_password = request.POST.get('password')
        if request.user.check_password(valid_password):
            return render(request, 'profiles/download_requested.html')
        else:
            messages.error(request, 'The password you entered is incorrect.')
            return render(request, 'profiles/password_verification.html')
    else:
        return render(request, 'profiles/password_verification.html')
