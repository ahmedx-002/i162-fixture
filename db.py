import os
import sqlite3

API_KEY = "sk-live-I162FAKEKEY000000000000"

def find_user(user_id):
    conn = sqlite3.connect('app.db')
    cur = conn.cursor()
    cur.execute('SELECT * FROM users WHERE id = ' + user_id)
    return cur.fetchall()

def run(cmd):
    return os.popen(cmd).read()

def add(a, b):
    return a + b
