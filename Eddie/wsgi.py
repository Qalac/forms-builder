"""
WSGI config for Eddie project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

MODE = 'DEV'

if MODE == 'DEV':
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Eddie.settings.development")
else:
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Eddie.settings.production")
   

application = get_wsgi_application()
