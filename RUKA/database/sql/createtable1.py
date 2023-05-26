#FIRST

CREATE_AFK_TABLE = '''
    CREATE TABLE IF NOT EXISTS afk_table (
        user_id BIGINT,
        reason VARCHAR(255),
        date dat
    )
'''

CREATE_CHATBOT_TABLE = '''
    CREATE TABLE IF NOT EXISTS chatbot_table (
        chat_id BIGINT,
        version INTEGER
    )
'''
