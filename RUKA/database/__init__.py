#Lazyyy
import asyncio
import sys

from motor.motor_asyncio import AsyncIOMotorClient as MongoClient
from RUKA import MONGO_DB_URI 
from pymongo.errors import ServerSelectionTimeoutError


MONGO_DB = "ishikki"


motor = MongoClient(MONGO_DB_URI)
db = motor[MONGO_DB]

try:
    asyncio.get_event_loop().run_until_complete(motor.server_info())
except ServerSelectionTimeoutError:
    sys.exit(log.critical("Can't connect to mongodb! Exiting..."))
