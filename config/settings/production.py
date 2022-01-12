# Override base.py settings here
import os

import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration

from config.settings.base import *

sentry_sdk.init(
    dsn=os.getenv('SENTRY_DNS'),
    integrations=[DjangoIntegration()],

    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    # We recommend adjusting this value in production.
    # traces_sample_rate=1.0,

    # If you wish to associate users to errors (assuming you are using
    # django.contrib.auth) you may enable sending PII data.
    send_default_pii=False
)



DEBUG = False

# Security Principles🛡
# SECURE_SSL_REDIRECT = True
# Whether the session cookie should be secure (https:// only).
# SESSION_COOKIE_SECURE = False
# SECURE_BROWSER_XSS_FILTER = True
# SECURE_HSTS_SECONDS = 31536000
# SECURE_HSTS_INCLUDE_SUBDOMAINS = True
# SECURE_HSTS_PRELOAD = True
# SECURE_CONTENT_TYPE_NOSNIFF = True
# CSRF_COOKIE_SECURE = True

try:
    from config.settings.local import *
except ImportError:
    pass
