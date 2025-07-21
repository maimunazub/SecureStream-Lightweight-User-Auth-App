import streamlit as st
import re
import os

USER_FILE = 'users.txt'

# Load users from file
def load_users():
    users = {}
    if os.path.exists(USER_FILE):
        with open(USER_FILE, 'r') as file:
            for line in file:
                username, password = line.strip().split(',')
                users[username] = password
    return users

# Save new user
def save_user(username, password):
    with open(USER_FILE, 'a') as file:
        file.write(f"{username},{password}\n")

# Validate password strength
def is_password_strong(password):
    return (
        len(password) >= 8 and
        re.search(r'[A-Z]', password) and
        re.search(r'[a-z]', password) and
        re.search(r'[0-9]', password) and
        re.search(r'[!@#$%^&*(),.?":{}|<>]', password)
    )

# Streamlit App
st.title("🔐 User Registration & Login")

menu = st.sidebar.selectbox("Menu", ["Register", "Login","Exit"])

users = load_users()

if menu == "Register":
    st.subheader("Create a New Account")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Register"):
        if ' ' in username:
            st.error("Username cannot contain spaces.")
        elif username in users:
            st.error("Username already exists.")
        elif not is_password_strong(password):
            st.warning("Weak password! Use upper/lowercase, digits and special characters.")
        else:
            save_user(username, password)
            st.success("Registration successful! log in.")

elif menu == "Login":
    st.subheader("Login to Your Account")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if username in users and users[username] == password:
            st.success("Login successful!")
        else:
            st.error("Invalid username or password.")

