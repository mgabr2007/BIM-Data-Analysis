import streamlit as st
import pandas as pd

# Install necessary libraries
#!pip install openpyxl

# Set page title
st.set_page_config(page_title="Excel Analysis App")

# Set page header
st.header("Excel Analysis App")

# Create file uploader
uploaded_file = st.file_uploader("Upload an Excel file", type=["xlsx", "xls"])

# If file is uploaded
if uploaded_file is not None:
    # Load Excel file into a pandas dataframe
    df = pd.read_excel(uploaded_file, engine="openpyxl")

    # Show dataframe
    st.write("Dataframe:")
    st.write(df)

    # Show some statistics
    st.write("Statistics:")
    st.write(df.describe())

    # Show a bar chart
    st.write("Bar chart:")
    st.bar_chart(df)