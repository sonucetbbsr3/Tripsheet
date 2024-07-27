import logging
from telegram import Update, BotCommand
from telegram.ext import Updater, CommandHandler, CallbackContext

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Define your bot token
TOKEN = '7269675192:AAFsTWjr2e2uhLLFfSpRpRbsAioJ0ELyyh8'

# Start command handler
def start(update: Update, context: CallbackContext) -> None:
    commands = [
        BotCommand("newto", "Create a new TO"),
        BotCommand("pastto", "View past TOs"),
        BotCommand("deletecurrentto", "Delete the current TO"),
    ]
    context.bot.set_my_commands(commands)
    update.message.reply_text('Commands set successfully')

# Define main function to start the bot
def main() -> None:
    updater = Updater(TOKEN)
    dispatcher = updater.dispatcher

    # Add command handler for /start
    dispatcher.add_handler(CommandHandler("start", start))

    # Start the Bot
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
