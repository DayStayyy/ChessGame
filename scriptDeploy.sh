#!/bin/bash
echo "Welcome to Chess Game"
sudo python3 -m flask run -h 0.0.0.0 -p 80 &
sleep 10
exit