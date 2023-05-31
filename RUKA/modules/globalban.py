from io import BytesIO
from RUKA import dp
from RUKA.helpers.errors import capture_error
from RUKA.helpers.rank_help import status
from RUKA.helpers.extra import mention
from RUKA.database.sql.gban_sql import sql_savegban, sql_revertgban, sql_updategban, checkgban, gban_list


from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes, CommandHandler, MessageHandler, filters, CallbackQueryHandler
from telegram.constants import ParseMode


@status(rank="sudo")
@capture_error
async def gban(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    message = update.effective_message
    args = context.args
    bot = context.bot
    
    reply = message.reply_to_message
    if reply:
        target_id = reply.from_user.id
        target_name = reply.from_user.first_name
        if len(args) > 0:
            reason = message.text.split(None, 1)[1]
        else:
            return message.reply_text("Provide me a reason baka!!")

    else:
        if len(args) > 0:
            try:
                target_id = args[0]
                target_id = int(target_id)
            except:
                return await message.reply_text("User id is not valid!!")
            try:
                reason = message.text.split(None, 1)[1].split(None, 1)[1]
            except:
                return await message.reply_text("Provide me a reason baka!!")
            try:
                target_chat = await bot.get_chat(target_id)
                target_name = target_chat.first_name
            except:
                target_name = "None"
        else:
            return await message.reply_text("Bro wtf, you havent provided me anything :/")
    
    exist = await checkgban(target_id)
    if exist:
        name = exist[0]
        oldreason = exist[1]
        if name == "None":
            if target_name != "None":
                name = target_name

        await message.reply_text(
            f"This user is already gbanned\n\n**Previous Reason**: `{oldreason}`\n**New reason**: `{reason}`\n\nDo you want to overide the reason?",
            parse_mode=ParseMode.MARKDOWN,
            reply_markup=InlineKeyboardMarkup(
                [
                    [InlineKeyboardButton(text="Yes", callback_data=f"gban=yes={target_id}={name}={reason}")]
                    [InlineKeyboardButton(text="No", callback_data="gban=no")]
                ]
            )
        )
        return
    
    await sql_savegban(target_id, reason, target_name)
    user = mention(target_id, target_name, mention=True)
    await message.reply_text(f"{user} has been banned globally!", parse_mode=ParseMode.MARKDOWN)


@capture_error
async def gban_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    message = update.effective_message
    commands = query.data.split("=")
    if commands[0] == "gban":
        if commands[1] == "yes":
            target_id = commands[2]
            name = commands[3]
            reason = commands[4]
            await sql_updategban(target_id, reason, name)
            await message.edit_text("I have updated the reason for his crime :)")
        else:
            await message.edit_text("Ok boss, i wont overide the reason :)")


@status(rank="sudo")
@capture_error
async def revert(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    message = update.effective_message
    args = context.args
    if len(args) > 0:
        try:
            target_id = args[0]
            target_id = int(target_id)
        except:
            return message.reply_text("User id is not valid!!")
        exist = await checkgban(target_id)
        if not exist:
            await message.reply_text("This user is not gbanned :/")
            return
            
        await sql_revertgban(target_id)
        await message.reply_text("I have ungbanned that person as you said my master :)")
    else:
        return await message.reply_text("Bro wtf, you havent provided me anything :/")




@status(rank="sudo")
@capture_error
async def gbanlist(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = update.effective_message
    gbans = await gban_list()
    if gbans:
        chatfile = "I'm banning these peoples:)\n"
        chatfile += "[x] - [USER ID]  - [NAME] -- [REASON]\n\n"
        for gban in gbans:
            user_id = gban["user_id"]
            name = gban["name"]
            reason = gban["reason"]
            chatfile += f"[x] - {user_id} - {name} -- {reason}\n"

        with BytesIO(str.encode(chatfile)) as output:
            output.name = "Gbanlist.txt"
            await message.reply_document(
                document=output,
                filename="Gbanlist.txt",
                caption="gbanned people list::",
            )
    else:
        await message.reply_text(text="No one is gbanned sir :)")
        

dp.add_handler(CommandHandler("gban", gban, block=False))
dp.add_handler(CallbackQueryHandler(gban_handler, block=False))
dp.add_handler(CommandHandler("revert", revert, block=False))
dp.add_handler(CommandHandler("gbanlist", gbanlist, block=False))
