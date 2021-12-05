"""
Title: Freshdesk CRM Platform.
Description: Freshdesk is smart ERP solution to manage your business. you can keep track of your inventory customers, products, orders, invoices, and more.
Author: Hossain Chisty(Backend Developer)
Contact: hossain.chisty11@gmail.com
Github: https://github.com/hossainchisty

"""

from pathlib import Path

from django.utils.translation import gettext_lazy as _

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-mqcg&7z#rec4yygir4_@&5ms0bno*9gribx$3@xwu#&-rvw$cs'

DEBUG = True

ALLOWED_HOSTS = ['localhost', '127.0.0.1']


DEFAULT_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
]

THIRD_PARTY_APPS = [
    # 'material',
    # 'material.admin',
    'user_sessions',
    'django.contrib.sitemaps',
    'django.contrib.humanize',
    'django_filters',
    'simple_history',
    'django_countries',
    'rest_framework',
    'phonenumber_field',
    'rest_framework.authtoken',
    'rest_auth',
    'rest_auth.registration',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
]

LOCAL_APPS = [
    'core.apps.CoreConfig',
    'stock.apps.StockConfig',
    'expense.apps.ExpenseConfig',
    'sales.apps.SalesConfig',
    'report.apps.ReportConfig',
    'settings.apps.SettingsConfig',
    'profiles.apps.ProfilesConfig',
    'products.apps.ProductsConfig',
    'accounts.apps.AccountsConfig',
    'purchase.apps.PurchaseConfig',
    'suppliers.apps.SuppliersConfig',
    'customers.apps.CustomersConfig',
]

INSTALLED_APPS = DEFAULT_APPS + LOCAL_APPS + THIRD_PARTY_APPS


SITE_ID = 1

ROOT_URLCONF = 'config.urls'
WSGI_APPLICATION = 'config.wsgi.application'
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [    
        'rest_framework.permissions.IsAuthenticated',
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': [
    'rest_framework.authentication.TokenAuthentication',
    'rest_framework.authentication.SessionAuthentication',
    ],
    'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend']
}

REST_FRAMEWORK = {
    #? By default set to like that 
    # 'SEARCH_PARAM': 'search'
    'SEARCH_PARAM': 'q'

}

# Setting the throttling policy

REST_FRAMEWORK = {
    'DEFAULT_THROTTLE_CLASSES': [
        'rest_framework.throttling.AnonRateThrottle',
        'rest_framework.throttling.UserRateThrottle'
    ],
    'DEFAULT_THROTTLE_RATES': {
        'anon': '2/day',
        'user': '5/hour',
        'sale': '3/min',
    }
}



DEFAULT_MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'user_sessions.middleware.SessionMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

MIDDLEWARE = DEFAULT_MIDDLEWARE 

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Mail configrations
# EMAIL_HOST = "smtp.zoho.com"
# EMAIL_PORT = 465
# EMAIL_HOST_USER = "hossain.chisty@zohomail.com"
# EMAIL_HOST_PASSWORD = "#2#3B399TiU@aBC"
# EMAIL_USE_SSL = True
# EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"

# Session configuration
# CART_SESSION_ID = 'cart'
SESSION_COOKIE_AGE = 86400  # 24 hours in seconds
SESSION_EXPIRE_AT_BROWSER_CLOSE = False

# Celery Configurations
CELERY_BROKER_URL = 'redis://127.0.0.1:6379'
# CELERY_RESULT_BACKEND = 'redis://127.0.0.1:6379'
CELERY_RESULT_BACKEND = 'django-db'
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TIMEZONE = 'Asia/Dhaka'

SESSION_ENGINE = 'user_sessions.backends.db'
# FIXME: Make sure LOGOUT_REDIRECT_URL is set to some page to redirect users after logging out.
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Dhaka'

USE_I18N = True

USE_L10N = True

USE_TZ = True


STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_DIRS = [BASE_DIR / 'static']
DATA_UPLOAD_MAX_NUMBER_FIELDS = 10240

# MATERIAL_ADMIN_SITE = {
#     'HEADER':  _('Your site header'),  # Admin site header
#     'TITLE':  _('Your site title'),  # Admin site title
#     'FAVICON':  'path/to/favicon',  # Admin site favicon (path to static should be specified)
#     'MAIN_BG_COLOR':  'color',  # Admin site main color, css color should be specified
#     'MAIN_HOVER_COLOR':  'color',  # Admin site main hover color, css color should be specified
#     'PROFILE_PICTURE':  'path/to/image',  # Admin site profile picture (path to static should be specified)
#     'PROFILE_BG':  'path/to/image',  # Admin site profile background (path to static should be specified)
#     'LOGIN_LOGO':  'path/to/image',  # Admin site logo on login page (path to static should be specified)
#     'LOGOUT_BG':  'path/to/image',  # Admin site background on login/logout pages (path to static should be specified)
#     'SHOW_THEMES':  True,  #  Show default admin themes button
#     'TRAY_REVERSE': True,  # Hide object-tools and additional-submit-line by default
#     'NAVBAR_REVERSE': True,  # Hide side navbar by default
#     'SHOW_COUNTS': True, # Show instances counts for each model
#     'APP_ICONS': {  # Set icons for applications(lowercase), including 3rd party apps, {'application_name': 'material_icon_name', ...}
#         'sites': 'send',
#     },
#     'MODEL_ICONS': {  # Set icons for models(lowercase), including 3rd party models, {'model_name': 'material_icon_name', ...}
#         'site': 'contact_mail',
#     }
# }
