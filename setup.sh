#!/bin/bash

GREEN='\033[0;32m'
NC='\033[0m' # No Color

git clone https://github.com/AmeerAssadi/SlackAraBot.git
chmod -R 777 SlackAraBot
echo "* * * * * python $PWD/AraBot/bot.py" >> /etc/crontab

echo -e "${GREEN}Everything is ready, mate!${NC}"