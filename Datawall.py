import streamlit as st
import pandas as pd

# Create a dataframe to store the points
points_df = pd.DataFrame(columns=["Name", "Points"])

# Function to update the points dataframe
def update_points(name, points):
    # Check if the name already exists in the dataframe
    if name in points_df["Name"].values:
        # Update the existing points
        points_df.loc[points_df["Name"] == name, "Points"] = points
    else:
        # Add a new row to the dataframe
        points_df.loc[len(points_df)] = [name, points]

# Streamlit app
st.title("Points Tracker")

# Get the name and points from the user
name = st.text_input("Enter your name:")
points = st.number_input("Enter your points:")

# Update the points when the button is clicked
if st.button("Update Points"):
    update_points(name, points)

# Display the points dataframe
st.dataframe(points_df)