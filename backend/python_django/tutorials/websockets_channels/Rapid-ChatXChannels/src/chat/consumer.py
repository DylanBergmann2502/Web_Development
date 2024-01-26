import asyncio
import json
from django.contrib.auth import get_user_model
from channels.consumer import AsyncConsumer

from .models import Thread, ChatMessage


class ChatConsumer(AsyncConsumer):
    async def websocket_connect(self, event):
        print("connected", event)
        await self.send({
            "type": "websocket.accept"
        })
        other_user = self.scope['url_route']['kwargs']['username']
        me = self.scope['user']
        # await asyncio.sleep(10)
        await self.send({
            "type": "websocket.send",
            "text": "Hello world"

        })

    async def websocket_receive(self, event):
        # when a message is received from the websocket
        pass

    async def websocket_disconnect(self, event):
        # when the socket connects
        pass