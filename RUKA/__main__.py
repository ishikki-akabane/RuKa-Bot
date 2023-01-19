from RUKA import application, LOGGER


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="I'm a bot, please talk to me!"
    )


def main():
    start_handler = CommandHandler("start", start)
    application.add_handler(start_handler)

    LOGGER.info("Using long polling.")
    application.run_polling(timeout=15, drop_pending_updates=False)

if __name__ == "__main__":
    LOGGER.info("Successfully loaded modules: ")
    main()