
import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime

st.title("Streamlit Widgets Demosntration App")
data=pd.DataFrame({
    "Name":['Sharan','Melinda','Wisdom',"Joshua Jeba"],
    "Age":[20,21,22,23],
    "Department":["CSE","ECE","EEE","MECH"]
})

st.subheader("Dataframe Display")
st.dataframe(data)

df=pd.read_csv("MortalityDataset.csv")

st.subheader("CSV File Display")

st.dataframe(df)

filter_column = st.selectbox(
    "Select column",
    ["SMOKE", "BLOOD", "MORT"]
)

# Choose category value
filter_value = st.selectbox(
    f"Select {filter_column} value",
    df[filter_column].unique()
)

# Apply filter
filtered_df = df[df[filter_column] == filter_value]

# Display filtered dataset

st.subheader(f" Filtered Data ({filter_column} = {filter_value})")
st.dataframe(filtered_df)


# Record count

st.write(f"Total records: {filtered_df.shape[0]}")
#create a page withand 
#import dataset and display as a table
#create a filter or identity one col and categories should be selection button and display the filtered data in a table


import streamlit as st

st.set_page_config(page_title="Sliding Calculator", layout="centered")

st.title("Sliding Calculator")

a = st.slider("Select first number", 0, 10, 1)
b = st.slider("Select second number", 0, 10, 1)

operation = st.radio("Select operation", ["Addition", "Subtraction", "Multiplication", "Division"])

if operation == "Addition":
    result = a + b
elif operation == "Subtraction":
    result = a - b
elif operation == "Multiplication":
    result = a * b
else:
    result = a / b if b != 0 else "Undefined"

st.subheader("Result")
st.write(result)