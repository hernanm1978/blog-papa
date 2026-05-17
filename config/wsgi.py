import os
import sys
from django.core.wsgi import get_wsgi_application

os.environ['DJANGO_SETTINGS_MODULE'] = 'config.settings.production'

# Debug temporal - borrar después
with open('/tmp/wsgi_debug.txt', 'w') as f:
    f.write(f"SETTINGS: {os.environ.get('DJANGO_SETTINGS_MODULE')}\n")

application = get_wsgi_application()

# Debug - escribir CSRF después de setup
with open('/tmp/wsgi_debug.txt', 'a') as f:
    from django.conf import settings
    f.write(f"CSRF: {getattr(settings, 'CSRF_TRUSTED_ORIGINS', 'NO EXISTE')}\n")
    f.write(f"DEBUG: {settings.DEBUG}\n")
