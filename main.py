import os
import subprocess
import time
import requests
from bot import application
from webhookserver import run_server

# Ensure your bot token and ngrok authtoken are set
BOT_TOKEN = '7269675192:AAFsTWjr2e2uhLLFfSpRpRbsAioJ0ELyyh8'
NGROK_AUTHTOKEN = '2YfvBHBBPX6ARFDG7S4ZM0jEupY_5CcfkAyWEuxNJUjS1iKeL'

def set_webhook():
    # Start ngrok with authtoken
    subprocess.run(['ngrok', 'config', 'add-authtoken', NGROK_AUTHTOKEN])
    ngrok_process = subprocess.Popen(['ngrok', 'http', '8443'])

    # Get the ngrok URL
    ngrok_url = ""
    while not ngrok_url:
        try:
            ngrok_response = requests.get('http://localhost:4040/api/tunnels')
            ngrok_url = ngrok_response.json()['tunnels'][0]['public_url']
            print(f"Ngrok URL: {ngrok_url}")
        except (requests.ConnectionError, IndexError):
            time.sleep(1)

    # Set the webhook for your bot
    set_webhook_url = f"https://api.telegram.org/bot{BOT_TOKEN}/setWebhook?url={ngrok_url}/webhook"
    response = requests.get(set_webhook_url)
    if response.status_code == 200:
        print("Webhook set successfully")
    else:
        print(f"Failed to set webhook: {response.text}")

if __name__ == '__main__':
    set_webhook()
    run_server()