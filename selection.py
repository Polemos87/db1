import sqlalchemy

engine = sqlalchemy.create_engine('postgresql://polemos87:19871505@localhost:5432/db1')
connection = engine.connect()
#
sel =connection.execute("""SELECT name,release FROM albums
    WHERE release = 2018;""")
print(sel.fetchall())

sel =connection.execute("""SELECT name,duration FROM composition
        ORDER BY duration DESC;""")
print(sel.fetchone())

sel =connection.execute("""SELECT name FROM composition
    WHERE duration >= '3:5;'""")
print(sel.fetchall())
#
sel =connection.execute("""SELECT name,release FROM collection
   WHERE release BETWEEN 2018 AND 2020 ;""")
print(sel.fetchall())

sel = connection.execute("""SELECT name FROM artists
   WHERE name NOT LIKE '%% %%' ;""")
print(sel.fetchall())

sel = connection.execute("""SELECT name FROM composition
   WHERE name iLIKE '%% my %%' OR name iLIKE '%% мой %%'  ;""")
print(sel.fetchall())



