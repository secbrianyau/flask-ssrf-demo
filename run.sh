#!/bin/bash
cd /home/ubuntu/website
export FLASK_ENV=development
export FLASK_APP=/home/ubuntu/website/main.py
nohup python3 -m flask run --host=0.0.0.0 --port=80 > web.log &
