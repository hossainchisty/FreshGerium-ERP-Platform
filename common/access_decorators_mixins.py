from django.core.exceptions import PermissionDenied
from django.shortcuts import redirect


def unauthenticated_user(view_func):
    '''
    This function is used on the views that require authorization if not
    redirects to login page.
    '''
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect("dashboard")
        else:
            return view_func(request, *args, **kwargs)

    return wrapper_func


# def sales_access_required(function):
#     ''' this function is a decorator used to authorize if a user has sales access '''

#     def wrap(request, *args, **kwargs):
#         if (
#             request.user.role == "ADMIN"
#             or request.user.is_superuser
#             or request.user.has_sales_access
#         ):
#             return function(request, *args, **kwargs)
#         raise PermissionDenied

#     return wrap


from django.contrib.auth import REDIRECT_FIELD_NAME
from django.contrib.auth.decorators import user_passes_test


# add logic to check if user is is_founder
def is_founder_required(view_func=None, redirect_field_name=REDIRECT_FIELD_NAME,
                        login_url='admin:login'):
    """
    Decorator for views that checks that the user is logged in and is a staff
    member, redirecting to the login page if necessary.
    """
    actual_decorator = user_passes_test(
        lambda u: u.is_active and u.is_staff,
        login_url=login_url,
        redirect_field_name=redirect_field_name
    )
    if view_func:
        return actual_decorator(view_func)
    return actual_decorator
