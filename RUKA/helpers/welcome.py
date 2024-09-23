# jai shree ram

from RUKA import MeowClient


async def fetch_welcome(welcome_data):
    welcome_text = welcome_data["text"]
    welcome_button = welcome_data["button"]
    welcome_ = welcome_data[""]
    
    welcome_type = welcome_data["type"]
    if welcome_type == "template":
        data = aahhh nvm, i will do tomorrow 


async def initialise_welcome(template_id, client, user, chat):
    data = MeowClient.check_welcome_template(template_id)
    result = []
    if data["user_pfp"]
        try:
            user_pfp = user.photo.big_file_id
        except:
            return False, "couldn't fetch big_file_id for user pfp"
        userphoto = await client.download_media(user_pfp, file_name=f"{user.id}userpfp.jpg")
        result.append(userphoto)

    if data["chat_pfp"]
        try:
            chat_pfp = chat.photo.big_file_id
        except:
            return False, "couldn't fetch big_file_id for chat pfp"
        chatphoto = await client.download_media(chat_pfp, file_name=f"{user.id}chatpfp.jpg")
        result.append(chatphoto)

    return True, result
    
