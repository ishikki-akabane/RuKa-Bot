# jai shree ram

from RUKA import MeowClient


async def initialise_welcome(template_id, client, user, chat):
    data = await MeowClient.check_welcome_template(template_id)
    if data["data"]["user_pfp"]:
        try:
            user_pfp = user.photo.big_file_id
        except:
            print(f"couldn't fetch big_file_id for user {user.id} pfp")
        userphoto = await client.download_media(user_pfp, file_name=f"{user.id}userpfp.jpg")

    if data["data"]["chat_pfp"]:
        try:
            chat_pfp = chat.photo.big_file_id
        except:
            print(f"couldn't fetch big_file_id for chat {chat.id} pfp")
        chatphoto = await client.download_media(chat_pfp, file_name=f"{user.id}chatpfp.jpg")

    return data
    
