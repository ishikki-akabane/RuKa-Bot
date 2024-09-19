from datetime import datetime
from RUKA import LOGGER

class DebugOperations:
    """
    A class that handles Debugging operations.
    """
    async def add_error(
        self,
        chat_id: str,
        func_name: str,
        file_path: str,
        error_line: str,
        error_e: str
    ):
        print("hola")
        current_time = datetime.now()
        str_date = current_time.strftime("%d %B, %Y %H:%M:%S")
        try:
            await self.db.insert_one(
                "debug",
                {
                    "chat_id": chat_id,
                    "func_name": func_name,
                    "file_path": file_path,
                    "error_line": error_line,
                    "error_e": error_e
                }
            )
        except Exception as e:
            LOGGER.error(f"Error adding debug info to database: {e}")
        return
