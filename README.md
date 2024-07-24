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

You can init Connectior using scripts:
* `init_connectior.sh` for Linux Based OS and Mac-OS
* `init_connectior.bat` for Windows
and go to [Run Connectior](#run-connectior) section.

Or setup it manually by following next steps

### Create virtual environment

Create virtual environment `.venv` using command
```bash
python -m venv .venv
```

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

### Create database
> Before run this commands make sure that you have installed all needed python modules and have activated correct environment in current terminal 

Create database
```bash
python database.py create
```

### Run Connectior
You can run Connectior
* Using scripts:
    * `run_connectior.sh` for Linux Based OS and Mac-OS
    * `run_connectior.bat` for Windows

* Or do it manually by running this in terminal
    > Before run this commands make sure that you have installed all needed python modules and have activated correct environment in current terminal 
    ```bash
    python run.py
    ```

After that you must see some output.
In it find line
```bash
* Running on <local_server_addres>
```
for example: `* Running on http://127.0.0.1:5000`

Copy <local_server_addres> and open it in your browser

## HTML rendering support
![image](https://github.com/user-attachments/assets/8a7dab59-c90e-4684-bdf8-163bc1830062)
* Image sending support
* Text side support
