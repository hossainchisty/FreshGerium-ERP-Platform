from authenticator.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, render


def SignInView(request):
    ''' Sign in views '''
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = User.objects.filter(email=email).first()
        if user is None:
            messages.info(request, '%s Not found!' % email)
            return redirect('sign-in')

        profile = User.objects.filter(email=user).first()
        ''' User verification checks '''
        if not profile.is_verified:
            messages.info(request, 'Your account is not verified!')
            return redirect('sign-in')

        auth_user = authenticate(email=email, password=password)
        if auth_user is None:
            messages.info(request, 'Wrong credentials')
            return redirect('sign-in')
        login(request, auth_user)
        return redirect('dashboard')
    return render(request, 'authenticator/login.html')
