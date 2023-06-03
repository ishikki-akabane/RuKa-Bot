#SECOND
CREATE_DISABLE_TABLE = '''
    CREATE TABLE IF NOT EXISTS disable_table (
        chat_id BIGINT,
        command VARCHAR(255),
    )
'''