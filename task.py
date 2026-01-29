import streamlit as st
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

    cursor.execute(
        "INSERT INTO users (fname, lname, username, password) VALUES (%s,%s,%s,%s)",
        (fname, lname, uname, pwd)
    )

    conn.commit()
    cursor.close()
    conn.close()

def login_user(uname, pwd):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM users WHERE username=%s AND password=%s",
        (uname, pwd)
    )

    user = cursor.fetchone()

    cursor.close()
    conn.close()

    return user

st.sidebar.title("Menu")
st.write("Choose an option:")
option = st.sidebar.radio(
"Choose page",
["Register", "Login"]
)

if option == "Register":
    st.header("Registration Form")
    with st.form("register"):
        fname = st.text_input("First Name")
        lname = st.text_input("Last Name")
        uname = st.text_input("User Name")
        pwd = st.text_input("Password", type="password")
        register = st.form_submit_button("register")
        if register:
            st.success("Registration successful!")
            st.write(fname, lname, uname)
elif option == "Login":
    st.header("login")
    with st.form("login_from"):
        uname = st.text_input("User Name")
        pwd = st.text_input("Password",type="password")
        login = st.form_submit_button("login")
        if login:
            st.success("Login successful")
            st.write(uname)

