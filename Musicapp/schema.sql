GRANT ALL PRIVILEGES ON SCHEMA public TO aurora;



CREATE TABLE IF NOT EXISTS users(
	user_id integer PRIMARY KEY,
	username varchar(60) NOT NULL,
	password varchar(255) NOT NULL
);

CREATE TABLE IF NOT EXISTS artist(
	artist_id integer PRIMARY KEY,
    name varchar(20)
);

CREATE TABLE IF NOT EXISTS songs(
	song_id integer PRIMARY KEY,
    name varchar(255),
	artist_id integer,
	genre varchar(120),
    FOREIGN KEY (artist_id) REFERENCES Artist(artist_id)
);

-- CREATE TABLE IF NOT EXISTS profanity(
-- 	profanity_id integer PRIMARY KEY,
--     name varchar(255)
-- );

-- CREATE TABLE IF NOT EXISTS song_profanity (
--     song_id INTEGER NOT NULL,
--     profanity_id INTEGER NOT NULL,
--     PRIMARY KEY (song_id, profanity_id),
--     FOREIGN KEY (song_id) REFERENCES songs(song_id),
--     FOREIGN KEY (profanity_id) REFERENCES profanity(profanity_id)
-- );


-- Song contains Curse
--Artist makes song
--Song has genre

-- CREATE TABLE IF NOT EXISTS manages(
-- 	emp_cpr_number INTEGER NOT NULL REFERENCES employees(id),
-- 	account_number INTEGER NOT NULL REFERENCES accounts
-- );
-- ALTER TABLE manages ADD CONSTRAINT pk_manages
--   PRIMARY KEY (emp_cpr_number, account_number)
--   ;


