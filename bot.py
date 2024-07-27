import logging
import os
import http.server
import socketserver
from threading import Thread
from telegram import Update, BotCommand
from telegram.ext import Updater, CommandHandler, CallbackContext

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

    # Start the dummy HTTP server
    http_thread = Thread(target=start_http_server)
    http_thread.start()

    updater.idle()

if __name__ == '__main__':
    main()
