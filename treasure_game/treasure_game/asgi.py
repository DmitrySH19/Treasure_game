"""
ASGI config for treasure_game project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/asgi/
"""

import os

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application

from django.urls import path, re_path
from django.conf.urls import url
from chat import consumers
from gameapp import game_users

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'treasure_game.settings')

chat_application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter([
            re_path(r'ws/account/login/(?P<game_room>\w+)/$', game_users.GameUsers.as_asgi()),
            re_path(r'ws/chat/(?P<room_name>\w+)/$', consumers.ChatConsumer.as_asgi()),
        ])
    ),
})

