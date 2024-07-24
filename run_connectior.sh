#!/bin/bash

# Check if the .venv
if [ ! -d ".venv" ]; then
    echo "Virtual environment '.venv' does not exist. Please initialize the environment first."
    echo View README.md for more instruction
    exit 1
fi

source .venv/bin/activate

python3 run.py

deactivate

