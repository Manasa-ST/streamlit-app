#jan 12
import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime,time
import matplotlib.pyplot as plt

st.title("Streamlit Widgets Demonstration App")
st.header(" an overview as streamlit features")
st.subheader("Streamlit is an amazing tool for interactive web applications.")

st.text("This is a simple text output using the text element")
st.write("you can also write to render Markdown,Dataframes,or other objects")

st.markdown("### Markdown Example")
st.markdown("Streamlit supports **Markdown**,including: \n- *Italic* \n- **Bold** \n- `Code Blocks`")

st.code(st.title('Streamlit App'), language="python")

st.markdown("### Metrics widgets")
st.metric(label = "Revenue",value="$120,000",delta ="$5,000",delta_color="inverse")
st.metric(label = "User Growth",value="$120,000",delta ="-200",delta_color="normal")

st.subheader(" Selectbox Widget")

agree = st.checkbox("I agree")

feedback = st.feedback("thumbs")

tags = st.pills("Tags",["Sports","Politics","Education"])

choice_radio = st.radio("pick one",["Cat","Dog"])

status = st.segmented_control("Filter",["Open","Closed"])

enable = st.toggle("Enable feature")

choice_select = st.selectbox("pick one",["Cat","Dog"])

shopping = st.multiselect("Buy",["milk","bread","eggs"])

st.subheader("Slider and inputs")

number = st.slider("Select a number", 0, 100)

size =st.select_slider("Select size",["Small","Medium","Large"])

name = st.text_input("Enter your name")

num_input = st.number_input("Pick a number", 0,10)

text = st.text_area("Text to translate")

st.subheader("Date and Time Widgets")

birthday = st.date_input("Select your birthday",)

meeting_time = st.time_input("Select meeting time",time(9, 0))

st.subheader("File and media Inputs")

uploaded_file = st.file_uploader("Upload a csv")
if uploaded_file:
    df_uploaded = pd.read_csv(uploaded_file)
    st.dataframe(df_uploaded)

audio = st.audio_input("Record audio")

photo = st.camera_input("Take a photo")

color = st.color_picker("Pick a color")

st.subheader("User Input Summary")

st.write({
    "Agreed ":agree,
    "Feedback":feedback,
    "Tags":tags,
    "Radio Choice":choice_radio,
    "Status":status,
    "Enable Feature":enable,
    "Selected Animal":choice_select,
    "Shopping items":shopping,
})

st.set_page_config(page_title="Data display and Visualization", layout="wide")

st.title("Data Display and Visualization in Streamlit")

data = pd.DataFrame({
    "Month": ["January", "February", "March", "April"],
    "Sales": [1000, 1500, 2000, 2500],
    "Profit": [200, 300, 400, 500]
})

st.subheader("Dataframe Display")

st.write("Using st.write()")
st.write(data)

st.write("Using st.table()(static):")
st.table(data)

st.write("Using st.dataframe()(interactive):")
st.dataframe(data)

st.subheader("Built-in Streamlit Charts")

st.line_chart(data.set_index("Month")["Sales"])
st.bar_chart(data.set_index("Month")["Profit"])
st.area_chart(data.set_index("Month")[["Sales", "Profit"]])

st.subheader("Matplotlib Visualization")

fig,ax = plt.subplots()
ax.plot(data["Month"],data["Sales"],marker='o',label = "Sales")
ax.plot(data["Month"],data["Profit"],marker='s',label = "Profit")

ax.set_xlabel("Month")
ax.set_ylabel("Amount")
ax.set_title("Sales vs Profit")
ax.legend()

st.pyplot(fig)

st.header("Forms and Input Handling")

with st.form("Student_form"):
    name = st.text_input("Student name")
    marks = st.number_input("Marks obtained", 0, 100)
    submit = st.form_submit_button("Submit")

if submit:
    st.success(f"Student {name} scored {marks} marks!")
