#!/bin/bash

GREEN='\033[0;32m'
NC='\033[0m' # No Color

echo "* * * * * python $PWD/SlackAraBot/bot.py" >> /etc/crontab

echo -e "${GREEN}Everything is ready, mate!${NC}"
