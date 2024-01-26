import os
from django.conf.urls import url
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.security.websocket import AllowedHostsOriginValidator, OriginValidator
from channels.auth import AuthMiddlewareStack

from chat.consumer import ChatConsumer
from chat.views import ThreadView

application = ProtocolTypeRouter({
    "websocket": AllowedHostsOriginValidator(
        AuthMiddlewareStack(
            URLRouter(
                [
                    url(r"^messages/(?P<username>[\w.@+-]+)/$", ChatConsumer),
                ]
            )
        )
    ),
})