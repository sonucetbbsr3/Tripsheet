from flask import Flask, request
from bot import bot
import os

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    if request.method == "POST":
        update = request.get_json()
        bot.process_new_updates([Update.de_json(update, bot)])
        return 'OK'

if __name__ == "__main__":
    app.run(port=5000)