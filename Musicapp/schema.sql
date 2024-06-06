-- GRANT ALL PRIVILEGES ON SCHEMA public TO aurora;


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

