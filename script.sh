#!/bin/bash
echo "Welcome to Chess Game"
python -m flask run &
sleep 10
kill $(ps aux | grep 'python -m flask run' | awk '{print $2}')
echo "Server stopped"

