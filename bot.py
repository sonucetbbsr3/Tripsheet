import os
import telegram
from telegram import Update
from telegram.ext import Application, CommandHandler
from flask import Flask, request

app = Flask(__name__)

BOT_TOKEN = os.getenv('BOT_TOKEN')
application = Application.builder().token(BOT_TOKEN).build()

async def start(update: Update, context: telegram.ext.CallbackContext):
    await update.message.reply_text("Hello! I am your bot.")

application.add_handler(CommandHandler("start", start))

@app.route('/webhook', methods=['POST'])
async def webhook():
    update = telegram.Update.de_json(request.get_json(force=True), application.bot)
    await application.process_update(update)
    return 'ok'

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)