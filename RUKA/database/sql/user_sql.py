from RUKA.database.sql import SQLDB


async def sql_adduser(user_id, name):
    user_id = int(user_id)
    query = '''INSERT INTO user_table (user_id, name)
            VALUES ({}, '{}')
    '''
    result = await SQLDB(query.format(user_id, name), commit=True)
    return result