import subprocess
import time
from dotenv import load_dotenv

load_dotenv()

def set_webhook():
    result = subprocess.run(['./setup_webhook.sh'], check=True, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Failed to set webhook: {result.stderr}")
    else:
        print("Webhook set successfully")

if __name__ == '__main__':
    set_webhook()
    time.sleep(5)
    import webhookserver
    webhookserver.run()