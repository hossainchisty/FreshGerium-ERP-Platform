from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import redirect, render


@login_required
def passwordChangeView(request):
    """ A form that lets a user change their password by entering their old
    password.
    """
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = PasswordChangeForm(user=request.user, data=request.POST)
            request.user.is_verified = True
            if form.is_valid():
                form.save()
                # Update the session hash to prevent session fixation attacks.
                update_session_auth_hash(request, form.user)
                messages.success(request, 'Password Change Successfully!')
                return redirect('/')
        else:
            form = PasswordChangeForm(user=request.user)
        return render(request, 'settings/password_change.html', {'form': form})
    else:
        return redirect('login')
