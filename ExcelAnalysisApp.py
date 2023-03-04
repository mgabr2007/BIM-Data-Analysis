import streamlit as st
import pandas as pd
import subprocess

# Install xlrd if not already installed
with st.spinner('Installing xlrd...'):
    subprocess.check_call(["pip", "install", "xlrd"])

# Set page title
st.set_page_config(page_title="Excel Analysis App")

# Set page header
st.header("Excel Analysis App")

# Create file uploader in sidebar
with st.sidebar:
    st.write("## Upload a file")
    uploaded_file = st.file_uploader("", type=["xlsx", "xls"])

# If file is uploaded
if uploaded_file is not None:
    # Check file format
    if uploaded_file.name.endswith('.xlsx') or uploaded_file.name.endswith('.xls'):
        # Load Excel file into a pandas dataframe using xlrd engine
        try:
            df = pd.read_excel(uploaded_file, engine="xlrd")
        except Exception as e:
            st.error(f"Error: {str(e)}")
            st.stop()

        # Select columns to include in sidebar
        st.sidebar.write("## Select columns to include")
        columns = list(df.columns)
        selected_columns = []
        for col in columns:
            if st.sidebar.checkbox(col, value=True):
                selected_columns.append(col)

        # Show selected dataframe in main area
        selected_df = df[selected_columns]
        st.write("## Selected dataframe")
        st.write(selected_df.head())

        # Show basic statistics
        st.write("## Basic statistics")
        st.write(selected_df.describe())

        # Show mean, max, and min values for each column
        st.write("## Summary statistics")
        st.write(selected_df.agg(['mean', 'max', 'min']))
    else:
        st.error("Error: Invalid file format. Please upload an Excel file (.xlsx or .xls).")
