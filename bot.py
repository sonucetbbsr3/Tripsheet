from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler
from telegram.helpers import create_deep_linked_url

# Replace 'YOUR_BOT_TOKEN' with your actual bot token
BOT_TOKEN = '7269675192:AAFsTWjr2e2uhLLFfSpRpRbsAioJ0ELyyh8'
WEBHOOK_URL = 'https://your-ngrok-url.ngrok.io/webhook'  # This will be set dynamically by the setup script

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

def setup_webhook(application: Application, webhook_url: str) -> None:
    # Set webhook URL
    application.bot.set_webhook(url=webhook_url)

def main() -> None:
    # Add handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("demoinline", demoinline))
    application.add_handler(CallbackQueryHandler(button))
    
    # Set webhook URL
    # This value should be set dynamically after running setup_webhook.sh
    setup_webhook(application, WEBHOOK_URL)
    
    # Run the webhook server
    print("Webhook server is running...")
    application.run_webhook(port=8443)  # Ensure port matches with ngrok configuration

if __name__ == '__main__':
    main()