import os
from dotenv import load_dotenv
from telegram import Bot, Update
from telegram.ext import CommandHandler, Dispatcher

load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")
bot = Bot(token=BOT_TOKEN)
dispatcher = Dispatcher(bot, None, workers=0)

def start(update, context):
    update.message.reply_text('Hello! Use /demoinline to get started.')

def demoinline(update, context):
    update.message.reply_text('This is an inline demo.')

def handle_update(update):
    dispatcher.process_update(update)

dispatcher.add_handler(CommandHandler("start", start))
dispatcher.add_handler(CommandHandler("demoinline", demoinline))