from app import *

import sys
import config

if __name__ == "__main__":
    PORT: int = 0

    try:
        PORT = int(sys.argv[1])
    except IndexError:
        PORT = config.DEFAULT_PORT
        print("Setting to default port - {}")
    except ValueError:
        print("PORT must be an integer! setting to default port - {}")


    socketio.run(app, host="0.0.0.0", port=PORT, debug=True)