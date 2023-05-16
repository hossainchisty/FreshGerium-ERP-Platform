# flake8: noqa

"""
Title: Freshdesk CRM Platform.
Description: Freshdesk is smart ERP solution to manage your business. you can keep track of your inventory customers, products, orders, invoices, and more.
Author: Hossain Chisty(Backend Developer)
Contact: hossain.chisty11@gmail.com
Github: https://github.com/hossainchisty
"""

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


# Whether to append trailing slashes to URLs.
APPEND_SLASH = True


# Languages we provide translations for, out of the box.
LANGUAGES = [
    ('bn', gettext_noop('Bengali')),
    ('en', gettext_noop('English')),
]

# Maximum size, in bytes, of a request before it will be streamed to the
# file system instead of into memory.
FILE_UPLOAD_MAX_MEMORY_SIZE = 2621440  # i.e. 2.5 MB

# Maximum size in bytes of request data (excluding file uploads) that will be
# read before a SuspiciousOperation (RequestDataTooBig) is raised.
DATA_UPLOAD_MAX_MEMORY_SIZE = 2621440  # i.e. 2.5 MB

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'


# The number of seconds a password reset link is valid for (default: 3 days).
PASSWORD_RESET_TIMEOUT = 60 * 60 * 24 * 3


############
# SESSIONS #
############

# Cookie name. This can be whatever you want.
# SESSION_COOKIE_NAME = 'DUMMY_SESSION'

# Age of cookie, in seconds 52 weeks
SESSION_COOKIE_AGE = 31449600

# Whether to save the session data on every request.
SESSION_SAVE_EVERY_REQUEST = False

# Whether a user's session cookie expires when the web browser is closed.
SESSION_EXPIRE_AT_BROWSER_CLOSE = False



# Mail configrations
# EMAIL_HOST = os.getenv('EMAIL_HOST')
# EMAIL_PORT = os.getenv('EMAIL_PORT')
# EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')
# EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')
# EMAIL_USE_SSL = os.getenv('EMAIL_USE_SSL')
# EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

try:
    from config.settings.local import *
except ImportError:
    pass
