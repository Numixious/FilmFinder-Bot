from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

# Replace with your bot token
TOKEN = "Token"

# Define a list of movies with titles and their file_id for Telegram
movies = [
    {"title": "Inception",
        "file_id": "BQACAgQAAxkBAAEuyVFnJIv73O-UGrMaFcgVIY6gwyN6SAACBhYAArufKVFAsgWQQu6WNTYE"},
    {"title": "The Matrix", "file_id": "FILE_ID_FOR_MATRIX"},
    {"title": "Interstellar", "file_id": "FILE_ID_FOR_INTERSTELLAR"},
    {"title": "Lost", "file_id": "BQACAgIAAxkBAAEuyWFnJJLwfFyA6CsyYCQz2orrQ9EnjQAC0gUAAkPsYUn6amMMAAGuL582BA"},
    # Add more movies here with their respective file_id
]
# Start command to send a welcome message to the user


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    welcome_text = (
        "Good Films Make your Life better \n"
        "🍿 هنـــر هفتـــــم را با ما تجربه کنید... \n"

        "🎬 دانلود فیلم های به روز، آخرین اخبار، توییت، شات های جذاب سلبریتی ها، موسیقی متن آثار بزرگ سینما و... \n"
        "لطفا اسم فیلم یا سریال مورد نظر خود را وارد کنید"

    )
    await update.message.reply_text(welcome_text)

# Function to search for the movie and send the file if found


async def search_movie(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.message.text.lower()
    found_movie = next(
        (movie for movie in movies if movie["title"].lower() == query), None)

    if found_movie:
        await update.message.reply_text(f"نتیجه مورد نظر پیدا شد: {found_movie['title']}")
        # Send the movie file based on file_id
        await update.message.reply_document(found_movie["file_id"])
    else:
        await update.message.reply_text("Sorry, no matching movies found.")


def main():
    # Initialize the bot
    app = ApplicationBuilder().token(TOKEN).build()

    # Add handlers for start and movie search
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(
        filters.TEXT & ~filters.COMMAND, search_movie))

    # Start the bot
    app.run_polling()


if __name__ == "__main__":
    main()
