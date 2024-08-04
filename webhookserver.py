from flask import Flask, request
from telegram import Update
from bot import bot, handle_update

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    if request.method == "POST":
        update = request.get_json()
        if update:
            update = Update.de_json(update, bot)
            handle_update(update)
        return 'OK', 200

def run():
    app.run(port=5000)

if __name__ == "__main__":
    run()