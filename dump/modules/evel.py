import io
import os

# Common imports for eval
import textwrap
import traceback
from contextlib import redirect_stdout

from RUKA import dp, LOGGER
from RUKA.helpers.rank_help import status

from telegram import Update
from telegram.ext import ContextTypes, CommandHandler
from telegram.constants import ParseMode


namespaces = {}


@status(rank="dev")
async def evaluate(update, context):
    bot = context.bot
    await send(do(eval, bot, update), bot, update)


@status(rank="dev")
async def execute(update, context):
    bot = context.bot
    await send(do(exec, bot, update), bot, update)


@status(rank="dev")
async def clear_eve(update, context):
    bot = context.bot
    log_input(update)
    global namespaces
    if update.message.chat_id in namespaces:
        del namespaces[update.message.chat_id]
    await send("Cleared locals.", bot, update)


#--------------------------#--------------------------#--------------------------#--------------------------#

async def send(msg, bot, update):
    if len(str(msg)) > 2000:
        with io.BytesIO(str.encode(msg)) as out_file:
            out_file.name = "output.txt"
            await bot.send_document(chat_id=update.effective_chat.id, document=out_file)
    else:
        LOGGER.info(f"OUT: '{msg}'")
        await bot.send_message(
            chat_id=update.effective_chat.id,
            text=f"`{msg}`",
            parse_mode=ParseMode.MARKDOWN,
        )


def do(func, bot, update):
    log_input(update)
    content = update.message.text.split(" ", 1)[-1]
    body = cleanup_code(content)
    env = namespace_of(update.message.chat_id, update, bot)

    os.chdir(os.getcwd())
    with open(
        os.path.join(os.getcwd(), "RUKA/helpers/temp.txt"), "w"
    ) as temp:
        temp.write(body)

    stdout = io.StringIO()

    to_compile = f'def func():\n{textwrap.indent(body, "  ")}'

    try:
        exec(to_compile, env)
    except Exception as e:
        return f"{e.__class__.__name__}: {e}"

    func = env["func"]

    try:
        with redirect_stdout(stdout):
            func_return = func()
    except Exception as e:
        value = stdout.getvalue()
        return f"{value}{traceback.format_exc()}"
    else:
        value = stdout.getvalue()
        result = None
        if func_return is None:
            if value:
                result = f"{value}"
            else:
                try:
                    result = f"{repr(eval(body, env))}"
                except:
                    pass
        else:
            result = f"{value}{func_return}"
        if result:
            return result


def log_input(update):
    user = update.effective_user.id
    chat = update.effective_chat.id
    LOGGER.info(f"IN: {update.effective_message.text} (user={user}, chat={chat})")


def cleanup_code(code):
    if code.startswith("```") and code.endswith("```"):
        return "\n".join(code.split("\n")[1:-1])
    return code.strip("` \n")


def namespace_of(chat, update, bot):
    if chat not in namespaces:
        namespaces[chat] = {
            "__builtins__": globals()["__builtins__"],
            "bot": bot,
            "effective_message": update.effective_message,
            "effective_user": update.effective_user,
            "effective_chat": update.effective_chat,
            "update": update,
        }

    return namespaces[chat]



dp.add_handler(CommandHandler(["evel", "ev"], evaluate, block=False))
dp.add_handler(CommandHandler(["exec", "ex"], execute, block=False))
dp.add_handler(CommandHandler("clear", clear_eve, block=False))
