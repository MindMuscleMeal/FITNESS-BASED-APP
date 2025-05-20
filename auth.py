# auth.py
import streamlit as st
from utils.db import add_user, get_user, reset_password

def signup():
    st.title("📝 Create Account")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    name = st.text_input("Full Name")
    age = st.number_input("Age", 10, 100)
    gender = st.selectbox("Gender", ["Male", "Female", "Other"])
    goal = st.selectbox("Fitness Goal", ["Fat Loss", "Muscle Gain", "Endurance", "General Fitness"])
    diet = st.selectbox("Diet Preference", ["None", "Vegetarian", "Vegan", "Keto", "Paleo"])

    if st.button("Sign Up"):
        if username and password:
            try:
                add_user(username, password, name, age, gender, goal, diet)
                st.success("Account created! Go to Login.")
            except:
                st.error("Username already exists.")
        else:
            st.error("Please enter all required fields.")

def login():
    st.title("🔐 Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        user = get_user(username, password)
        if user:
            st.session_state.authenticated = True
            st.session_state.user_data = {
                "name": user[3],
                "age": user[4],
                "gender": user[5],
                "fitness_goal": user[6],
                "diet_preference": user[7]
            }
            st.success("Login successful!")
        else:
            st.error("Invalid credentials.")

def reset():
    st.title("🔁 Reset Password")
    username = st.text_input("Username")
    new_password = st.text_input("New Password", type="password")

    if st.button("Reset"):
        reset_password(username, new_password)
        st.success("Password reset successful.")