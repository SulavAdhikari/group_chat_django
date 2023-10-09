"""
ASGI config for groupchat project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, get_default_application
from chat.middlewares import TokenAuthMiddleware
from chat.routing import application
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "groupchat.settings")

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": application(),
})
