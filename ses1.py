"""
notes
streamlist is for frontend/ui
install streamlit using pip install streamlit
run streamlit run file_name.py
exercise 1 - intro yourself - name, hobbies with text elements
2 - pic if fav superhero - st.image and pic
widgets allow users to enter info
3- develop a word count tool giving a text araea and display the total word count
4 - basic calculator - input 2 numbers and do +, - ,/, *
5 - take a video and take input of start time
6 - ask user for audio file then play it

st.header/subheader/code/write

st.button(label='text')
st.checkbox("label")
st.selectbox("label",options=[list])
a = st.selectbox("label",options=[1,2,3,4,5])
st.write("thank you for",a)

st.multiselect(labels,options=[list])
st.slider("label",min_value=int,max_value=int, value=(default value))
st.select_slider("label",options=[list])
st.text_input("enter text") - takes in text
st.text_area("enter text") - gives larger typing area
st.file_uploader("choose a file", type=[list of file types. is optional], accept_mutliple_files = T/F(also optional))
file = st.file_uploader("choose a file")
st.image(file)

st.color_picker(label="select a color")
st.audio("name of file")
st.video("name of file",start_time=##)
"""


import streamlit as st

st.header("Arnav")
st.write("hobby is: reading novels")

st.image("tny.png", caption="superhero")

a = st.text_area("enter text")
txt = a.replace(" ","")
st.write(len(txt))

b = st.number_input("enter no")
c = st.number_input("enter no1")
op = st.selectbox("operator",options=['+','-','*','/'])
if op == "+":
  st.write(b+c)
elif op == "-":
  st.write(b-c)
elif op == "/":
  st.write(b/c) 
else:
  st.write(b * c)


vid = st.file_uploader("choose a vid")
time = st.number_input("enter start time")
st.video(vid, start_time=time)

aud = st.file_uploader("choose a aud")
st.audio(aud)