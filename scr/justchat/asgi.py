"""
ASGI config for justchat project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/asgi/
"""

import os

from channels.routing import ProtocolTypeRouter
from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'justchat.settings')

application = ProtocolTypeRouter(
  {
    "http": get_asgi_application(),
    # Just HTTP for now. (we cand add other protocols later.)
  }
)
