from django.apps import AppConfig


class AuthenticatorConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'authenticator'

    def ready(self):
        import authenticator.signals
