import sqlalchemy

engine = sqlalchemy.create_engine('postgresql://polemos87:19871505@localhost:5432/db1')
connection = engine.connect()

connection.execute("""INSERT INTO genre(name)
    VALUES
        ('Rock'),
        ('Metal'),
        ('Pop'),
        ('Rap'),
        ('Jazz');""")

connection.execute("""INSERT INTO artists(name)
    VALUES
        ('The Beatles'),
        ('Radiohead'),
        ('Metallica'),
        ('Rammstein'),
        ('Madonna'),
        ('Britney Spears'),
        ('Eminem'),
        ('Snoop Dogg'),
        ('John Coltrane'),
        ('Louis Armstrong');""")

connection.execute("""INSERT INTO albums(name, release)
    VALUES
        ('Beatles For Sale', 1964),
        ('The King of Limbs', 2011),
        ('And Justice for All', 1988),
        ('Rosenrot', 2005),
        ('Rammstein!', 2019),
        ('Femme Fatale', 2011),
        ('Kamikaze', 2018),
        ('Revival!', 2017),
        (' Get Yo Bread Up', 2018),
        ('Stardust', 1958),
        ('Satchmo in Style', 1959),
        ('Madam X', 2020);""")

connection.execute("""INSERT INTO composition(name, duration, albums_id)
    VALUES
        ('No Reply' ,'02:15', 1),
        ('I’m a Loser' ,'2:28', 1),
        ('…And Justice for All' ,'9:45', 3),
        ('Dyers Eve' ,'5:13', 3),
        ('Bloom' ,'5:15', 2),
        ('Feral','3:13', 2),
        ('Benzin','3:46', 4),
        ('Rammstein','3:26', 5),
        ('Till the World Ends','3:26' ,6),
        ('How I Roll', '3:56', 6),
        ('The Ringer','5:37', 7),
        ('Normal','3:37', 7),
        ('Roaches In My Ashtray', '4:56', 9),
        (' Get Yo Bread Up', '3:46', 9),
        ('Love Thy Neighbor', '9:56' ,10),
        ('Time After Time', '8:57', 10),
        ('Jeannine ', '3:26', 11),
        ('You are Just in Love', '2:43', 11),
        ('God Control',' 6:19', 12),
        ('Crazy', '4:02', 12);""")

connection.execute("""INSERT INTO collection(name, release)
    VALUES
        ('first', 2019),
        ('second', 2010),
        ('third', 2020),
        ('fourth', 2011),
        ('fifth', 1970),
        ('sixth', 2001),
        ('seventh', 2012),
        ('eighth', 1987);""")

connection.execute("""INSERT INTO artisgenre(artist_id, genre_id)
    VALUES
        (1, 1),
        (1, 3),
        (2, 1),
        (3, 2),
        (4, 2),
        (5, 3),
        (6, 3),
        (7, 4),
        (8, 4),
        (9, 5),
        (10, 5);""")

connection.execute("""INSERT INTO artistsalbums(artist_id, albums_id)
    VALUES
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (4, 5),
        (5, 12),
        (6, 6),
        (7, 7),
        (7, 8),
        (8, 9),
        (9, 10),
        (10, 11);""")

connection.execute("""INSERT INTO compositioncollection(composition_id, collection_id)
    VALUES
        (1, 1),
        (3, 1),
        (2, 2),
        (4, 2),
        (5, 3),
        (7, 3),
        (6, 4),
        (8, 4),
        (9, 5),
        (11, 5),
        (10, 6),
        (12, 6),
        (13, 7),
        (15, 7),
        (16, 8),
        (18, 8);""")
