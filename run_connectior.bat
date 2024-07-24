@echo off

REM Check if the .venv exists
if not exist .venv (
    echo Virtual environment ".venv" does not exist. Please initialize the environment first.
    echo View README.md for more instruction
    exit /b
)

call .venv\Scripts\activate

python run.py

deactivate
