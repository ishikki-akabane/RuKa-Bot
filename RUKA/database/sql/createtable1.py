#FIRST

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
