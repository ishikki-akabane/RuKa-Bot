#FIRST

CREATE_USER_TABLE = '''
    CREATE TABLE IF NOT EXISTS user_table (
        user_id BIGINT,
        name VARCHAR(255)
    )
'''



#asyncio.run(create_table1())