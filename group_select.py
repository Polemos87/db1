import pprint
import sqlalchemy

engine = sqlalchemy.create_engine('postgresql://polemos87:19871505@localhost:5432/db1')
connection = engine.connect()

sel =connection.execute("""SELECT  genre.name, COUNT(*) FROM genre
    JOIN artisgenre ON genre_id = genre.id 
    GROUP BY genre.name        
    """)
print(sel.fetchall())

sel =connection.execute("""SELECT  COUNT(*) FROM composition
    JOIN albums a ON a.id = composition.albums_id
    WHERE release BETWEEN 2019 AND 2020
    """)
print(sel.fetchall())

sel =connection.execute("""SELECT  a.name, AVG(duration) FROM composition
    JOIN albums a ON a.id = composition.albums_id
    GROUP BY a.name;
    """)
print(sel.fetchall())

sel =connection.execute("""SELECT  ar.name FROM artists ar
        WHERE ar.id NOT IN (SELECT artists.id FROM artists
            JOIN ArtistsAlbums aa ON artist_id = artists.id
            JOIN albums al ON al.id = albums_id 
            WHERE al.release = 2019)
            GROUP BY ar.name;              
            """)
print(sel.fetchall())

sel =connection.execute("""SELECT  col.name FROM artistsalbums
        JOIN artists ar ON ar.id = artistsalbums.artist_id
        JOIN albums al ON al.id = albums_id
        JOIN composition c ON c.albums_id = al.id
        JOIN CompositionCollection ON composition_id = c.id
        JOIN collection col ON col.id = collection_id
        WHERE ar.name = 'Rammstein'
        ;
        """)
print(sel.fetchall())

sel =connection.execute("""SELECT  al.name FROM artisgenre
        JOIN artists ar ON ar.id = artisgenre.artist_id
        JOIN artistsalbums aa ON aa.artist_id = ar.id
        JOIN albums al ON al.id = albums_id
        GROUP BY genre_id, al.name
        HAVING genre_id > 1
        ;
        """)
print(sel.fetchall())

sel =connection.execute("""SELECT  c.name FROM composition c
        LEFT JOIN compositioncollection ON c.id = composition_id
        WHERE collection_id is NULL                   
         ;
        """)
print(sel.fetchall())

sel =connection.execute("""SELECT  artists.name, duration FROM artists
        JOIN ArtistsAlbums aa ON artist_id = artists.id
        JOIN albums al ON al.id = aa.albums_id
        JOIN composition c ON c.albums_id = al.id
        JOIN CompositionCollection ON composition_id = c.id
        WHERE duration = (SELECT MIN(duration) FROM composition)
                         
            ;                         
            """)

sel = connection.execute("""SELECT a.name FROM albums a        
        JOIN composition c ON c.albums_id = a.id         
        WHERE c.albums_id in (SELECT albums_id FROM composition c                
            GROUP BY albums_id
            HAVING COUNT(id) = (SELECT  COUNT(id) FROM composition
                GROUP BY albums_id
                ORDER BY COUNT(id) 
        LIMIT 1))      
        ;                         
        """)
print(sel.fetchall())