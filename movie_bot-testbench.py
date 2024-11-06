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

# Start command to greet users


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        "Welcome to the Movie Bot! Type the name of a movie, and I’ll check if it’s in our collection."
    )

# Function to search for the movie and send the file if found


async def search_movie(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.message.text.lower()
    found_movie = next(
        (movie for movie in movies if movie["title"].lower() == query), None)

    if found_movie:
        await update.message.reply_text(f"Found the movie: {found_movie['title']}")
        # Send the movie file based on file_id
        await update.message.reply_document(found_movie["file_id"])
    else:
        await update.message.reply_text("Sorry, no matching movies found.")


def main():
    # Initialize the bot
    app = ApplicationBuilder().token(TOKEN).build()

    # Add handlers for start and text search
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(
        filters.TEXT & ~filters.COMMAND, search_movie))

    # Start the bot
    app.run_polling()


if __name__ == "__main__":
    main()
