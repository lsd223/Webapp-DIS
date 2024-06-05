DELETE FROM users;
DELETE FROM songs;
DELETE FROM artist;


INSERT INTO users(user_id, username, password) VALUES
(0,'aurora','123'),
(1,'minhi','321');

INSERT INTO artist(artist_id, name) VALUES
(2,'Rihanna'),
(3,'Drake');

INSERT INTO songs(song_id, name, artist_id, genre) VALUES
(4,'Umbrella',2,'pop'),
(5,'Over',3,'hiphop');

-- INSERT INTO profanity (name) VALUES
-- ('fuck'),
-- ('hell');


-- Song contains Curse
--Artist makes song
--Song has genre

