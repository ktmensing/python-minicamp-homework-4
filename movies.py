from flask import Flask, render_template, request, jsonify
import sqlite3
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/movie', methods = ['POST'])
def addMovie():
    connection = sqlite3.connect('movies.db')
    cursor = connection.cursor()

    try:
        name = request.form['name']
        genre = request.form['genre']
        release_date = request.form['release_date']
        rotten_tomatoes_rating = request.form['rotten_tomatoes_rating']
        cursor.execute('INSERT INTO movies (name,genre,release_date,rotten_tomatoes_rating) VALUES (?,?,?,?)', (name,genre,release_date,rotten_tomatoes_rating))
        connection.commit()
        message = 'Movie added successfully!'
    except:
        connection.rollback()
        message = 'Movie was not able to be added'
    finally:
        return render_template('result.html', message = message)
        connection.close()

@app.route('/movies')
def movies():
    connection = sqlite3.connect('movies.db')
    cursor = connection.cursor()

    try:
        cursor.execute('SELECT * FROM movies')
        listOfMovies = cursor.fetchall()
        message = 'List found!'
    except:
        connection.rollback()
        message = 'Sorry, nothing was found'
    finally:
        return jsonify(listOfMovies)
        connection.close()
