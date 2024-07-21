-- Inserting users
INSERT INTO users (email, password, first_name, last_name, nickname) VALUES
('nazarpasichnyk@example.com', '123456', 'Nazar', 'Pasichnyk', 'Nazar'),
('oleksandr@example.com', '123456', 'Oleksandr', 'Surname', 'Oleksandr'),
('volodia@example.com', '123456', 'Volodia', 'Surname', 'Volodia'),
('daryna@example.com', '123456', 'Daryna', 'Surname', 'Daryna'),
('user5@example.com', '123456', 'User', 'Five', 'user5'),
('user6@example.com', '123456', 'User', 'Six', 'user6'),
('user7@example.com', '123456', 'User', 'Seven', 'user7'),
('user8@example.com', '123456', 'User', 'Eight', 'user8'),
('user9@example.com', '123456', 'User', 'Nine', 'user9'),
('user10@example.com', '123456', 'User', 'Ten', 'user10');

-- Inserting chats
INSERT INTO chats (user_1, user_2) VALUES
((SELECT id FROM users WHERE nickname = 'Nazar'), (SELECT id FROM users WHERE nickname = 'Oleksandr')),
((SELECT id FROM users WHERE nickname = 'Nazar'), (SELECT id FROM users WHERE nickname = 'Volodia')),
((SELECT id FROM users WHERE nickname = 'Nazar'), (SELECT id FROM users WHERE nickname = 'Daryna')),
((SELECT id FROM users WHERE nickname = 'Oleksandr'), (SELECT id FROM users WHERE nickname = 'Volodia')),
((SELECT id FROM users WHERE nickname = 'Oleksandr'), (SELECT id FROM users WHERE nickname = 'Daryna')),
((SELECT id FROM users WHERE nickname = 'Volodia'), (SELECT id FROM users WHERE nickname = 'Daryna')),
((SELECT id FROM users WHERE nickname = 'user5'), (SELECT id FROM users WHERE nickname = 'user6')),
((SELECT id FROM users WHERE nickname = 'user5'), (SELECT id FROM users WHERE nickname = 'user7')),
((SELECT id FROM users WHERE nickname = 'user5'), (SELECT id FROM users WHERE nickname = 'user8')),
((SELECT id FROM users WHERE nickname = 'user5'), (SELECT id FROM users WHERE nickname = 'user9')),
((SELECT id FROM users WHERE nickname = 'user5'), (SELECT id FROM users WHERE nickname = 'user10')),
((SELECT id FROM users WHERE nickname = 'user6'), (SELECT id FROM users WHERE nickname = 'user7')),
((SELECT id FROM users WHERE nickname = 'user6'), (SELECT id FROM users WHERE nickname = 'user8')),
((SELECT id FROM users WHERE nickname = 'user6'), (SELECT id FROM users WHERE nickname = 'user9')),
((SELECT id FROM users WHERE nickname = 'user6'), (SELECT id FROM users WHERE nickname = 'user10')),
((SELECT id FROM users WHERE nickname = 'user7'), (SELECT id FROM users WHERE nickname = 'user8')),
((SELECT id FROM users WHERE nickname = 'user7'), (SELECT id FROM users WHERE nickname = 'user9')),
((SELECT id FROM users WHERE nickname = 'user7'), (SELECT id FROM users WHERE nickname = 'user10')),
((SELECT id FROM users WHERE nickname = 'user8'), (SELECT id FROM users WHERE nickname = 'user9')),
((SELECT id FROM users WHERE nickname = 'user8'), (SELECT id FROM users WHERE nickname = 'user10')),
((SELECT id FROM users WHERE nickname = 'user9'), (SELECT id FROM users WHERE nickname = 'user10'));

