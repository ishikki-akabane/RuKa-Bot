from RUKA.database.sql import SQLDB


async def sql_adduser(user_id, user_name="None", bio="None", me="None"):
    user_id = int(user_id)
    query = '''INSERT INTO users_table (user_id, user_name, bio, me)
            VALUES ({}, '{}', '{}', '{}')
    '''
    result = await SQLDB(query.format(user_id, user_name, bio, me), commit=True)
    return result


async def sql_get_userid(user_name):
    query = """SELECT user_id FROM users_table WHERE username = '{}'"""
    result = await SQLDB(query.format(user_name), commit=False)
    exist = len(result)
    if exist == 0:
        return None
    else:
        print(result)
        for row in result:
            user_id = row[0]
        return user_id
