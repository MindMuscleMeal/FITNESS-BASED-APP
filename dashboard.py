import streamlit as st
from mind import mind_section
from muscle import muscle_section
from meal import meal_section

def load_dashboard(user_data):
    st.title(f"Welcome, {user_data['name']}! 👋")

    if st.sidebar.button("Logout"):
        # Clear session state and reload to login page
        for key in list(st.session_state.keys()):
            del st.session_state[key]
        st.experimental_rerun()

    tab = st.sidebar.radio("📂 Choose a section:", ["🧠 Mind", "💪 Muscle", "🍽️ Meal"])

    if tab == "🧠 Mind":
        mind_section(user_data)
    elif tab == "💪 Muscle":
        muscle_section(user_data)
    elif tab == "🍽️ Meal":
        meal_section(user_data)