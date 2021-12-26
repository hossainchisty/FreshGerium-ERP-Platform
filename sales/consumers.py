import json
from asyncio import sleep
from random import randint

from channels.generic.websocket import AsyncWebsocketConsumer


class SaleGraphConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        for _ in range(1000):
            await self.send(
                json.dumps({
                    'value': randint(0, 1000),
                })
            )
            await sleep(1)

    def disconnect(self, close_code):
        pass

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        self.send(text_data=json.dumps({
            'message': message
        }))
