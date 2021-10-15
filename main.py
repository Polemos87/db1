import sqlalchemy

engine = sqlalchemy.create_engine('postgresql://polemos87:19871505@localhost:5432/db1')
connection = engine.connect()

connection.execute("""create table if not exists Collection(
	id serial primary key,
	name varchar(50) not null,
	release integer not null
);""")
connection.execute("""create table if not exists Albums(
	id serial primary key,
	name varchar(50) not null,
	release integer not null
);""")
connection.execute("""create table if not exists Composition(
	id serial primary key,
	name varchar(50) not null,
	duration time not null,
	albums_id integer references Albums(id)
);""")
connection.execute("""create table if not exists Genre(
	id serial primary key,
	name varchar(50) not null unique
);""")
connection.execute("""create table if not exists Artists(
	id serial primary key,
	name varchar(70) not null
);""")
connection.execute("""create table if not exists ArtisGenre(
	artist_id integer references Artists(id),
	genre_id integer references Genre(id),
	constraint ag primary key (artist_id, genre_id)
);""")
connection.execute("""create table if not exists CompositionCollection(
	composition_id integer references Composition(id),
	collection_id integer references Collection(id),
	constraint cc primary key (composition_id, collection_id)
);""")
connection.execute("""create table if not exists ArtistsAlbums(
	artist_id integer references Artists(id),
	albums_id integer references Albums(id),
	constraint aa primary key (artist_id, albums_id)
);""")
