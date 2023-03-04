import streamlit as st
import pandas as pd
import subprocess

# Install openpyxl if not already installed
st.info("Checking if openpyxl is installed...")
try:
    import openpyxl
except ImportError:
    st.info("openpyxl not found, installing...")
    subprocess.call(["pip", "install", "openpyxl"])

# Set page title and icon
st.set_page_config(page_title="Excel Analysis App", page_icon=":bar_chart:")

# Set page header
st.header("Excel Analysis App")

# Create file uploader
uploaded_file = st.file_uploader("Upload an Excel file", type=["xlsx", "xls"])

# If file is uploaded
if uploaded_file is not None:
    # Load Excel file into a pandas dataframe
    try:
        df = pd.read_excel(uploaded_file, engine="openpyxl")
    except Exception as e:
        st.error(f"Error: {str(e)}")
        st.stop()

    # Show dataframe
    st.write("Dataframe:")
    st.write(df.head())

    # Select columns to include
    st.write("Select columns to include:")
    columns = list(df.columns)
    selected_columns = []
    for col in columns:
        if st.checkbox(col, value=True):
            selected_columns.append(col)
    selected_df = df[selected_columns]
    st.write("Selected dataframe:")
    st.write(selected_df.head())

    # Get some basic statistics about the data
    st.write("Basic statistics about the data:")
    st.write(selected_df.describe())

    # Get the mean value for each column
    st.write("Mean value for each column:")
    st.write(selected_df.mean(numeric_only=True))

    # Find the maximum value in the DataFrame
    st.write("Maximum value for each column:")
    st.write(selected_df.max(numeric_only=True))

    # Find the minimum value in the DataFrame
    st.write("Minimum value for each column:")
    st.write(selected_df.min(numeric_only=True))
