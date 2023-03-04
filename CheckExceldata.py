import streamlit as st
import pandas as pd
from typing import List

# Set page title
st.set_page_config(page_title="Excel Analysis App")

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
        return

    # Show dataframe
    st.write("Dataframe:")
    st.write(df.head())

    # Select columns to include
    st.write("Select columns to include:")
    columns = list(df.columns)
    selected_columns: List[str] = []
    for col in columns:
        if st.checkbox(col, value=True):
            selected_columns.append(col)
    selected_df = df[selected_columns]
    st.write("Selected dataframe:")
    st.write(selected_df.head())

    # Replace missing values in the DataFrame using linear interpolation
    st.write("Interpolated dataframe:")
    interpolated_df = selected_df.interpolate(method='linear')
    st.write(interpolated_df.head())

    # Save the new file
    st.write("Save the new file:")
    file_path = st.text_input("Enter the file path to save", value="new_data.xlsx")
    if st.button("Save file"):
        interpolated_df.to_excel(file_path, index=False)
        st.success(f"File saved to {file_path}")
