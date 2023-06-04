from RUKA.database.sql import SQLDB


async def sql_disable(chat_id, command):
    chat_id = int(chat_id)
    query = '''INSERT INTO disable_table (chat_id, command)
            VALUES ({}, '{}')
    '''
    result = await SQLDB(query.format(chat_id, command), commit=True)
    return result


async def sql_enable(chat_id, command):
    chat_id = int(chat_id)
    query = '''DELETE FROM disable_table WHERE chat_id = {} AND command = '{}' '''
    result = await SQLDB(query.format(chat_id, command), commit=True)
    return result


async def checkdisable(chat_id):
    chat_id = int(chat_id)
    query = '''SELECT * FROM disable_table WHERE chat_id = {}'''
    result = await SQLDB(query.format(chat_id), commit=False)
    exist = len(result)
    commands = []
    if exist == 0:
        return commands
    else:
        for row in result:
            command = row[1]
            commands.append(command)
        return commands


async def sql_get_alldisabled_cache():
    query = '''SELECT * FROM disable_table'''
    result = await SQLDB(query, commit=False)
    exist = len(result)
    disabled_cache_dict = {}
    if exist == 0:
        return disabled_cache_dict
    else:
        for row in result:
            chat_id = row[0]
            command = row[1]
            listed_chats = disabled_cache_dict.keys()
            if chat_id in listed_chats:
                cmds = disabled_cache_dict[chat_id]
                cmds.append(command)
            else:
                disabled_cache_dict[chat_id] = [command]
        return disabled_cache_dict
