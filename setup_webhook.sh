#!/usr/bin/env bash

# Load environment variables
source .env

# Download jq if not present
if ! [ -x "$(command -v jq)" ]; then
    echo "jq not found, downloading..."
    curl -L -o jq https://github.com/stedolan/jq/releases/download/jq-1.6/jq-linux64
    chmod +x ./jq
    JQ="./jq"
else
    JQ="jq"
fi

# Authenticate ngrok
ngrok config add-authtoken $NGROK_AUTHTOKEN

# Start ngrok
ngrok http 8443 &

# Wait for ngrok to start
sleep 5

# Fetch the ngrok URL
NGROK_URL=$(curl -s http://localhost:4040/api/tunnels | $JQ -r ".tunnels[0].public_url")

# Set the webhook
curl -s "https://api.telegram.org/bot${BOT_TOKEN}/setWebhook?url=${NGROK_URL}/webhook"

echo "Webhook URL set to: ${NGROK_URL}/webhook"