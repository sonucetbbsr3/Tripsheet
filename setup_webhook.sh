#!/bin/bash
source myenv/bin/activate

NGROK_URL=$(python get_ngrok_url.py)
WEBHOOK_URL="$NGROK_URL/webhook"
BOT_TOKEN=$(grep BOT_TOKEN .env | cut -d '=' -f2)

echo "Setting webhook to $WEBHOOK_URL"
curl -F "url=$WEBHOOK_URL" "https://api.telegram.org/bot$BOT_TOKEN/setWebhook"