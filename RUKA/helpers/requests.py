import asyncio
import json
import aiohttp

from RUKA import BLUE_API, aiosession

headers = {"API-KEY": BLUE_API}

async def bluerequest(url, data=None):
    if data == None:
        async with aiosession.get(url, headers=headers) as resp:
            response = await resp.json()
        return response
    
    async with aiosession.post(url, headers=headers, json=data) as resp:
        response = await resp.json()
    return response
