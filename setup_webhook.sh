#!/bin/bash
source .env
ngrok config add-authtoken $NGROK_AUTH_TOKEN
./ngrok http 5000 > /dev/null &
sleep 10
NGROK_URL=$(curl -s http://127.0.0.1:4040/api/tunnels | jq -r .tunnels[0].public_url)
curl -F "url=${NGROK_URL}/webhook" "https://api.telegram.org/bot${BOT_TOKEN}/setWebhook"