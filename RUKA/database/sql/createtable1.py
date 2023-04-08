#FIRST
from RUKA.database.sql import SQLDB
import asyncio


user_table_query = '''
        CREATE TABLE IF NOT EXISTS user_table (
            user_id BIGINT PRIMARY KEY,
            name VARCHAR(255),
        )
'''

async def create_table1():
    r1 = await SQLDB(user_table_query, commit=True)
    return True


asyncio.run(create_table1())