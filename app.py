# app.py
import streamlit as st
from dashboard import load_dashboard
from auth import login, signup, reset
from utils.db import init_db

st.set_page_config(page_title="Mind Muscle Meal", layout="wide")
init_db()

if "page" not in st.session_state:
    st.session_state.page = "login"
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

def logout():
    st.session_state.authenticated = False
    st.session_state.page = "login"
    st.session_state.user_data = {}

if st.session_state.authenticated:
    with st.sidebar:
        if st.button("🔓 Logout"):
            logout()
    load_dashboard(st.session_state.user_data)
else:
    st.sidebar.title("🔑 Auth Navigation")
    if st.sidebar.button("Login",key="nav_login"):
        st.session_state.page = "login"
    if st.sidebar.button("Signup", key="nav_signup"):
        st.session_state.page = "signup"
    if st.sidebar.button("Reset Password", key="nav_reset"):
        st.session_state.page = "reset"

    if st.session_state.page == "login":
        login()
    elif st.session_state.page == "signup":
        signup()
    elif st.session_state.page == "reset":
        reset()