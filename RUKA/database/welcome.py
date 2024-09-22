from datetime import datetime
from RUKA import LOGGER

class WelcomeOperations:
    """
    A class that handles welcome-related operations.
    """
    async def check_chat_welcome(self, chat_id: int):
        data = await self.db.find_one(
            "welcome",
            {
                "_id": chat_id
            }
        )
        if data:
            return data
        else:
            return None

    async def add_welcome(
        self
    ):
        data = await self.check_user(user_id)
        if data:
            return
        else:
            current_time = datetime.now()
            str_date = current_time.strftime("%d %B, %Y")
            
