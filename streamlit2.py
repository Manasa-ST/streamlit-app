import pandas as pd 
import numpy as np 
from datetime import datetime , time , date 
import matplotlib.pyplot as plt
import streamlit as st

st.title("stream lit elements")
st.header("an overview of streamlit")
st.subheader("streamlit is an amazing tool")

st.text("this is simple text output ")
st.write("you can also use write to render markdown")

st.markdown("markdown support")
st.markdown("streamlit supports **markdown** include:\n-*Italics* \n- ")

st.code("st.title('streamlit app')",language ='python')


st.markdown("Metrics widget")
st.metric(label="Revenue",value ="$120,000",delta="$5,000",delta_color="normal")
st.metric(label="User Growth",value ="$2500",delta="$-200",delta_color="normal")

st.subheader("selection widget")
agree = st.checkbox("i agree")
feedback = st.feedback("thumbs")
tags = st.pills("tags",["Sports","Politics","Education"])

choice_radio = st.radio("pick one",["Cat","Dog"])
status = st.segmented_control("filter",["Active","Inactive","Pending"]  )
enable = st.toggle("enable feature")

choice_select = st.selectbox("select option",["option 1","option 2","option 3"])
multi_choice = st.multiselect("select multiple",["option A","option B","option C"])

st.slider("select a range",0,100,(25,75))
st.number_input("enter a number",0,100,25)
name = st.text_input("enter your name")
text = st.text_area("enter your feedback")
Birth_date = st.date_input("select your birth date",min_value= date(1900,1,1),max_value=date.today())

meeting_time = st.time_input("select meeting time",time(9,0))

uploaded_file = st.file_uploader("upload a file")


audio = st.audio_input("upload audio")

photo = st.camera_input("take a photo")

color = st.color_picker("pick a color","#00ff00")

st.write({
    "Agreed" : agree,
    "Feedback" : feedback,
    "Tags": tags,
    "Radio Choice": choice_radio,
    "Segmented Control": status,
    "Enabled": enable,
    "Selectbox Choice": choice_select,
    "Multiselect Choices": multi_choice,
    "Name": name,
    "Text": text,
    "Birth Date": Birth_date,
    "Meeting Time": meeting_time,
    "Uploaded File": uploaded_file,
    "Color": color

})
data = pd.DataFrame({
    "Month": ["Jan", "Feb", "Mar", "Apr"],
    "Sales": [1200, 1500, 1800, 1700],
    "Profit": [200, 300, 450, 400]
})
st.line_chart(data.set_index("Month")[["Sales"]])
st.bar_chart(data.set_index("Month")[["Profit"]])
st.area_chart(data.set_index("Month")[["Sales","Profit"]])

fig,ax = plt.subplots()
ax.plot(data["Month"],data["Sales"],marker = "o",label="Sales")
ax.plot(data["Month"],data["Profit"],marker = "s",label="Profit")
ax.set_title("Sales and Profit over Months")
ax.set_xlabel("Month")
ax.set_ylabel("Amount")
ax.legend()
st.pyplot(fig)

with st.form("studeenet form"):
    name =  st.text_input("enter your name")
    age = st.number_input("enter your age",0,120,25)
    city = st.text_input("enter your city")
    submit = st.form_submit_button("submit")
    if submit:
        st.success(f"form submitted successfully! Name: {name}, Age: {age}, City: {city}")