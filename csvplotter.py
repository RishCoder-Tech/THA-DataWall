import streamlit as st
import pandas as pd
import matplotlib as plt
import seaborn as sns
import io

# Set up the Streamlit app
st.title('CSV Data Visualizer')
st.write('Upload multiple CSV files and visualize their data.')

# Upload multiple CSV files
uploaded_files = st.file_uploader("Choose CSV files", type="csv", accept_multiple_files=True)

# Process the files if they are uploaded
if uploaded_files:
    data_frames = []
    
    # Read each file and store it in a list of DataFrames
    for uploaded_file in uploaded_files:
        # Read the CSV file into a DataFrame
        df = pd.read_csv(uploaded_file)
        data_frames.append(df)

    # Concatenate all DataFrames into one DataFrame
    combined_df = pd.concat(data_frames, ignore_index=True)
    
    # Display a preview of the combined DataFrame
    st.write('Combined Data Preview:')
    st.write(combined_df.head())
    
    # Create a line plot if the DataFrame has numerical data
    numeric_columns = combined_df.select_dtypes(include='number').columns
    
    if len(numeric_columns) > 0:
        # Plot
        st.write('Line Plot of Numerical Data:')
        plt.figure(figsize=(10, 6))
        sns.lineplot(data=combined_df, palette='tab10')
        plt.xlabel('Index')
        plt.ylabel('Values')
        plt.title('Line Plot of Combined CSV Data')
        st.pyplot(plt)
    else:
        st.write('No numerical data found to plot.')
else:
    st.write('Please upload CSV files to display data.')
