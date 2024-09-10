# Lazyyy

from datetime import datetime
from GramDB import GramDB, GramDBAsync
from RUKA import DATABASE_URL, LOGGER

from .user import UserOperations
from .group import GroupOperations


class DATABASE(
    UserOperations,
    GroupOperations
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
            "users": ("_id", "name", "bio", "coins", "joined_date", "is_scanned"),
            "groups": ("_id", "name", "member_count", "created_at", "is_scanned")
        }
        self.async_manager.run_async(self.create_table())

    async def create_table(self):
        """
        Asynchronously creates a table if it doesn't exist.
        """
        for table_name, schema in self.table_schemas.items():
            if not await self.db.check_table(table_name):
                await self.db.create(table_name, schema)


db = DATABASE(DATABASE_URL)