-- Inserting messages
-- Messages for chat between Nazar and Oleksandr
INSERT INTO messages (sender, chat_id, body) VALUES
((SELECT id FROM users WHERE nickname = 'Nazar'), (SELECT id FROM chats WHERE user_1 = (SELECT id FROM users WHERE nickname = 'Nazar') AND user_2 = (SELECT id FROM users WHERE nickname = 'Oleksandr')), 'Hi Oleksandr!'),
((SELECT id FROM users WHERE nickname = 'Oleksandr'), (SELECT id FROM chats WHERE user_1 = (SELECT id FROM users WHERE nickname = 'Nazar') AND user_2 = (SELECT id FROM users WHERE nickname = 'Oleksandr')), 'Hello Nazar!'),
((SELECT id FROM users WHERE nickname = 'Nazar'), (SELECT id FROM chats WHERE user_1 = (SELECT id FROM users WHERE nickname = 'Nazar') AND user_2 = (SELECT id FROM users WHERE nickname = 'Oleksandr')), 'How are you today?'),
((SELECT id FROM users WHERE nickname = 'Oleksandr'), (SELECT id FROM chats WHERE user_1 = (SELECT id FROM users WHERE nickname = 'Nazar') AND user_2 = (SELECT id FROM users WHERE nickname = 'Oleksandr')), 'I’m doing well, thanks! How about you?'),
((SELECT id FROM users WHERE nickname = 'Nazar'), (SELECT id FROM chats WHERE user_1 = (SELECT id FROM users WHERE nickname = 'Nazar') AND user_2 = (SELECT id FROM users WHERE nickname = 'Oleksandr')), 'I’m good too. Any plans for the weekend?'),
((SELECT id FROM users WHERE nickname = 'Oleksandr'), (SELECT id FROM chats WHERE user_1 = (SELECT id FROM users WHERE nickname = 'Nazar') AND user_2 = (SELECT id FROM users WHERE nickname = 'Oleksandr')), 'Not yet, still thinking. Do you have any ideas?'),
((SELECT id FROM users WHERE nickname = 'Nazar'), (SELECT id FROM chats WHERE user_1 = (SELECT id FROM users WHERE nickname = 'Nazar') AND user_2 = (SELECT id FROM users WHERE nickname = 'Oleksandr')), 'Maybe we could go for a hike or catch a movie.'),
((SELECT id FROM users WHERE nickname = 'Oleksandr'), (SELECT id FROM chats WHERE user_1 = (SELECT id FROM users WHERE nickname = 'Nazar') AND user_2 = (SELECT id FROM users WHERE nickname = 'Oleksandr')), 'That sounds good. Let’s discuss it more tomorrow.'),
((SELECT id FROM users WHERE nickname = 'Nazar'), (SELECT id FROM chats WHERE user_1 = (SELECT id FROM users WHERE nickname = 'Nazar') AND user_2 = (SELECT id FROM users WHERE nickname = 'Oleksandr')), 'Sure, let’s do that.'),
((SELECT id FROM users WHERE nickname = 'Oleksandr'), (SELECT id FROM chats WHERE user_1 = (SELECT id FROM users WHERE nickname = 'Nazar') AND user_2 = (SELECT id FROM users WHERE nickname = 'Oleksandr')), 'By the way, have you finished the project report?'),
((SELECT id FROM users WHERE nickname = 'Nazar'), (SELECT id FROM chats WHERE user_1 = (SELECT id FROM users WHERE nickname = 'Nazar') AND user_2 = (SELECT id FROM users WHERE nickname = 'Oleksandr')), 'Not yet, but I’m almost done.'),
((SELECT id FROM users WHERE nickname = 'Oleksandr'), (SELECT id FROM chats WHERE user_1 = (SELECT id FROM users WHERE nickname = 'Nazar') AND user_2 = (SELECT id FROM users WHERE nickname = 'Oleksandr')), 'Great! I need to review it once you’re done.'),
((SELECT id FROM users WHERE nickname = 'Nazar'), (SELECT id FROM chats WHERE user_1 = (SELECT id FROM users WHERE nickname = 'Nazar') AND user_2 = (SELECT id FROM users WHERE nickname = 'Oleksandr')), 'Sure thing. I’ll send it over when it’s ready.'),
((SELECT id FROM users WHERE nickname = 'Oleksandr'), (SELECT id FROM chats WHERE user_1 = (SELECT id FROM users WHERE nickname = 'Nazar') AND user_2 = (SELECT id FROM users WHERE nickname = 'Oleksandr')), 'Thanks! I’ll be looking forward to it.'),
((SELECT id FROM users WHERE nickname = 'Nazar'), (SELECT id FROM chats WHERE user_1 = (SELECT id FROM users WHERE nickname = 'Nazar') AND user_2 = (SELECT id FROM users WHERE nickname = 'Oleksandr')), 'No problem. Let me know if you need anything else.'),
((SELECT id FROM users WHERE nickname = 'Oleksandr'), (SELECT id FROM chats WHERE user_1 = (SELECT id FROM users WHERE nickname = 'Nazar') AND user_2 = (SELECT id FROM users WHERE nickname = 'Oleksandr')), 'Will do.'),
((SELECT id FROM users WHERE nickname = 'Nazar'), (SELECT id FROM chats WHERE user_1 = (SELECT id FROM users WHERE nickname = 'Nazar') AND user_2 = (SELECT id FROM users WHERE nickname = 'Oleksandr')), 'Also, have you seen the latest episode of that show?'),
((SELECT id FROM users WHERE nickname = 'Oleksandr'), (SELECT id FROM chats WHERE user_1 = (SELECT id FROM users WHERE nickname = 'Nazar') AND user_2 = (SELECT id FROM users WHERE nickname = 'Oleksandr')), 'Not yet. Is it good?'),
((SELECT id FROM users WHERE nickname = 'Nazar'), (SELECT id FROM chats WHERE user_1 = (SELECT id FROM users WHERE nickname = 'Nazar') AND user_2 = (SELECT id FROM users WHERE nickname = 'Oleksandr')), 'It’s really good. You should check it out.'),
((SELECT id FROM users WHERE nickname = 'Oleksandr'), (SELECT id FROM chats WHERE user_1 = (SELECT id FROM users WHERE nickname = 'Nazar') AND user_2 = (SELECT id FROM users WHERE nickname = 'Oleksandr')), 'I will. Thanks for the recommendation!'),
((SELECT id FROM users WHERE nickname = 'Nazar'), (SELECT id FROM chats WHERE user_1 = (SELECT id FROM users WHERE nickname = 'Nazar') AND user_2 = (SELECT id FROM users WHERE nickname = 'Oleksandr')), 'Anytime!'),
((SELECT id FROM users WHERE nickname = 'Oleksandr'), (SELECT id FROM chats WHERE user_1 = (SELECT id FROM users WHERE nickname = 'Nazar') AND user_2 = (SELECT id FROM users WHERE nickname = 'Oleksandr')), 'Talk to you later.'),
((SELECT id FROM users WHERE nickname = 'Nazar'), (SELECT id FROM chats WHERE user_1 = (SELECT id FROM users WHERE nickname = 'Nazar') AND user_2 = (SELECT id FROM users WHERE nickname = 'Oleksandr')), 'Bye!'),
((SELECT id FROM users WHERE nickname = 'Oleksandr'), (SELECT id FROM chats WHERE user_1 = (SELECT id FROM users WHERE nickname = 'Nazar') AND user_2 = (SELECT id FROM users WHERE nickname = 'Oleksandr')), 'Bye!'),
((SELECT id FROM users WHERE nickname = 'Nazar'), (SELECT id FROM chats WHERE user_1 = (SELECT id FROM users WHERE nickname = 'Nazar') AND user_2 = (SELECT id FROM users WHERE nickname = 'Oleksandr')), 'See you tomorrow.');

