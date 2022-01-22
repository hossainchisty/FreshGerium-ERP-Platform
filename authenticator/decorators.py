from django.shortcuts import redirect


def unauthenticated_user(view_func):
    '''
    Decorator for views that checks if the user is authenticated, if not
    redirects to login page.
    '''
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect("dashboard")
        else:
            return view_func(request, *args, **kwargs)

    return wrapper_func
