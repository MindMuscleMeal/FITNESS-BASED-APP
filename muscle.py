import streamlit as st
from utils.openrouter_ai import generate_ai_response

def muscle_section(user_data):
    st.header("💪 Muscle & Fitness")

    tabs = st.tabs(["Workout Generator", "Recovery Planning", "Mood-Based Workouts", "Genetic Profiling", "Equipment Match"])

    with tabs[0]:
        st.subheader("AI-Personalized Workout Generator")
        goal = st.selectbox("Select your fitness goal:", ["Build Muscle", "Lose Fat", "Increase Endurance", "Improve Flexibility"])
        experience = st.selectbox("Experience Level:", ["Beginner", "Intermediate", "Advanced"])
        available_time = st.slider("Available workout time (minutes):", 15, 120, 45)
        if st.button("Generate Workout", key="workout_gen"):
            prompt = (f"Generate a {available_time}-minute workout for a {experience} person aiming to {goal}.")
            response = generate_ai_response(prompt)
            st.write(response)

    with tabs[1]:
        st.subheader("Adaptive Recovery Planning")
        soreness_level = st.slider("Rate your muscle soreness (1-10):", 1, 10, 5)
        if st.button("Get Recovery Plan", key="recovery_plan"):
            prompt = f"Provide a recovery plan for muscle soreness level {soreness_level}."
            response = generate_ai_response(prompt)
            st.write(response)

    with tabs[2]:
        st.subheader("Workout Mood Match")
        mood = st.selectbox("Select your current mood:", ["Energetic", "Lazy", "Stressed", "Happy"])
        if st.button("Suggest Workout", key="mood_workout"):
            prompt = f"Suggest a workout matching the mood: {mood}."
            response = generate_ai_response(prompt)
            st.write(response)

    with tabs[3]:
        st.subheader("Genetic Fitness Profiling")
        enabled = st.checkbox("Enable genetic profiling insights (if data available)")
        if enabled:
            st.info("'Genetic profiling feature is enabled. (Add integration for DNA data here.)Feature to be added soon!'")

    with tabs[4]:
        st.subheader("Intelligent Equipment Matching")
        equipment = st.multiselect("Select available equipment:", ["Dumbbells", "Resistance Bands", "Kettlebell", "Treadmill", "None"])
        if st.button("Get Equipment-Based Workout", key="equip_workout"):
            prompt = f"Generate a workout using this equipment: {', '.join(equipment)}."
            response = generate_ai_response(prompt)
            st.write(response)
