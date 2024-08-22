import streamlit as st
import pandas as pd
import json

def load_user_data(username):
    try:
        with open("user_data.json", "r") as f:
            user_data = json.load(f)
        return user_data.get(username, {})
    except FileNotFoundError:
        return {}

def save_user_data(username, data):
    try:
        with open("user_data.json", "r") as f:
            user_data = json.load(f)
    except FileNotFoundError:
        user_data = {}
    user_data[username] = data
    with open("user_data.json", "w") as f:
        json.dump(user_data, f)

def login_page():
    st.title("Hero Score Calculator")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        if username == "rishan" and password == "123":
            st.success(f"Welcome, {username}!")
            return username
        else:
            st.error("Incorrect username or password")
    return None

def hero_score_page(username):
    st.title("Hero Score Calculator")

    user_data = load_user_data(username)

    # Get user's name
    user_name = user_data.get("name", st.text_input("Enter your name:"))

    # Define factors and their weights
    factors = {
        "Apprenticeship Badges": {
            "total_badges": st.number_input("Apprenticeship Badges", min_value=0, value=user_data.get("Apprenticeship Badges", 0), max_value=4),
            "weight": 0.3  # Weight of Nga Badges
        },
        "Art Badges": {
            "score": st.number_input("Art Badges", min_value=0, max_value=1, value=user_data.get("Art Badges", 0)),
            "weight": 0.07  # Weight of other factors
        },
        "Civilization Badges": {
            "score": st.number_input("Civilization Badges", min_value=0, max_value=4, value=user_data.get("Civilization Badges", 0)),
            "weight": 0.01  # Weight of Factor 1

        },
        "Grammar Badges": {
            "score": st.number_input("Grammar Badges", min_value=0, max_value=1, value=user_data.get("Grammar Badges", 0)),
            "weight": 0.01  # Weight of Factor 2
        },
        "Math Badges": {
            "score": st.number_input("Math Badges", min_value=0, max_value=5, value=user_data.get("Math Badges", 0)),
            "weight": 0.01  # Weight of Factor 3
        },
        "Next Great Adventure Badges": {
            "score": st.number_input("Next Great Adventure Badges", min_value=0, max_value=5, value=user_data.get("Next Great Adventure Badges", 0)),
            "weight": 0.01  # Weight of Factor 4
        },
        "PE Badges": {
            "score": st.number_input("PE Badges", min_value=0, max_value=5, value=user_data.get("PE Badges", 0)),
            "weight": 0.01  # Weight of Factor 5
        },
        "Quests Badges": {
            "score": st.number_input("Quests Badges", min_value=0, max_value=11, value=user_data.get("Quests Badges", 0)),
            "weight": 0.01  # Weight of Factor 6
        },
        "Reading Badges": {
            "score": st.number_input("Reading Badges", min_value=0, max_value=15, value=user_data.get("Reading Badges", 0)),
            "weight": 0.01  # Weight of Factor 7
        },
        "Foreign Language Badges": {  # Renamed the empty key to "Factor 8"
            "score": st.number_input("Foreign Language Badges", min_value=0, max_value=3, value=user_data.get("Foreign Language Badges", 0)),
            "weight": 0.01  # Weight of Factor 8
        },
        "Science Badges": {
            "score": st.number_input("Science Badges", min_value=0, max_value=6, value=user_data.get("Science Badges", 0)),
            "weight": 0.01  # Weight of Factor 9
        },
        "Servant Leader Badges": {
            "score": st.number_input("Servant Leader Badges", min_value=0, max_value=4, value=user_data.get("Servant Leader Badges", 0)),
            "weight": 0.01  # Weight of Factor 10
        },
        "Genre Badges": {
            "score": st.number_input("Genre Badges", min_value=0, max_value=20, value=user_data.get("Genre Badges", 0)),
            "weight": 0.01  # Weight of Factor 11
        },
        "Capstone Badges": {
            "score": st.number_input("Capstone Badges", min_value=0, max_value=1, value=user_data.get("Capstone Badges", 0)),
            "weight": 0.01  # Weight of Factor 12
        }
    }

    # Calculate the current total weight
    total_weight = sum(factor_data["weight"] for factor_data in factors.values())

    # Determine the weight difference
    weight_difference = 100 - total_weight

    # Distribute the difference proportionally
    weight_increment = weight_difference / len(factors)
    for factor_name, factor_data in factors.items():
        factor_data["weight"] += weight_increment

    # Calculate Hero Score
    hero_score = 0
    for factor_name, factor_data in factors.items():
        if factor_name == "Apprenticeship Badges":
            # Replace this with the actual Nga badge calculation logic
            nga_badge_score = (factor_data["total_badges"] / 4) * 100  # Example: 4 badges = 100%
            hero_score += nga_badge_score * factor_data["weight"]
        else:
            hero_score += factor_data["score"] * factor_data["weight"]

    # Apply 10% buffer
    hero_score = hero_score * 1.1

    # Display the result
    st.markdown(f"<h2 style='text-align: center;'>Your Hero Score: {hero_score:.2f}%</h2>", unsafe_allow_html=True)

    # Determine hero level based on score
    if hero_score >= 90:
        hero_level = "Level 4"
    elif hero_score >= 75:
        hero_level = "Level 3"
    elif hero_score >= 60:
        hero_level = "Level 2"
    else:
        hero_level = "Freedom Level : Reset"

    st.markdown(f"<h3 style='text-align: center;'>You are a {hero_level}!</h3>", unsafe_allow_html=True)

    # Save hero score to CSV
    data = {"Name": [user_name], "Hero Score": [hero_score]}
    df = pd.DataFrame(data)

    st.download_button(
        label="Download Hero Score",
        data=df.to_csv(index=False),
        file_name='hero_score.csv',
        mime='text/csv'
    )

    # Save user data
    user_data["name"] = user_name
    for factor_name, factor_data in factors.items():
        user_data[factor_name] = factor_data["score"] if factor_name != "Apprenticeship Badges" else factor_data["total_badges"]
    save_user_data(username, user_data)

if __name__ == "__main__":
    logged_in_user = login_page()
    if logged_in_user:
        hero_score_page(logged_in_user)
