import subprocess
import os

def set_webhook():
    script_path = os.path.join(os.path.dirname(__file__), 'setup_webhook.sh')
    result = subprocess.run([script_path], check=True, capture_output=True, text=True)
    print(result.stdout)
    print(result.stderr)

if __name__ == "__main__":
    set_webhook()
    from webhookserver import app
    app.run(host='0.0.0.0', port=5000)