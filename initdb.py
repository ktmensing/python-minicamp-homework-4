import sqlite3

connection = sqlite3.connect('movies.db')
print 'Opened database successfully';

connection.execute('CREATE TABLE movies (name TEXT, genre TEXT, release_date TEXT, rotten_tomatoes_rating TEXT)')
print 'Table created successfully';

connection.close()
