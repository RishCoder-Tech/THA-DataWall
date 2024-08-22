import streamlit as st
import pandas as pd

st.title("Hero Score Calculator")

# File uploader widget
uploaded_file = st.file_uploader("Upload CSV file", type=["csv"])

# Initialize a DataFrame for the CSV data
if uploaded_file is not None:
    # Read the uploaded CSV file
    df = pd.read_csv(uploaded_file)
    st.write("Uploaded CSV data:")
    st.write(df)

    # Check if specific columns exist in the DataFrame
    if not set(factors.keys()).issubset(df.columns):
        st.warning("Uploaded CSV does not contain all required columns.")
        st.stop()

    # Use uploaded CSV values as default
    factors = {k: {"score": df[k].values[0] if k in df.columns else 0, "weight": v["weight"]} for k, v in factors.items()}
else:
    # Default values for number inputs
    factors = {
        "Apprenticeship Badges": {
            "total_badges": st.number_input("Apprenticeship Badges", min_value=0, value=0, max_value=4),
            "weight": 0.3
        },
        "Art Badges": {
            "score": st.number_input("Art Badges", min_value=0, max_value=1),
            "weight": 0.07
        },
        "Civilization Badges": {
            "score": st.number_input("Civilization Badges", min_value=0, max_value=4),
            "weight": 0.01
        },
        "Grammar Badges": {
            "score": st.number_input("Grammar Badges", min_value=0, max_value=1),
            "weight": 0.01
        },
        "Math Badges": {
            "score": st.number_input("Math Badges", min_value=0, max_value=5),
            "weight": 0.01
        },
        "Next Great Adventure Badges": {
            "score": st.number_input("Next Great Adventure Badges", min_value=0, max_value=5),
            "weight": 0.01
        },
        "PE Badges": {
            "score": st.number_input("PE Badges", min_value=0, max_value=5),
            "weight": 0.01
        },
        "Quests Badges": {
            "score": st.number_input("Quests Badges", min_value=0, max_value=11),
            "weight": 0.01
        },
        "Reading Badges": {
            "score": st.number_input("Reading Badges", min_value=0, max_value=15),
            "weight": 0.01
        },
        "Foreign Language Badges": {
            "score": st.number_input("Foreign Language Badges", min_value=0, max_value=3),
            "weight": 0.01
        },
        "Science Badges": {
            "score": st.number_input("Science Badges", min_value=0, max_value=6),
            "weight": 0.01
        },
        "Servant Leader Badges": {
            "score": st.number_input("Servant Leader Badges", min_value=0, max_value=4),
            "weight": 0.01
        },
        "Genre Badges": {
            "score": st.number_input("Genre Badges", min_value=0, max_value=20),
            "weight": 0.01
        },
        "Capstone Badges": {
            "score": st.number_input("Capstone Badges", min_value=0, max_value=1),
            "weight": 0.01
        }
    }

# Calculate Hero Score
hero_score = 0
for factor_name, factor_data in factors.items():
    if factor_name == "Apprenticeship Badges":
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

# Create a DataFrame to save the new values
data = {"Hero Score": [hero_score]}
df_new = pd.DataFrame(data)

# Save the updated hero score to CSV
if uploaded_file is not None:
    df = df.append(df_new, ignore_index=True)
else:
    df = df_new

# Provide the updated CSV file for download
st.download_button(
    label="Download Updated CSV",
    data=df.to_csv(index=False),
    file_name='updated_hero_score.csv',
    mime='text/csv'
)
