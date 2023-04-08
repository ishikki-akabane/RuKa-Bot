from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker
from RUKA import DB_URI

MAX_POOL_SIZE = 5

engine = create_engine(DB_URI, pool_size=MAX_POOL_SIZE, max_overflow=0)
BASE = declarative_base()
Session = scoped_session(sessionmaker(bind=engine))

# Define your models here

def start():
    BASE.metadata.create_all(engine)
    return Session()

# Use the session to query your database
session = start()