# flake8: noqa

"""
Title: Freshdesk CRM Platform.
Description: Freshdesk is smart ERP solution to manage your business. you can keep track of your inventory customers, products, orders, invoices, and more.
Author: Hossain Chisty(Backend Developer)
Contact: hossain.chisty11@gmail.com
Github: https://github.com/hossainchisty
"""

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
