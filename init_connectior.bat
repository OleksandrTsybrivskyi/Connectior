
@echo off

REM Check if Python can be callable
python --version >nul 2>&1
IF %ERRORLEVEL% NEQ 0 (
    echo Python is not installed. Please install Python and/or add it to your PATH.
    echo View instruction in README.md
    exit /b
)

python -m venv .venv
call .venv\Scripts\activate
pip install flask flask-socketio

python database.py create


deactivate
echo Connectior init complete successfully.
pause
