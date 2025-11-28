from datetime import datetime
from RUKA import LOGGER

class UserOperations:
    """
    A class that handles user-related operations.
    """
    async def check_user(self, user_id: int):
        data = await self.db.find_one(
            "users",
            {
                "_id": user_id
            }
        )
        if data:
            return data
        else:
            return None

    async def add_user(
        self,
        user_id: int,
        name: str,
        coins: str,
        is_scanned: bool
    ):
        data = await self.check_user(user_id)
        if data:
            return
        else:
            current_time = datetime.now()
            str_date = current_time.strftime("%d %B, %Y")
            try:
                await self.db.insert_one(
                    "users",
                    {
                        "_id": user_id,
                        "name": name,
                        "coins": coins,
                        "joined_date": str_date,
                        "is_scanned": is_scanned
                    }
                )
            except Exception as e:
                LOGGER.error(f"Error adding user to database: {e}")
            return
