import os
import subprocess
from dotenv import load_dotenv
from webhookserver import run_server

# Load environment variables
load_dotenv()

def set_webhook():
    # Run the setup script to configure ngrok and set the webhook
    subprocess.run(['./setup_webhook.sh'], check=True)

if __name__ == '__main__':
    set_webhook()
    run_server()