import streamlit as st
from utils.openrouter_ai import generate_ai_response
from utils.journal import save_journal_entry
import time

def mind_section(user_data):
    st.header("🧠 Mind Wellness")

    tabs = st.tabs(["Meditation & Breathwork", "AI Therapy Chatbot", "Journal", "Focus Mode", "Cognitive Training"])

    with tabs[0]:
        st.subheader("Personalized Meditation & Breathwork")
        mood = st.selectbox("How do you feel today?", ["Calm", "Anxious", "Energetic", "Tired"])
        if st.button("Get Meditation Suggestion", key="meditate"):
            prompt = f"Suggest a meditation and breathwork exercise for mood: {mood}."
            response = generate_ai_response(prompt)
            st.write(response)

    with tabs[1]:
        st.subheader("AI Therapy Companion")
        user_input = st.text_area("Talk to your AI therapist:", key="therapy_input")
        if st.button("Send", key="therapy_send"):
            prompt = f"Therapy session: {user_input}"
            response = generate_ai_response(prompt)
            st.write(response)

    with tabs[2]:
        st.subheader("📝 Journal Entry")
        journal_text = st.text_area("Write your thoughts here:", key="journal")
        if st.button("Save Journal", key="journal_save"):
            if journal_text.strip() == "":
                st.warning("Please write something before saving.")
            else:
                user_name = user_data.get("name", "anonymous")  
                file_path = save_journal_entry(user_name, journal_text)
                st.success(f"Journal saved to: {file_path}")


    with tabs[3]:
        st.subheader("Focus Mode")
        duration = st.slider("Select focus duration (minutes):", 10, 120, 25)
        if st.button("Start Focus Mode", key="focus_start"):
            st.info(f"Starting Focus Mode for {duration} minutes")
            with st.empty():
                for remaining in range(duration * 60, 0, -1):
                    mins, secs = divmod(remaining, 60)
                    timer_display = f"⏳ Time remaining: {mins:02d}:{secs:02d}"
                    st.markdown(f"### {timer_display}")
                    time.sleep(1)

        st.success("✅ Focus Mode complete! Great job staying focused! 🎉")

    with tabs[4]:
        st.subheader("Cognitive Skill Training")
        game = st.selectbox("Choose a game to train your brain:", ["Memory Game", "Math Puzzles", "Logic Riddles"])
        if st.button("Start Game", key="cog_game"):
            prompt = f"Provide instructions and a sample puzzle for the game: {game}."
            response = generate_ai_response(prompt)
            st.write(response)