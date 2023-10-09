from channels.routing import ProtocolTypeRouter, URLRouter
from channels.security.websocket import AllowedHostsOriginValidators
from chat.middlewares import TokenAuthMiddleware
from django.urls import path

from chat import consumers

application = ProtocolTypeRouter({
    "websocket": AllowedHostsOriginValidators(
        TokenAuthMiddleware(
            URLRouter([
        path("ws/chat/<int:group_id>/", consumers.ChatConsumer.as_asgi()),
        ])
        )
    ) ,
})
