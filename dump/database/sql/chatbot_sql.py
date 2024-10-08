from RUKA.database.sql import SQLDB

async def sql_addchatbot(chat_id, version):
    chat_id = int(chat_id)
    query = '''INSERT INTO chatbot_table (chat_id, version)
            VALUES ({}, {})
    '''
    result = await SQLDB(query.format(chat_id, version), commit=True)
    return result


async def sql_removechatbot(chat_id):
    chat_id = int(chat_id)
    query = '''DELETE FROM chatbot_table WHERE chat_id = {}'''
    result = await SQLDB(query.format(chat_id), commit=True)
    return result


async def sql_updatechatbot(chat_id, version):
    chat_id = int(chat_id)
    query = '''UPDATE chatbot_table SET version = {} WHERE chat_id = {}'''
    result = await SQLDB(query.format(version, chat_id), commit=True)
    return result


async def checkchat(chat_id):
    chat_id = int(chat_id)
    query = '''SELECT * FROM chatbot_table WHERE chat_id = {}'''
    result = await SQLDB(query.format(chat_id), commit=False)
    exist = len(result)
    if exist == 0:
        return None
    else:
        for row in result:
            version = row[1]
        return version
    
    
async def chatbot_list():
    query = '''SELECT * FROM chatbot_table'''
    result = await SQLDB(query, commit=False)
    exist = len(result)
    CHATbot = []
    if exist == 0:
        return None
    else:
        for row in result:
            chat_id = row[0]
            version = row[1]
            chatbot_list = [chat_id, version]
            CHATbot.append(chatbot_list)
        return CHATbot
