from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()
BOT_TOKEN = os.getenv('BOT_TOKEN')

# Create the application object
application = Application.builder().token(BOT_TOKEN).build()

async def start(update: Update, context) -> None:
    await update.message.reply_text('Hello! Use /demoinline to get an inline button.')

async def demoinline(update: Update, context) -> None:
    keyboard = [
        [
            InlineKeyboardButton("Option 1", callback_data='1'),
            InlineKeyboardButton("Option 2", callback_data='2'),
        ],
        [
            InlineKeyboardButton("Option 3", callback_data='3'),
            InlineKeyboardButton("Option 4", callback_data='4'),
        ],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text('Please choose:', reply_markup=reply_markup)

async def button(update: Update, context) -> None:
    query = update.callback_query
    await query.answer()
    selection = query.data
    await query.edit_message_text(text=f"Button {selection} was clicked.")

def setup_webhook(application: Application) -> None:
    # This function is now redundant as webhook setup is handled in setup_webhook.sh
    pass

def main() -> None:
    # Add handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("demoinline", demoinline))
    application.add_handler(CallbackQueryHandler(button))
    
    # Run the webhook server
    application.run_webhook(port=8443)  # Ensure port matches with ngrok configuration

if __name__ == '__main__':
    main()