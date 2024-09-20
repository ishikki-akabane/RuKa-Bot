from datetime import datetime
from RUKA import LOGGER

class GroupOperations:
    """
    A class that handles group-related operations.
    """
    async def check_group(self, group_id: int):
        data = await self.db.find_one(
            "groups",
            {
                "_id": group_id
            }
        )
        if data:
            return data
        else:
            return None

    async def add_group(
        self,
        group_id: int,
        name: str,
        member_count: int,
        is_scanned: bool
    ):
        data = await self.check_group(group_id)
        if data:
            return
        else:
            current_time = datetime.now()
            str_date = current_time.strftime("%d %B, %Y")
            try:
                await self.db.insert_one(
                    "groups",
                    {
                        "_id": group_id,
                        "name": name,
                        "member_count": member_count,
                        "joined_date": str_date,
                        "is_scanned": is_scanned
                    }
                )
            except Exception as e:
                LOGGER.error(f"Error adding group to database: {e}")
            return
