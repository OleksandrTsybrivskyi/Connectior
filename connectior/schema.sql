
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    email VARCHAR(128) NOT NULL,
    password VARCHAR(256) NOT NULL,
    first_name VARCHAR(16) NOT NULL,
    last_name VARCHAR(16),
    nickname VARCHAR(32) NOT NULL
);

CREATE TABLE IF NOT EXISTS chats (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_1 INTEGER NOT NULL,
    user_2 INTEGER NOT NULL,
    FOREIGN KEY (user_1) REFERENCES users (id),
    FOREIGN KEY (user_2) REFERENCES users (id)
);

CREATE TABLE IF NOT EXISTS messages (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    sender INTEGER NOT NULL,
    chat_id INTEGER NOT NULL,
    body VARCHAR(2048) NOT NULL,
    send_time TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (sender) REFERENCES users (id),
    FOREIGN KEY (chat_id) REFERENCES chats (id)
);

CREATE TABLE IF NOT EXISTS unactivated_users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    email VARCHAR(128) NOT NULL,
    password VARCHAR(256) NOT NULL,
    first_name VARCHAR(16) NOT NULL,
    last_name VARCHAR(16),
    nickname VARCHAR(32) NOT NULL,
    activation_code TEXT NOT NULL,
    sent_time INTEGER NOT NULL
);
