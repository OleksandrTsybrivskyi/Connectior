
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,

    email VARCHAR(128) NOT NULL UNIQUE,
    password VARCHAR(256) NOT NULL,

    first_name VARCHAR(16) NOT NULL,
    last_name VARCHAR(16),

    nickname VARCHAR(16) NOT NULL UNIQUE
);

CREATE TABLE IF NOT EXISTS chats (
    id INTEGER PRIMARY KEY AUTOINCREMENT,

    user_1 INTEGER NOT NULL,
    user_2 INTEGER NOT NULL,
    
    last_message_id INTEGER DEFAULT NULL,

    -- user_A and user_B was created just to make sure two users only have one chat
    -- user_A and user_B for unique check
    user_A TEXT GENERATED ALWAYS AS (CASE WHEN user_1 < user_2 THEN user_1 ELSE user_2 END) STORED,
    user_B TEXT GENERATED ALWAYS AS (CASE WHEN user_1 < user_2 THEN user_2 ELSE user_1 END) STORED,
    UNIQUE(user_A, user_B)

    FOREIGN KEY (user_1) REFERENCES users (id),
    FOREIGN KEY (user_2) REFERENCES users (id),
    FOREIGN KEY (last_message_id) REFERENCES messages (id),

    CHECK (user_1 <> user_2)
);


CREATE TABLE IF NOT EXISTS messages (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    sender_id INTEGER NOT NULL,
    chat_id INTEGER NOT NULL,

    body VARCHAR(2048) NOT NULL,
    send_time TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    viewed BOOLEAN NOT NULL DEFAULT FALSE,

    FOREIGN KEY (sender_id) REFERENCES users (id),
    FOREIGN KEY (chat_id) REFERENCES chats (id)
);

CREATE TABLE IF NOT EXISTS unactivated_users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,

    email VARCHAR(128) NOT NULL,
    password VARCHAR(256) NOT NULL,

    first_name VARCHAR(16) NOT NULL,
    last_name VARCHAR(16),

    nickname VARCHAR(16) NOT NULL,

    activation_code VARCHAR(64) NOT NULL,
    sent_time TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);
