from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

# Replace with your bot token from BotFather
TOKEN = "token"


async def get_file_id(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    file_id = update.message.document.file_id if update.message.document else update.message.photo[-1].file_id
    await update.message.reply_text(f"File ID: {file_id}")


def main():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(MessageHandler(
        filters.Document.ALL | filters.PHOTO, get_file_id))

    app.run_polling()


if __name__ == "__main__":
    main()
