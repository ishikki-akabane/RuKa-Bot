# below code is taken from USERGE-X repo
# all credits to the respective author (dunno who wrote it will find later n update)
# i simply copied this code and pasted here for few modules, still i don't know much about this code, so please don't ask me about this 


__all__ = ['get_collection']

import asyncio
from motor.motor_asyncio import AsyncIOMotorClient
from motor.core import AgnosticClient, AgnosticDatabase, AgnosticCollection
from SUMI import MONGO_DB_URI as DB_URL

print("Connecting to Database ...")

_MGCLIENT: AgnosticClient = AsyncIOMotorClient(DB_URL)
_RUN = asyncio.get_event_loop().run_until_complete

if "SUMI" in _RUN(_MGCLIENT.list_database_names()):
    print("SUMI Database Found :) => Now Logging to it...")
else:
    print("SUMI Database Not Found :( => Creating New Database...")

_DATABASE: AgnosticDatabase = _MGCLIENT["SUMI"]


def get_collection(name: str) -> AgnosticCollection:
    """ Create or Get Collection from your database """
    return _DATABASE[name]


def _close_db() -> None:
    _MGCLIENT.close()
