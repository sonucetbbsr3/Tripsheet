from flask import Flask, request
from bot import application
from telegram import Update

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    update = Update.de_json(request.get_json(force=True), application.bot)
    application.update_queue.put(update)
    return 'ok'

def run_server():
    app.run(port=8443)