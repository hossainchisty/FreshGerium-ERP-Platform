# flake8: noqa

from config.settings.base import *

# Override base.py settings here

DEBUG = True

# THIRD_PARTY_APPS = [
#     'debug_toolbar',
# ]

# INTERNAL_IPS = [
#     "127.0.0.1",
# ]
try:
    from config.settings.local import *
except ImportError:
    pass
