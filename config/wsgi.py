import os

from django.core.wsgi import get_wsgi_application

# Note: Don't forget to add production file
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.development')

application = get_wsgi_application()
