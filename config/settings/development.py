from config.settings.base import *

# Override base.py settings here

DEBUG = True

try:
    from config.settings.local import *
except ImportError:
    pass