-- Messages for chats between team members
INSERT INTO messages (sender, chat_id, body) VALUES
((SELECT id FROM users WHERE nickname = 'Nazar'), (SELECT id FROM chats WHERE user_1 = (SELECT id FROM users WHERE nickname = 'Nazar') AND user_2 = (SELECT id FROM users WHERE nickname = 'Oleksandr')), 'Hi Oleksandr!'),
((SELECT id FROM users WHERE nickname = 'Oleksandr'), (SELECT id FROM chats WHERE user_1 = (SELECT id FROM users WHERE nickname = 'Nazar') AND user_2 = (SELECT id FROM users WHERE nickname = 'Oleksandr')), 'Hello Nazar!'),
((SELECT id FROM users WHERE nickname = 'Nazar'), (SELECT id FROM chats WHERE user_1 = (SELECT id FROM users WHERE nickname = 'Nazar') AND user_2 = (SELECT id FROM users WHERE nickname = 'Volodia')), 'Hey Volodia, what’s up?'),
((SELECT id FROM users WHERE nickname = 'Volodia'), (SELECT id FROM chats WHERE user_1 = (SELECT id FROM users WHERE nickname = 'Nazar') AND user_2 = (SELECT id FROM users WHERE nickname = 'Volodia')), 'Not much, just working.'),
((SELECT id FROM users WHERE nickname = 'Daryna'), (SELECT id FROM chats WHERE user_1 = (SELECT id FROM users WHERE nickname = 'Nazar') AND user_2 = (SELECT id FROM users WHERE nickname = 'Daryna')), 'Hi Nazar, I need some help with the project.'),
((SELECT id FROM users WHERE nickname = 'Nazar'), (SELECT id FROM chats WHERE user_1 = (SELECT id FROM users WHERE nickname = 'Daryna') AND user_2 = (SELECT id FROM users WHERE nickname = 'Nazar')), 'Sure Daryna, what do you need?'),
((SELECT id FROM users WHERE nickname = 'Oleksandr'), (SELECT id FROM chats WHERE user_1 = (SELECT id FROM users WHERE nickname = 'Oleksandr') AND user_2 = (SELECT id FROM users WHERE nickname = 'Volodia')), 'Hi Volodia!'),
((SELECT id FROM users WHERE nickname = 'Volodia'), (SELECT id FROM chats WHERE user_1 = (SELECT id FROM users WHERE nickname = 'Oleksandr') AND user_2 = (SELECT id FROM users WHERE nickname = 'Volodia')), 'Hello Oleksandr!'),
((SELECT id FROM users WHERE nickname = 'Daryna'), (SELECT id FROM chats WHERE user_1 = (SELECT id FROM users WHERE nickname = 'Daryna') AND user_2 = (SELECT id FROM users WHERE nickname = 'Volodia')), 'Hey Volodia, are you free this weekend?'),
((SELECT id FROM users WHERE nickname = 'Volodia'), (SELECT id FROM chats WHERE user_1 = (SELECT id FROM users WHERE nickname = 'Daryna') AND user_2 = (SELECT id FROM users WHERE nickname = 'Daryna')), 'Sure Daryna, let’s talk later.'),
((SELECT id FROM users WHERE nickname = 'Nazar'), (SELECT id FROM chats WHERE user_1 = (SELECT id FROM users WHERE nickname = 'Nazar') AND user_2 = (SELECT id FROM users WHERE nickname = 'Daryna')), 'Any updates on the project?'),
((SELECT id FROM users WHERE nickname = 'Daryna'), (SELECT id FROM chats WHERE user_1 = (SELECT id FROM users WHERE nickname = 'Nazar') AND user_2 = (SELECT id FROM users WHERE nickname = 'Daryna')), 'I’m working on the design now.');


