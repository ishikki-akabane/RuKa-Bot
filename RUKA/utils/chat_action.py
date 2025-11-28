
from functools import wraps
from pyrogram.enums import ChatAction


def chatAction(action: str = "typing"):
    """
    Automatically sends a chat action (typing, uploading, choosing sticker, etc.)
    
    Usage:
        @send_action("typing")
        async def start(client, message):
        
    Available actions:
        typing, upload_photo, record_video, upload_video, record_audio,
        upload_audio, upload_document, find_location, record_video_note,
        upload_video_note, playing, speaking, choose_sticker, cancel
    """
    action_map = {
        "typing": ChatAction.TYPING,
        "upload_photo": ChatAction.UPLOAD_PHOTO,
        "record_video": ChatAction.RECORD_VIDEO,
        "upload_video": ChatAction.UPLOAD_VIDEO,
        "record_audio": ChatAction.RECORD_AUDIO,
        "upload_audio": ChatAction.UPLOAD_AUDIO,
        "upload_document": ChatAction.UPLOAD_DOCUMENT,
        "find_location": ChatAction.FIND_LOCATION,
        "record_video_note": ChatAction.RECORD_VIDEO_NOTE,
        "upload_video_note": ChatAction.UPLOAD_VIDEO_NOTE,
        "playing": ChatAction.PLAYING,
        "speaking": ChatAction.SPEAKING,
        "choose_sticker": ChatAction.CHOOSE_STICKER,
        "cancel": ChatAction.CANCEL,
    }
    
    chosen_action = action_map.get(action.lower(), ChatAction.TYPING)
    def decorator(func):
        @wraps(func)
        async def wrapper(client, message, *args, **kwargs):
            try:
                await client.send_chat_action(
                    chat_id=message.chat.id,
                    action=chosen_action
                )
            except:
                pass
            return await func(client, message, *args, **kwargs)
        return wrapper
    return decorator
