from django.apps import AppConfig


class ProductsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'products'
    icon = 'fa fa-product-hunt'

    def ready(self):
        import products.signals