-- Messages for chats between generic users
-- Chat between user5 and user6
INSERT INTO messages (sender, chat_id, body) VALUES
((SELECT id FROM users WHERE nickname = 'user5'), (SELECT id FROM chats WHERE user_1 = (SELECT id FROM users WHERE nickname = 'user5') AND user_2 = (SELECT id FROM users WHERE nickname = 'user6')), 'Hello user6!'),
((SELECT id FROM users WHERE nickname = 'user6'), (SELECT id FROM chats WHERE user_1 = (SELECT id FROM users WHERE nickname = 'user5') AND user_2 = (SELECT id FROM users WHERE nickname = 'user6')), 'Hi user5!'),
((SELECT id FROM users WHERE nickname = 'user5'), (SELECT id FROM chats WHERE user_1 = (SELECT id FROM users WHERE nickname = 'user5') AND user_2 = (SELECT id FROM users WHERE nickname = 'user6')), 'How are you?'),
((SELECT id FROM users WHERE nickname = 'user6'), (SELECT id FROM chats WHERE user_1 = (SELECT id FROM users WHERE nickname = 'user5') AND user_2 = (SELECT id FROM users WHERE nickname = 'user6')), 'I’m good, thanks. What about you?');

-- Chat between user5 and user7
INSERT INTO messages (sender, chat_id, body) VALUES
((SELECT id FROM users WHERE nickname = 'user5'), (SELECT id FROM chats WHERE user_1 = (SELECT id FROM users WHERE nickname = 'user5') AND user_2 = (SELECT id FROM users WHERE nickname = 'user7')), 'Hi user7!'),
((SELECT id FROM users WHERE nickname = 'user7'), (SELECT id FROM chats WHERE user_1 = (SELECT id FROM users WHERE nickname = 'user5') AND user_2 = (SELECT id FROM users WHERE nickname = 'user7')), 'Hello user5!'),
((SELECT id FROM users WHERE nickname = 'user5'), (SELECT id FROM chats WHERE user_1 = (SELECT id FROM users WHERE nickname = 'user5') AND user_2 = (SELECT id FROM users WHERE nickname = 'user7')), 'What’s new?'),
((SELECT id FROM users WHERE nickname = 'user7'), (SELECT id FROM chats WHERE user_1 = (SELECT id FROM users WHERE nickname = 'user5') AND user_2 = (SELECT id FROM users WHERE nickname = 'user7')), 'Not much, just relaxing.');

