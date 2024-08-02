import subprocess
import time
import requests
from webhookserver import run_server

# Ensure your bot token and ngrok authtoken are set
BOT_TOKEN = '7269675192:AAFsTWjr2e2uhLLFfSpRpRbsAioJ0ELyyh8'
NGROK_AUTHTOKEN = '2YfvBHBBPX6ARFDG7S4ZM0jEupY_5CcfkAyWEuxNJUjS1iKeL'

def set_webhook():
    # Run the setup script
    subprocess.run(['./setup_webhook.sh'], check=True)

if __name__ == '__main__':
    set_webhook()
    run_server()