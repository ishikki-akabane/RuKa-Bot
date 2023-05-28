from RUKA.database.sql import SQLDB


async def sql_savegban(user_id, reason, name="None"):
    user_id = int(user_id)
    query = '''INSERT INTO gban_table (user_id, name, reason)
            VALUES ({}, '{}', '{}')
    '''
    result = await SQLDB(query.format(user_id, name, reason), commit=True)
    return result


async def sql_updategban(user_id, reason, name):
    user_id = int(user_id)
    query = '''UPDATE gban_table SET reason = '{}' WHERE user_id = {}'''
    result = await SQLDB(query.format(reason, user_id), commit=True)
    if name != "None":
        query = '''UPDATE gban_table SET name = '{}' WHERE user_id = {}'''
        result = await SQLDB(query.format(name, user_id), commit=True)
    return result


async def sql_revertgban(user_id):
    user_id = int(user_id)
    query = '''DELETE FROM gban_table WHERE user_id = {}'''
    result = await SQLDB(query.format(user_id), commit=True)
    return result


async def checkgban(user_id):
    user_id = int(user_id)
    query = '''SELECT * FROM gban_table WHERE user_id = {}'''
    result = await SQLDB(query.format(user_id), commit=False)
    exist = len(result)
    if exist == 0:
        return None
    else:
        for row in result:
            user_id = row[0]
            name = row[1]
            reason = row[2]
        data = [name, reason]
        return data


async def gban_list():
    query = '''SELECT * FROM gban_table'''
    result = await SQLDB(query, commit=False)
    exist = len(result)
    GBANLIST = []
    if exist == 0:
        return None
    else:
        for row in result:
            user_id = row[0]
            name = row[1]
            reason = row[2]
            gban_dict = {"user_id": user_id, "name": name, "reason": reason}
            GBANLIST.append(gban_dict)
        return GBANLIST