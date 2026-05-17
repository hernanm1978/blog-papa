from .base import *

DEBUG = False

ALLOWED_HOSTS = ['localhost', '127.0.0.1','*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

INSTALLED_APPS += ['debug_toolbar']
MIDDLEWARE.insert(1, 'debug_toolbar.middleware.DebugToolbarMiddleware')
INTERNAL_IPS = ['127.0.0.1','192.168.1.198']
CSRF_TRUSTED_ORIGINS = ['http://192.168.1.198:8085']
