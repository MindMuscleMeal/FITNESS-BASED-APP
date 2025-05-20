import streamlit as st
from utils.openrouter_ai import generate_ai_response

def meal_section(user_data):
    st.header("🍽️ Nutrition & Meal Planning")

    tabs = st.tabs(["Meal Planning", "Grocery List", "Recipe Generator", "Hydration Assistant", "Supplement Intelligence"])

    with tabs[0]:
        st.subheader("AI-Personalized Meal Planning")
        diet = st.selectbox("Select your diet preference:", ["Vegetarian", "Vegan", "Keto", "Balanced", "Paleo"])
        calories = st.number_input("Daily calorie target:", min_value=1000, max_value=4000, value=2000)
        if st.button("Generate Meal Plan", key="meal_plan"):
            prompt = f"Create a {calories} calorie {diet} meal plan for a day."
            response = generate_ai_response(prompt)
            st.write(response)

    with tabs[1]:
        st.subheader("Smart Grocery List Generator")
        meal_type = st.selectbox("Select meal type:", ["Breakfast", "Lunch", "Dinner", "Snacks"])
        if st.button("Generate Grocery List", key="grocery_list"):
            prompt = f"Generate a grocery list for a {meal_type} meal."
            response = generate_ai_response(prompt)
            st.write(response)

    with tabs[2]:
        st.subheader("AI-Driven Recipe Generator")
        ingredients = st.text_input("Enter available ingredients (comma separated):")
        if st.button("Get Recipes", key="recipe_gen"):
            prompt = f"Generate recipes using these ingredients: {ingredients}."
            response = generate_ai_response(prompt)
            st.write(response)

    with tabs[3]:
        st.subheader("AI Hydration Assistant")
        weight = st.number_input("Enter your weight (kg):", min_value=30, max_value=200, value=70)
        activity_level = st.selectbox("Activity level:", ["Low", "Moderate", "High"])
        if st.button("Get Hydration Advice", key="hydration"):
            prompt = f"Calculate daily water intake for a {weight}kg person with {activity_level} activity."
            response = generate_ai_response(prompt)
            st.write(response)

    with tabs[4]:
        st.subheader("Supplement Intelligence")
        goals = st.text_area("Enter your fitness and health goals:")
        if st.button("Get Supplement Advice", key="supplements"):
            prompt = f"Suggest supplements based on these goals: {goals}."
            response = generate_ai_response(prompt)
            st.write(response)