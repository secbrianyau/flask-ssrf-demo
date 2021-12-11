#!/bin/bash
export FLASK_ENV=development
export FLASK_APP=./main.py
nohup python3 -m flask run --host=0.0.0.0 --port=80 > web.log &
