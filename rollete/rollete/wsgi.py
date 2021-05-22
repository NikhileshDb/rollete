"""
WSGI config for rollete project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""
import sys
import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rollete.settings')

application = get_wsgi_application()


path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

if path not in sys.path:
    sys.path.append(path)