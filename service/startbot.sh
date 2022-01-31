#!/bin/bash

source /root/TradingView-Webhook-Bot/bin/activate && cd /root/TradingView-Webhook-Bot
python main.py >> /root/TradingView-Webhook-Bot/logs/TelegramBot.log 2>&1
#python main.py