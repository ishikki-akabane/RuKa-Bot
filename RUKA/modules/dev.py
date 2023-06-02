import psutil
import os
import datetime
import time

from telegram import Update
from telegram.constants import ParseMode
from telegram.ext import ContextTypes, CommandHandler

from RUKA import LOGGER, dp
from RUKA.helpers.rank_help import status


@status(rank="dev")
async def logs(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = update.effective_message
    user = update.effective_user
    chat = update.effective_chat

    if chat.type != "private":
        await message.reply_text("I sent your logs into your dm.")
        
    with open("logs.txt", "rb") as f:
        await context.bot.send_document(document=f, filename=f.name, chat_id=user.id)


async def stats(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = update.effective_message
    # Get system memory usage
    mem = psutil.virtual_memory()
    total_mem = round(mem.total / (1024 ** 2), 2)
    used_mem = round(mem.used / (1024 ** 2), 2)
    free_mem = round(mem.free / (1024 ** 2), 2)
    mem_percent = mem.percent

    # Get system storage usage
    disk = psutil.disk_usage('/')
    total_disk = round(disk.total / (1024 ** 3), 2)
    used_disk = round(disk.used / (1024 ** 3), 2)
    free_disk = round(disk.free / (1024 ** 3), 2)
    disk_percent = disk.percent

    # Get system uptime
    uptime = datetime.timedelta(seconds=int(time.time() - psutil.boot_time()))

    # Get system load average
    load_avg = os.getloadavg()

    # Compose system stats message
    msg = f"🖥 System Stats 🖥\n\n"
    msg += f"🧠 Memory: {used_mem}MB used / {free_mem}MB free ({mem_percent}%)\n"
    msg += f"💾 Storage: {used_disk}GB used / {free_disk}GB free ({disk_percent}%)\n"
    msg += f"🕒 Uptime: {uptime}\n"
    msg += f"💪 Load Avg: {load_avg[0]:.2f} (1 minute) / {load_avg[1]:.2f} (5 minutes) / {load_avg[2]:.2f} (15 minutes)"

    # Send system stats message
    await message.reply_text(msg)



dp.add_handler(CommandHandler("logs", logs, block=False))
dp.add_handler(CommandHandler("stats", stats, block=False))


__mod_name__ = "chatbot"
__help__ = ""