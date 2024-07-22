import sys
from lib.db import *
from flask import Flask

if __name__ == "__main__":
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=DATABASE_PATH,
    )

    os.makedirs(app.instance_path, exist_ok=True)


    init_app(app)

    if len(sys.argv) == 2:
        command = sys.argv[1]

        with app.app_context():
            match command:
                case "create":
                    create_db_command()
                case "fill":
                    fill_db_command()
                case "delete":
                    delete_db_command()
                case "reset":
                    reset_db_command()
                case default:
                    print(f">>> Error: there is no \"{command}\" command.")
    else:
        print(">>> Error: database.py gets in 1 argument")