from sanic.views import HTTPMethodView
from sanic import response
import aiohttp
import logging
from config import *


class Smoke(HTTPMethodView):
    def get(self, request):
        return response.json(
            {"message": "Hello world!"}, headers={"Service": SERVICE_NAME}, status=200
        )

    def post(self, request):
        return response.json(
            {"message": "Hello world!"}, headers={"Service": SERVICE_NAME}, status=200
        )


async def notification():
    # data = {"name": SERVICE_NAME, "ip": SDA_CONNECT, "port": SERVICE_PORT}
    data = {"name": SERVICE_NAME, "ip": SERVICE_HOST, "port": SERVICE_PORT}
    try:
        async with aiohttp.ClientSession() as session:
            request_post = await session.post(f"http://{SDA_HOST}:{SDA_PORT}", params=data)
    except Exception as exc:
        logging.error('Connection to SDA refused. ERROR')
