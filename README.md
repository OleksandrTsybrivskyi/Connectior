# Connectior

# Dependencies
Create python environment
```bash
python -m venv .venv
```
Install pip dependencies
```bash
pip install Flask
```

# Run
```bash
flask --app connectior run --debug
```

# Database
## Create database
```bash
flask --app connectior database create
```
## Fill database with test data
```bash
flask --app connectior database fill
```
## Delete database file
```bash
flask --app connectior database delete
```
## Reset database
Delete and create a new empty one
```bash
flask --app connectior database reset
```