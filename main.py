from typing import Final
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN: Final = '8649074381:AAG9mobdCC7vgPpmjkfR50indyWx80iuLpQ'

async def start_command(update:Update,context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Welcome to Feed Reader Bot!")

async def help_command(update:Update,context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Please add the sources you want to grab the feeds from...")

'''async def start_command(update:Update,context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Welcome to Feed Reader Bot!")'''

# Responses

def handle_response(text: str) -> str:
    processed = text.lower()

    if "hello" in processed:
        return "Hi there!"
    return "I didn't understand that."


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    response = handle_response(text)
    await update.message.reply_text(response)


async def error(update:Update,context: ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} caused error {context.error}')
    
if __name__ == '__main__':
    print('starting the bot...')
    app = Application.builder().token(TOKEN).build()
    
    # Commands
    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('help', help_command))
    
    # Messages
    app.add_handler(MessageHandler(filters.TEXT, handle_message))

    # Errors
    app.add_error_handler(error)

    # Polls the bot
    print('polling...')
    app.run_polling(poll_interval=3)