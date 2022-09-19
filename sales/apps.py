from django.apps import AppConfig


class SalesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'sales'
    icon = 'fa fa-shopping-basket'

    def ready(self):
        import sales.signals
