from django.apps import AppConfig


class ExpenseConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'expense'
    icon = 'fa fa-minus-square-o'

    def ready(self):
        import expense.signals
