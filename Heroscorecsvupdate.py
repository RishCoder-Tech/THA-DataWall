import streamlit as st
import pandas as pd

st.title("Hero Score Calculator")

# Define default factors
default_factors = {
    "Apprenticeship Badges": {"score": 0, "weight": 0.3},
    "Art Badges": {"score": 0, "weight": 0.07},
    "Civilization Badges": {"score": 0, "weight": 0.01},
    "Grammar Badges": {"score": 0, "weight": 0.01},
    "Math Badges": {"score": 0, "weight": 0.01},
    "Next Great Adventure Badges": {"score": 0, "weight": 0.01},
    "PE Badges": {"score": 0, "weight": 0.01},
    "Quests Badges": {"score": 0, "weight": 0.01},
    "Reading Badges": {"score": 0, "weight": 0.01},
    "Foreign Language Badges": {"score": 0, "weight": 0.01},
    "Science Badges": {"score": 0, "weight": 0.01},
    "Servant Leader Badges": {"score": 0, "weight": 0.01},
    "Genre Badges": {"score": 0, "weight": 0.01},
    "Capstone Badges": {"score": 0, "weight": 0.01}
}

# File uploader widget
uploaded_file = st.file_uploader("Upload CSV file", type=["csv"])

# Initialize DataFrame and factors
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    
    # Ensure all required columns are present in the DataFrame
    if not all(col in df.columns for col in default_factors.keys()):
        st.warning("Uploaded CSV is missing some required columns.")
        st.stop()

    # Initialize factors from the uploaded CSV
    factors = {key: {"score": df[key].iloc[0] if key in df.columns else 0, "weight": value["weight"]}
               for key, value in default_factors.items()}
else:
    # Initialize factors from Streamlit inputs
    factors = {key: {"score": st.number_input(key, min_value=0, value=0), "weight": value["weight"]}
               for key, value in default_factors.items()}

# Calculate Hero Score
hero_score = 0
for factor_name, factor_data in factors.items():
    if factor_name == "Apprenticeship Badges":
        nga_badge_score = (factor_data["score"] / 4) * 100  # Example: 4 badges = 100%
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

# Create a DataFrame for the new values
new_data = {**{key: [factor["score"]] for key, factor in factors.items()}, "Hero Score": [hero_score]}
df_new = pd.DataFrame(new_data)

# Append new data to the existing CSV data or use new DataFrame if no file was uploaded
if uploaded_file is not None:
    df_combined = pd.concat([df, df_new], ignore_index=True)
else:
    df_combined = df_new

# Provide the updated CSV file for download
st.download_button(
    label="Download Updated CSV",
    data=df_combined.to_csv(index=False),
    file_name='updated_hero_score.csv',
    mime='text/csv'
)
