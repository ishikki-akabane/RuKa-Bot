import os
import subprocess

from telegram import Update
from telegram.constants import ParseMode
from telegram.ext import ContextTypes, CommandHandler

from RUKA import LOGGER, dp
from RUKA.helpers.rank_help import status
from RUKA.helpers.errors import capture_error


@capture_error
@status(rank="dev")
async def shell(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = update.effective_message
    cmd = message.text.split(" ", 1)
    if len(cmd) == 1:
        await message.reply_text("ɴᴏ ᴄᴏᴍᴍᴀɴᴅ ᴡᴀs ɢɪᴠᴇɴ ᴛᴏ ᴇxᴇᴄᴜᴛᴇ!")
        return
    cmd = cmd[1]
    process = subprocess.Popen(
        cmd,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        shell=True,
    )
    stdout, stderr = process.communicate()
    reply = ""
    stderr = stderr.decode()
    stdout = stdout.decode()
    if stdout:
        reply += f"*sᴛᴅᴏᴜᴛ*\n`{stdout}`\n"
        LOGGER.info(f"Shell - {cmd} - {stdout}")
    if stderr:
        reply += f"*sᴛᴅᴇʀʀ*\n`{stderr}`\n"
        LOGGER.error(f"Shell - {cmd} - {stderr}")
    if len(reply) > 3000:
        with open("shell_output.txt", "w") as file:
            file.write(reply)
        with open("shell_output.txt", "rb") as doc:
            await context.bot.send_document(
                document=doc,
                filename=doc.name,
                reply_to_message_id=message.message_id,
                chat_id=message.chat_id,
            )
        if os.path.isfile("shell_ouput.txt"):
            os.remove("shell_output.txt")
    else:
        await message.reply_text(reply, parse_mode=ParseMode.MARKDOWN)


dp.add_handler(CommandHandler("sh", shell, block=False))
