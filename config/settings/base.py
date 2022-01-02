"""
Title: Freshdesk CRM Platform.
Description: Freshdesk is smart ERP solution to manage your business. you can keep track of your inventory customers, products, orders, invoices, and more.
Author: Hossain Chisty(Backend Developer)
Contact: hossain.chisty11@gmail.com
Github: https://github.com/hossainchisty

"""

from pathlib import Path

from .env import private_ip, serect_key

BASE_DIR = Path(__file__).resolve().parent.parent.parent

SECRET_KEY = serect_key

DEBUG = True

ALLOWED_HOSTS = ['localhost', '127.0.0.1', private_ip]


DEFAULT_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.sites',
    'django.contrib.contenttypes',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sessions',
]

THIRD_PARTY_APPS = [
    'corsheaders',
    'import_export',
    'django_user_agents',
    'django.contrib.sitemaps',
    'django.contrib.humanize',
    'django_filters',
    'crispy_forms',
    'simple_history',
    'django_countries',
    'rest_framework',
    'phonenumber_field',
    'rest_framework.authtoken',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'django_otp',
    'django_otp.plugins.otp_totp',
    'django_otp.plugins.otp_static',
]

LOCAL_APPS = [
    'core.apps.CoreConfig',
    'stock.apps.StockConfig',
    'expense.apps.ExpenseConfig',
    'sales.apps.SalesConfig',
    'report.apps.ReportConfig',
    'service.apps.ServiceConfig',
    'returns.apps.ReturnsConfig',
    'damage.apps.DamageConfig',
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

THOUSAND_SEPARATOR = ','
PHONENUMBER_DEFAULT_REGION = 'BD'
ROOT_URLCONF = 'config.urls'
WSGI_APPLICATION = 'config.wsgi.application'
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


# Password reset time limit⏳:
PASSWORD_RESET_TIMEOUT = 259200 # 3 days - 72 hour, in (seconds)

# REST_FRAMEWORK = {
#     'DEFAULT_PERMISSION_CLASSES': [    
#         # 'rest_framework.permissions.IsAuthenticated',
#         'rest_framework.permissions.AllowAny',
#     ],
#     'DEFAULT_AUTHENTICATION_CLASSES': [
#     'rest_framework.authentication.TokenAuthentication',
#     'rest_framework.authentication.SessionAuthentication',
#     ],
#     'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend']
# }

REST_FRAMEWORK = {
    # 'SEARCH_PARAM': 'search'
    'SEARCH_PARAM': 'q'
}

# Setting the throttling policy

REST_FRAMEWORK = {
    'DEFAULT_THROTTLE_CLASSES': [
        'rest_framework.throttling.AnonRateThrottle',
        'rest_framework.throttling.UserRateThrottle'
    ],
    # 'DEFAULT_THROTTLE_RATES': {
    #     'anon': '2/day',
    #     'user': '5/hour',
    #     'sale': '3/min',
    # }
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # Third party middleware📌
    'corsheaders.middleware.CorsMiddleware',
    'django_otp.middleware.OTPMiddleware',
]


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
                # Custom context processors📌
                'expense.context_processors.get_total_expsense',
                'expense.context_processors.get_total_expsense_by_month',
                'expense.context_processors.get_total_expsense_by_year',
                'sales.context_processors.march_sales',
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


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'database/freshdesh-db.sqlite3',
    },
    'expense_db' : {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'database/expense-db.sqlite3',
    },

}

# The list of routers that will be used to determine which database to use when performing a database query.
DATABASE_ROUTERS = ['database.routers.db_routers.ExpenseRouter']

# CACHES = {
#     'default': {
#         'BACKEND': 'django.core.cache.backends.redis.RedisCache',
#         'LOCATION': 'redis://127.0.0.1:6379',
#     }
# }

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Dhaka'

USE_I18N = True

USE_L10N = True

USE_TZ = True


STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_DIRS = [BASE_DIR / 'static']
CRISPY_TEMPLATE_PACK = "bootstrap4"
DATA_UPLOAD_MAX_NUMBER_FIELDS = 10240
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# A list of origins that are authorized to make cross-site HTTP requests.
CORS_ALLOWED_ORIGINS = [
    'http://localhost:3000',
]
# CORS_ALLOW_ALL_ORIGINS = True


