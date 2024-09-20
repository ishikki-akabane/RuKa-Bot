# Lazyyy

from datetime import datetime
from GramDB import GramDB, GramDBAsync
from RUKA import DATABASE_URL, LOGGER

from .users import UserOperations
from .groups import GroupOperations
from .debug import DebugOperations


class DATABASE(
    UserOperations,
    GroupOperations,
    DebugOperations
):
    """
    A class to manage the database operations using GramDB.

    Attributes:
        db (GramDB): An instance of the GramDB class initialized with the provided URI.
        table_schemas (dict): A dictionary defining table names and their corresponding schema.
    """
    def __init__(self, uri):
        """
        Initializes the Database instance and creates tables if they don't exist.

        Args:
            uri (str): The URI string to connect to the GramDB database.
        """
        self.async_manager = GramDBAsync()
        self.db = GramDB(uri, self.async_manager)
        self.initialize()

    def initialize(self):
        self.table_schemas = {
            "users": ("_id", "name", "coins", "joined_date", "is_scanned"),
            "groups": ("_id", "name", "member_count", "joined_date", "is_scanned"),
            "debug": ("chat_id", "func_name", "file_path", "error_line", "error_e")
        }
        self.async_manager.run_async(self.create_table())

    async def create_table(self):
        """
        Asynchronously creates a table if it doesn't exist.
        """
        for table_name, schema in self.table_schemas.items():
            if not await self.db.check_table(table_name):
                await self.db.create_one(table_name, schema)

    async def create_cache():
        
    def close(self):
        self.db.close()


CACHE_USERS = []
CACHE_GROUPS = []

db = DATABASE(DATABASE_URL)

