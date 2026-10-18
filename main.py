import os
from typing import Final

from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters,
)

TOKEN: Final = os.environ["8649074381:AAG9mobdCC7vgPpmjkfR50indyWx80iuLpQ"]


async def start_command(
    update: Update, context: ContextTypes.DEFAULT_TYPE
) -> None:
    if update.effective_message:
        await update.effective_message.reply_text(
            "Welcome to Feed Reader Bot!"
        )


async def help_command(
    update: Update, context: ContextTypes.DEFAULT_TYPE
) -> None:
    if update.effective_message:
        await update.effective_message.reply_text(
            "Please add the sources you want to grab the feeds from..."
        )


def handle_response(text: str) -> str:
    if "hello" in text.lower():
        return "Hi there!"
    return "I didn't understand that."


async def handle_message(
    update: Update, context: ContextTypes.DEFAULT_TYPE
) -> None:
    message = update.effective_message
    chat = update.effective_chat

    if message is None or chat is None or message.text is None:
        return

    text = message.text
    print(f"User ({chat.id}) in {chat.type}: {text!r}")

    # In groups, only respond when the bot is mentioned.
    if chat.type in ("group", "supergroup"):
        bot_username = context.bot.username
        if not bot_username or f"@{bot_username}".lower() not in text.lower():
            return
        text = text.replace(f"@{bot_username}", "").strip()

    response = handle_response(text)
    print("Bot:", response)
    await message.reply_text(response)


async def error_handler(
    update: object, context: ContextTypes.DEFAULT_TYPE
) -> None:
    print(f"Update {update} caused error {context.error}")


def main() -> None:
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start_command))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(
        MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message)
    )
    app.add_error_handler(error_handler)

    app.run_polling(poll_interval=3)


if __name__ == "__main__":
    main()