-- Chat between user5 and user8
INSERT INTO messages (sender, chat_id, body) VALUES
((SELECT id FROM users WHERE nickname = 'user5'), (SELECT id FROM chats WHERE user_1 = (SELECT id FROM users WHERE nickname = 'user5') AND user_2 = (SELECT id FROM users WHERE nickname = 'user8')), 'Hello user8!'),
((SELECT id FROM users WHERE nickname = 'user8'), (SELECT id FROM chats WHERE user_1 = (SELECT id FROM users WHERE nickname = 'user5') AND user_2 = (SELECT id FROM users WHERE nickname = 'user8')), 'Hi user5!'),
((SELECT id FROM users WHERE nickname = 'user5'), (SELECT id FROM chats WHERE user_1 = (SELECT id FROM users WHERE nickname = 'user5') AND user_2 = (SELECT id FROM users WHERE nickname = 'user8')), 'Any plans for the weekend?'),
((SELECT id FROM users WHERE nickname = 'user8'), (SELECT id FROM chats WHERE user_1 = (SELECT id FROM users WHERE nickname = 'user5') AND user_2 = (SELECT id FROM users WHERE nickname = 'user8')), 'Not yet, still deciding.');

-- Chat between user6 and user7
INSERT INTO messages (sender, chat_id, body) VALUES
((SELECT id FROM users WHERE nickname = 'user6'), (SELECT id FROM chats WHERE user_1 = (SELECT id FROM users WHERE nickname = 'user6') AND user_2 = (SELECT id FROM users WHERE nickname = 'user7')), 'Hi user7!'),
((SELECT id FROM users WHERE nickname = 'user7'), (SELECT id FROM chats WHERE user_1 = (SELECT id FROM users WHERE nickname = 'user6') AND user_2 = (SELECT id FROM users WHERE nickname = 'user7')), 'Hello user6!'),
((SELECT id FROM users WHERE nickname = 'user6'), (SELECT id FROM chats WHERE user_1 = (SELECT id FROM users WHERE nickname = 'user6') AND user_2 = (SELECT id FROM users WHERE nickname = 'user7')), 'How’s it going?'),
((SELECT id FROM users WHERE nickname = 'user7'), (SELECT id FROM chats WHERE user_1 = (SELECT id FROM users WHERE nickname = 'user6') AND user_2 = (SELECT id FROM users WHERE nickname = 'user7')), 'Going well, thanks.');

-- Chat between user7 and user8
INSERT INTO messages (sender, chat_id, body) VALUES
((SELECT id FROM users WHERE nickname = 'user7'), (SELECT id FROM chats WHERE user_1 = (SELECT id FROM users WHERE nickname = 'user7') AND user_2 = (SELECT id FROM users WHERE nickname = 'user8')), 'Hello user8!'),
((SELECT id FROM users WHERE nickname = 'user8'), (SELECT id FROM chats WHERE user_1 = (SELECT id FROM users WHERE nickname = 'user7') AND user_2 = (SELECT id FROM users WHERE nickname = 'user8')), 'Hi user7!'),
((SELECT id FROM users WHERE nickname = 'user7'), (SELECT id FROM chats WHERE user_1 = (SELECT id FROM users WHERE nickname = 'user7') AND user_2 = (SELECT id FROM users WHERE nickname = 'user8')), 'What are you up to?'),
((SELECT id FROM users WHERE nickname = 'user8'), (SELECT id FROM chats WHERE user_1 = (SELECT id FROM users WHERE nickname = 'user7') AND user_2 = (SELECT id FROM users WHERE nickname = 'user8')), 'Just working on some stuff.');

-- Chat between user8 and user9
INSERT INTO messages (sender, chat_id, body) VALUES
((SELECT id FROM users WHERE nickname = 'user8'), (SELECT id FROM chats WHERE user_1 = (SELECT id FROM users WHERE nickname = 'user8') AND user_2 = (SELECT id FROM users WHERE nickname = 'user9')), 'Hi user9!'),
((SELECT id FROM users WHERE nickname = 'user9'), (SELECT id FROM chats WHERE user_1 = (SELECT id FROM users WHERE nickname = 'user8') AND user_2 = (SELECT id FROM users WHERE nickname = 'user9')), 'Hello user8!'),
((SELECT id FROM users WHERE nickname = 'user8'), (SELECT id FROM chats WHERE user_1 = (SELECT id FROM users WHERE nickname = 'user8') AND user_2 = (SELECT id FROM users WHERE nickname = 'user9')), 'Any updates on the project?'),
((SELECT id FROM users WHERE nickname = 'user9'), (SELECT id FROM chats WHERE user_1 = (SELECT id FROM users WHERE nickname = 'user8') AND user_2 = (SELECT id FROM users WHERE nickname = 'user9')), 'Not yet, but I will keep you posted.');

-- Chat between user9 and user10 (no messages)

