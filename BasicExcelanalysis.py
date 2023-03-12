import streamlit as st
import pandas as pd
import openpyxl

# Define a function to read Excel file and return a Pandas DataFrame
@st.cache
def read_excel(file):
    wb = openpyxl.load_workbook(file)
    sheet = wb.active
    data = sheet.values
    cols = next(data)[0:]
    df = pd.DataFrame(data, columns=cols)
    df = df.astype(str)
    return df

# Set up the Streamlit app
st.set_page_config(page_title="Excel Analyzer", page_icon=":bar_chart:")
st.title('Excel Analyzer')
st.write('Upload an Excel file to get started.')

# Allow the user to upload a file
file = st.file_uploader('Upload an Excel file', type=['xlsx'])

if file is not None:
    # Call the read_excel function to read the file into a DataFrame
    df = read_excel(file)

    # Display some basic information about the data
    st.write(f'Number of rows: {df.shape[0]}')
    st.write(f'Number of columns: {df.shape[1]}')

    # Display the data using the st.dataframe widget
    st.write('Data:')
    st.dataframe(df)

    # Perform some basic analysis on the data and display the results
    st.write('Basic analysis:')
    st.write(df.describe())
