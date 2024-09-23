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
        self,
        chat_id
    ):
        data = await self.check_chat_welcome(chat_id)
        if data:
            return
        else:
            current_time = datetime.now()
            str_date = current_time.strftime("%d %B, %Y")
            try:
                await self.db.insert_one(
                    "welcome",
                    {
                        "_id": chat_id,
                        "mode": "template",
                        "template_id": "x00xhaha"
                    }
                )
            except Exception as e:
                LOGGER.error(f"Error adding user to database: {e}")
            return
            
            
