from django.apps import AppConfig


class AuthenticatorConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'authenticator'
    verbose_name = 'User Accounts'
    verbose_name_plural = 'User Accounts'

    def ready(self):
        import authenticator.signals
