# get_ngrok_url.py
import requests

def get_ngrok_url():
    url = "http://localhost:4040/api/tunnels"
    response = requests.get(url)
    data = response.json()
    public_url = data['tunnels'][0]['public_url']
    return public_url

if __name__ == "__main__":
    print(get_ngrok_url())