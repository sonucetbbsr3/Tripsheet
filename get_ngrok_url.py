import requests
import json

def get_ngrok_url():
    response = requests.get("http://localhost:4040/api/tunnels")
    data = json.loads(response.text)
    public_url = data['tunnels'][0]['public_url']
    return public_url

if __name__ == "__main__":
    print(get_ngrok_url())