import streamlit as st
import pandas as pd

def read_excel(file):
    df = pd.read_excel(file, engine='openpyxl', read_only=True)
    return df

st.title('Excel File Reader (Read-Only)')

file = st.file_uploader('Upload an Excel file', type=['xlsx', 'xls'])

if file is not None:
    df = read_excel(file)
    st.write(df.head())
