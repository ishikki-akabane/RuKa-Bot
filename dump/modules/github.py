import os
import subprocess

from telegram import Update
from telegram.constants import ParseMode
from telegram.ext import ContextTypes, CommandHandler

from RUKA import LOGGER, dp
from RUKA.helpers.rank_help import status
from RUKA.helpers.errors import capture_error



@status(rank="dev")
@capture_error
async def git_pull_restart(update, context):
    # Change this to the path of your bot code directory
    await context.bot.send_message(chat_id=update.message.chat_id, text='Pulling changes!')

    bot_code_dir = '/root/Ruka-bot'

    # Change this to the URL of your GitHub repo
    repo_url = 'https://github.com/ishikki-akabane/Ruka-bot.git'

    # Change this to the name of the branch you want to pull from
    branch = 'main'

    # Change this to the command you use to start your bot
    start_command = 'python3 -m RUKA'

    # Change the working directory to your bot code directory
    os.chdir(bot_code_dir)

    # Pull the latest changes from the repo
    subprocess.run(['git', 'pull', repo_url, branch])

    # Restart the bot
    subprocess.run(start_command.split())

    # Send a message to the user indicating that the bot has been restarted
    await context.bot.send_message(chat_id=update.message.chat_id, text='Bot restarted!')


dp.add_handler(CommandHandler("gitpull", git_pull_restart, block=False))

__mod_name__ = "github"
__help__ = "git puull"
