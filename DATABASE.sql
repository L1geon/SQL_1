CREATE TABLE IF NOT EXISTS genres (
	id SERIAL PRIMARY KEY,
	name VARCHAR(40) NOT NULL
);


CREATE TABLE IF NOT EXISTS performers (
	id SERIAL PRIMARY KEY,
	name VARCHAR(20) NOT NULL,
	surname VARCHAR(20),
	nickname VARCHAR(20) NOT NULL,
	genreid INTEGER REFERENCES genres(id)
);


CREATE TABLE IF NOT EXISTS albums (
	id SERIAL PRIMARY KEY,
	authorid INTEGER REFERENCES performers(id),
	name VARCHAR(60) NOT NULL,
	create_data DATE NOT NULL
);


CREATE TABLE IF NOT EXISTS songs (
	id SERIAL PRIMARY KEY,
	albumsid INTEGER REFERENCES albums(id),
	name VARCHAR(60) NOT NULL,
	duration INTEGER NOT NULL
);


CREATE TABLE IF NOT EXISTS сollection (
	id SERIAL PRIMARY KEY,
	name VARCHAR(60) NOT NULL,
	create_data DATE NOT NULL

);


CREATE TABLE IF NOT EXISTS performers_albums (
	performer_id INTEGER REFERENCES performers(id),
	album_id INTEGER REFERENCES albums(id),
	CONSTRAINT performers_albums PRIMARY KEY (performer_id, album_id)
);


CREATE TABLE IF NOT EXIST performers_genres (
	performer_id INTEGER REFERENCES performers(id),
	genres_id INTEGER REFERENCES genres(id),
	CONSTRAINT performers_genres PRIMARY KEY (performer_id, genres_id)


);


CREATE TABLE IF NOT EXIST collection_songs (
	collection_id INTEGER REFERENCES collections(id),
	song_id INTEGER REFERENCES songs(id),
	CONSTRAINT collection_songs PRIMARY KEY (collection_id, song_id)


);


CREATE TABLE IF NOT EXIST staff (
	id SERIAL PRIMARY KEY,
	name VARCHAR(60) NOT NULL,
	department_id INTEGER REFERENCES departments(id),
	boss_id INTEGER REFERENCES bosses(id)

);


CREATE TABLE IF NOT EXIST departments (
	id SERIAL PRIMARY KEY,
	name VARCHAR(120) NOT NULL

);


CREATE TABLE IF NOT EXIST bosses (
	id SERIAL PRIMARY KEY,
	worker_id INTEGER REFERENCES staff(id)

);