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
## Init database
```bash
flask --app connectior database init
```
## Fill database with test data
```bash
flask --app connectior database fill
```