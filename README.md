# Connectior

# Dependencies
Create python environment
```bash
python -m venv .venv
```
Install pip dependencies
```bash
pip install Flask flask-socketio
```

# Run
```bash
python run.py
```

# Database
## Create database
```bash
python database.py create
```
## Fill database with test data
```bash
python database.py fill
```
## Delete database file
```bash
python database.py delete
```
## Reset database
Delete and create a new empty one
```bash
python database.py reset
```