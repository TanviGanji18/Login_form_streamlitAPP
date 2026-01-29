import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root"
)

cursor = conn.cursor()

cursor.execute("CREATE DATABASE IF NOT EXISTS user_db")

cursor.execute("USE user_db")

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    fname VARCHAR(50),
    lname VARCHAR(50),
    username VARCHAR(50) UNIQUE,
    password VARCHAR(100)
)
""")

conn.commit()
cursor.close()
conn.close()

print("Database and table created successfully")

import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="user_db"
    )

def register_user(fname, lname, uname, pwd):
    conn = get_connection()
    cursor = conn.cursor()

    query = """
    INSERT INTO users (fname, lname, username, password)
    VALUES (%s, %s, %s, %s)
    """

    cursor.execute(query, (fname, lname, uname, pwd))
    conn.commit()

    cursor.close()
    conn.close()
def login_user(uname, pwd):
    conn = get_connection()
    cursor = conn.cursor()

    query = "SELECT * FROM users WHERE username=%s AND password=%s"
    cursor.execute(query, (uname, pwd))

    result = cursor.fetchone()

    cursor.close()
    conn.close()

    return result

