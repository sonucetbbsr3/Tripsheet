import logging
import os
import http.server
import socketserver
from threading import Thread
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, BotCommand
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, CallbackContext

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Get the bot token from environment variables
TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')

# Define a simple request handler for the dummy HTTP server
class SimpleHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(b'Hello, world!')

def start_http_server():
    port = int(os.getenv('PORT', 8000))
    handler = SimpleHTTPRequestHandler
    with socketserver.TCPServer(("", port), handler) as httpd:
        logger.info(f"Serving HTTP on port {port}")
        httpd.serve_forever()

# Start command handler
def start(update: Update, context: CallbackContext) -> None:
    commands = [
        BotCommand("newto", "Create a new TO"),
        BotCommand("pastto", "View past TOs"),
        BotCommand("deletecurrentto", "Delete the current TO"),
        BotCommand("inlinekey", "Show inline keyboard")
    ]
    context.bot.set_my_commands(commands)
    update.message.reply_text('Commands set successfully')

# Inline keyboard handler
def inlinekey(update: Update, context: CallbackContext) -> None:
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
    update.message.reply_text('Please choose:', reply_markup=reply_markup)

def button(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    query.answer()
    query.edit_message_text(text=f"You chose option {query.data}")

# Define main function to start the bot
def main() -> None:
    updater = Updater(TOKEN)
    dispatcher = updater.dispatcher

    # Add command handlers
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("inlinekey", inlinekey))
    dispatcher.add_handler(CallbackQueryHandler(button))

    # Start the Bot
    updater.start_polling()

    # Start the dummy HTTP server
    http_thread = Thread(target=start_http_server)
    http_thread.start()

    updater.idle()

if __name__ == '__main__':
    main()
