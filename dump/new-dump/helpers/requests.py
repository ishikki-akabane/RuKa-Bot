import asyncio
import json
import aiohttp

from RUKA import BLUE_API, aiosession
from RUKA.helpers.errors import capture_error

headers = {"API-KEY": BLUE_API}


async def bluerequest(url, data=None):
    if data == None:
        try:
            async with aiosession.get(url, headers=headers) as resp:
                response = await resp.json()
            return response
        except:
            response = {"msg": "Opps!! Something went wrong"}
            return response
    try:
        async with aiosession.post(url, headers=headers, json=data) as resp:
            response = await resp.json()
        return response
    except:
        response = {"msg": "Opps!! Something went wrong"}
        return response