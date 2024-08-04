from flask import Flask, request
from telegram import Update
from bot import bot

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    if request.method == "POST":
        update = request.get_json()
        if update:
            update = Update.de_json(update, bot)
            bot.process_new_updates([update])
        return 'OK', 200

if __name__ == "__main__":
    app.run(port=5000)