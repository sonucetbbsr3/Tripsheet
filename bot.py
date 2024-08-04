import os
from dotenv import load_dotenv
from telegram import Bot, Update
from telegram.ext import CommandHandler, CallbackQueryHandler, Updater

load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")
bot = Bot(token=BOT_TOKEN)

def start(update, context):
    update.message.reply_text('Hello! Use /demoinline to get started.')

def demoinline(update, context):
    update.message.reply_text('This is an inline demo.')

def main():
    updater = Updater(token=BOT_TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("demoinline", demoinline))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()