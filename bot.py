import os
from dotenv import load_dotenv
from telegram import Bot, Update
from telegram.ext import CommandHandler, Application, ContextTypes

load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")
bot = Bot(token=BOT_TOKEN)
application = Application.builder().token(BOT_TOKEN).build()

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('Hello! Use /demoinline to get started.')

async def demoinline(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('This is an inline demo.')

def handle_update(update):
    application.process_update(update)

application.add_handler(CommandHandler("start", start))
application.add_handler(CommandHandler("demoinline", demoinline))