# A asyncpg for postgres connections
from RUKA import DB_URI, LOGGER
from RUKA.database.sql.createtable1 import (
    CREATE_USERS_TABLE,
    CREATE_CHATBOT_TABLE,
    CREATE_AFK_TABLE,
    CREATE_GBAN_TABLE
)
from RUKA.database.sql.createtable2 import (
    CREATE_DISABLE_TABLE
)

import asyncpg
import asyncio

MAX_CONNECTIONS = 5 # default to 5 since elephant allow only 5 connections
tables = [
    CREATE_USERS_TABLE,
    CREATE_CHATBOT_TABLE,
    #CREATE_AFK_TABLE,
    CREATE_GBAN_TABLE,
    CREATE_DISABLE_TABLE,
]


class Database:
    def __init__(self, uri):
        self.pool = None
        self.uri = uri

        async def connect():
            self.pool = await asyncpg.create_pool(self.uri, min_size=1, max_size=MAX_CONNECTIONS)
            async with self.pool.acquire() as conn:
                try:
                    for table in tables:
                        await conn.execute(table)
                except:
                    pass

        asyncio.get_event_loop().run_until_complete(connect())

    async def execute(self, query, *args, commit=False):
        async with self.pool.acquire() as conn:
            async with conn.transaction():
                if commit:
                    result = await conn.execute(query, *args)
                    return None
                else:
                    result = await conn.fetch(query, *args)
                    return result


LOGGER.info("[Ishikki] - [SQL] DATABASE CONNECTION SUCCESSFUL!!!")
sql_con = Database(DB_URI)
SQLDB = sql_con.execute  # Your SQLdb object for executing with one param commit whose default value set to False

"""
Dont simply kang, please give credits and one star for this help
https://github.com/ishikki-akabane/Ruka-Bot

This method solves the `To many connections error` in elephant sql or any other free postgresql
Founded by IShikki, dont say its yours
"""
