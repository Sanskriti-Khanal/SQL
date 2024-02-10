# database_mysql.py
import mysql.connector

def create_table():
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="tkinter_auth"
    )
    cursor = connection.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INT AUTO_INCREMENT PRIMARY KEY,
            username VARCHAR(255) NOT NULL,
            password VARCHAR(255) NOT NULL
        )
    ''')

    connection.commit()
    connection.close()

def insert_user(username, password):

    
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="tkinter_auth"
    )
    cursor = connection.cursor()

    cursor.execute('INSERT INTO users (username, password) VALUES (%s, %s)', (username, password))
    connection.commit()
    connection.close()

def get_user(username, password):
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="tkinter_auth"
    )
    cursor = connection.cursor()

    cursor.execute('SELECT * FROM users WHERE username=%s AND password=%s', (username, password))
    user = cursor.fetchone()

    connection.close()
    return user



