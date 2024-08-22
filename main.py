import streamlit as st
import pandas as pd

st.title("Hero Score Calculator")

# Define factors and their weights
factors = {
    "Apprenticeship Badges": {
        "total_badges": st.number_input("Apprenticeship Badges", min_value=0, value=0, max_value=4),
        "weight": 0.3  # Weight of Nga Badges
    },
    "Art Badges": {
        "score": st.number_input("Art Badges", min_value=0, max_value=1),
        "weight": 0.07  # Weight of other factors
    },
    "Civilization Badges": {
        "score": st.number_input("Civilization Badges", min_value=0, max_value=4),
        "weight": 0.01  # Weight of Factor 1

    },
    "Grammar Badges": {
        "score": st.number_input("Grammar Badges", min_value=0, max_value=1),
        "weight": 0.01  # Weight of Factor 2
    },
    "Math Badges": {
        "score": st.number_input("Math Badges", min_value=0, max_value=5),
        "weight": 0.01  # Weight of Factor 3
    },
    "Next Great Adventure Badges": {
        "score": st.number_input("Next Great Adventure Badges", min_value=0, max_value=5),
        "weight": 0.01  # Weight of Factor 4
    },
    "PE Badges": {
        "score": st.number_input("PE Badges", min_value=0, max_value=5),
        "weight": 0.01  # Weight of Factor 5
    },
    "Quests Badges": {
        "score": st.number_input("Quests Badges", min_value=0, max_value=11),
        "weight": 0.01  # Weight of Factor 6
    },
    "Reading Badges": {
        "score": st.number_input("Reading Badges", min_value=0, max_value=15),
        "weight": 0.01  # Weight of Factor 7
    },
    "Foreign Language Badges": {  # Renamed the empty key to "Factor 8"
        "score": st.number_input("Foreign Language Badges", min_value=0, max_value=3),
        "weight": 0.01  # Weight of Factor 8
    },
    "Science Badges": {
        "score": st.number_input("Science Badges", min_value=0, max_value=6),
        "weight": 0.01  # Weight of Factor 9
    },
    "Servant Leader Badges": {
        "score": st.number_input("Servant Leader Badges", min_value=0, max_value=4),
        "weight": 0.01  # Weight of Factor 10
    },
    "Genre Badges": {
        "score": st.number_input("Genre Badges", min_value=0, max_value=20),
        "weight": 0.01  # Weight of Factor 11
    },
    "Capstone Badges": {
        "score": st.number_input("Capstone Badges", min_value=0, max_value=1),
        "weight": 0.01  # Weight of Factor 12
    }
}

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
data = {"Hero Score": [hero_score]}
df = pd.DataFrame(data)
df.to_csv("hero_score.csv", index=False) 

st.download_button(
    label="Download Hero Score",
    data=df.to_csv(index=False),
    file_name='hero_score.csv',
    mime='text/csv'
)
