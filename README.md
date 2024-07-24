# Connectior
![Connectior banner](./static/imgs/connectior-banner.svg)
## Messanger python web app
Connectior is a web application that allows you to communicate with your friends using your home localhost.

This project was created during the final stage of the all-Ukrainian team programming Olympiad, which was held by [StarForLife Ukraine](https://www.sflua.org/).

---

## Video demo
Watch project preview [here](https://www.youtube.com/).

---

## How to install and run Connectior

### Install all dependencies
* Python - [official python download page](https://www.python.org/downloads/])
* Git - [official git download page](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)

### Clone git repository
Go to desired directory and clone git repository 
```bash
git clone https://github.com/OleksandrTsybrivskyi/Connectior.git
```
Navigate to project directory
```bash
cd Connectior 
```

### Create virtual environment
Create virtual environment `.venv` using command
```bash
python -m venv .venv
```
or by running script files:
* `create_environment.sh` for Linux Based OS and Mac-OS
* `create_environment.bat` for Windows

Activate vertual environment

* For Linux Based OS and Mac-OS
    ```bash
    source ./.venv/bin/activate
    ```

* For Windows
    ```bash
    .\venv\Scripts\activate.bat
    ```

Install python modules
```bash
pip install Flask flask-socketio
```

### Create database and run
> Before run this commands make sure that you have installed all needed python modules and have activated correct environment in current terminal 

Create database
```bash
python database.py create
```

Run local server
```bash
python run.py
```


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