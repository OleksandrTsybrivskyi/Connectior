#!/bin/bash

# Check if Python can be executed
if ! command -v python3 &> /dev/null
then
    echo "Python is not installed. Please install Python."
    echo "More instructions in README.md"
    exit
fi

python3 -m venv .venv
source .venv/bin/activate
pip install flask flask-socketio

python3 database.py create

deactivate
echo "Connectior init complete successfully."

