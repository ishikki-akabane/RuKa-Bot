import requests
from Sumi import CASH_API_KEY, dispatcher
from telegram import Update, ParseMode
from telegram.ext import CallbackContext, CommandHandler, run_async
from Sumi.modules.sql.clear_cmd_sql import get_clearcmd
from Sumi.modules.helper_funcs.misc import delete


def convert(update: Update, context: CallbackContext):
    chat = update.effective_chat
    args = update.effective_message.text.split(" ")

    if len(args) == 4:
        try:
            orig_cur_amount = float(args[1])

        except ValueError:
            update.effective_message.reply_text("Invalid amount of currency")
            return

        orig_cur = args[2].upper()

        new_cur = args[3].upper()

        request_url = (
            f"https://www.alphavantage.co/query"
            f"?function=CURRENCY_EXCHANGE_RATE"
            f"&from_currency={orig_cur}"
            f"&to_currency={new_cur}"
            f"&apikey={CASH_API_KEY}"
        )
        response = requests.get(request_url).json()
        try:
            current_rate = float(
                response["Realtime Currency Exchange Rate"]["5. Exchange Rate"]
            )
        except KeyError:
            update.effective_message.reply_text("Currency not supported.")
            return
        new_cur_amount = round(orig_cur_amount * current_rate, 5)
        delmsg = update.effective_message.reply_text(
            f"{orig_cur_amount} {orig_cur} = {new_cur_amount} {new_cur}"
        )

    elif len(args) == 1:
        delmsg = update.effective_message.reply_text("Check extras module help for `/cash` usage", parse_mode=ParseMode.MARKDOWN)

    else:
        delmsg = update.effective_message.reply_text(
            f"*Invalid Args!!:* Required 3 but passed {len(args) -1}",
            parse_mode=ParseMode.MARKDOWN,
        )

    cleartime = get_clearcmd(chat.id, "cash")

    if cleartime:
        context.dispatcher.run_async(delete, delmsg, cleartime.time)


CONVERTER_HANDLER = CommandHandler("cash", convert, run_async=True)

dispatcher.add_handler(CONVERTER_HANDLER)
