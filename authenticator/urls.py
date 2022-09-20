from authenticator.views.login_views import SignInView
from authenticator.views.logout_views import SignOutView
from authenticator.views.password_reset import PasswordResetView
from authenticator.views.register_views import RegisterView, Success, Tokensend
from authenticator.views.verify_token import VerifyToken
from django.contrib.auth import views as auth_views
from django.urls import path

urlpatterns = [
    path('sign-up/', RegisterView, name='sign-up'),
    path('sign-in/', SignInView, name='sign-in'),
    path('sign-out/', SignOutView.as_view(), name='sign-out'),
    path('tokensent/', Tokensend, name='token_send'),
    path('success', Success, name='success'),
    path('verify/<token>', VerifyToken, name='verify'),

    # Password Reset with email
    path("password_reset", PasswordResetView.as_view(), name="password_reset"),
    path('password_reset/done/',
         auth_views.PasswordResetDoneView.as_view(template_name='authenticator/password/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name="authenticator/password/password_reset_confirm.html"), name='password_reset_confirm'),
    path('reset/done/',
         auth_views.PasswordResetCompleteView.as_view(template_name='authenticator/password/password_reset_complete.html'), name='password_reset_complete'),

]
