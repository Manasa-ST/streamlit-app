import streamlit as st
import numpy as np
import pandas as pd
from datetime import datetime,time

st.set_page_config(page_title="Streamlit Demo", layout="wide")
st.title(" Welcome to Streamlit demosnstration app")

data = pd.DataFrame({
    "Name": ["Alice", "Bob", "Charlie", "David"],
    "Age": [25, 30, 35, 40],
    "Department": ["HR", "IT", "Finance", "Marketing"]
})

st.subheader("Employee Data")
st.dataframe(data)