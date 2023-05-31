#FIRST
CREATE_USERS_TABLE = '''
    CREATE TABLE IF NOT EXISTS users_table (
        user_id BIGINT,
        user_name VARCHAR(255),
        bio VARCHAR(255),
        me VARCHAR(255)
    )
'''




CREATE_AFK_TABLE = '''
    CREATE TABLE IF NOT EXISTS afk_table (
        user_id BIGINT,
        reason VARCHAR(255),
        date date
    )
'''

CREATE_CHATBOT_TABLE = '''
    CREATE TABLE IF NOT EXISTS chatbot_table (
        chat_id BIGINT,
        version INTEGER
    )
'''

CREATE_GBAN_TABLE = '''
    CREATE TABLE IF NOT EXISTS gban_table (
        user_id BIGINT,
        name VARCHAR(255),
        reason VARCHAR(255)
    )
'''
