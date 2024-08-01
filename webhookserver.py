from flask import Flask, request
from telegram import Update
from bot import get_application

app = Flask(__name__)
application = get_application()

@app.route('/webhook', methods=['POST'])
def webhook():
    update = Update.de_json(request.get_json(force=True), application.bot)
    application.update_queue.put(update)
    return 'ok'

def run_server():
    app.run(port=8443)