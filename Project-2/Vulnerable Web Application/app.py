from flask import Flask, render_template, request, redirect, session, flash
import sqlite3
import random

app = Flask(__name__)
app.secret_key = 'secret'

def init_db():
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        username TEXT PRIMARY KEY,
        password TEXT
    )
    ''')
    cursor.execute('INSERT OR IGNORE INTO users (username, password) VALUES (?, ?)', ('admin', 'password123'))
    conn.commit()
    conn.close()

init_db()

compliments = [
    "You're awesome!",
    "You're doing great!",
    "You have a fantastic smile!",
    "You're a smart cookie!",
    "You are an amazing person!"
]

@app.route('/')
def home():
    if 'username' in session:
        compliment = random.choice(compliments)
        return render_template('home.html', username=session['username'], compliment=compliment)
    return redirect('/login')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        conn = sqlite3.connect('users.db')
        cursor = conn.cursor()

        query = f"SELECT * FROM users WHERE username='{username}' AND password='{password}'"
        cursor.execute(query)
        user = cursor.fetchone()

        if user:
            session['username'] = username
            return redirect('/')
        else:
            flash(f'Invalid credentials. Username: {username}')  
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect('/login')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)  
