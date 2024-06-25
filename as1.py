import streamlit as st
#Q1
st.header("Temp converter")
t = st.selectbox("Unit of temperature entered",options=["C","F"])
val = st.number_input("enter temp")
if t == "C":
    a = (val*9/5)+32
    st.write("temperature is:",int(a) , "farehneit")
elif t == "F":
    a = (val-32)*(5/9)
    st.write("temperature is:",int(a) , "celsius")

#Q2
st.header("Calculator")
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

#Q3
import random


st.header('number guesser')
if 'x' not in st.session_state:
    st.session_state.x = random.randint(1,100)


st.write(st.session_state.x)
n = st.number_input("enter whole number between 1-100",min_value=1,max_value=100,step=1)
n = int(n)


if n != 0:
    s = st.button(label='submit')
    if s:
        if n < st.session_state.x:
            st.write("your guess is too low")
        elif n > st.session_state.x:
           st.write("guess is too high")
        else:
            st.write("your guess is correct",)
regen = st.button("get new number")
if regen:
    del st.session_state.x



#4
st.header("BMI calculator")
w = st.number_input("enter weight in kg")
h = st.number_input("enter height in cm")
if w > 0 and h > 0:
    h = h/100
    bmi = w/(h*h)

    sub = st.button(label='calculate')
    if sub:
        if bmi <18.5:
            st.write("you are underweight. BMI is",bmi)
        elif bmi > 24.9:
            st.write("you are overweight. BMI is",bmi)
        else:
           st.write("weight is normal., BMI is", bmi)
#5
st.header("Audio Player")
songs = []

f_list = st.file_uploader("upload song",accept_multiple_files=True, type= ['mp4','mp3','m4a'])


#if len(f_list) > 0:
for x in f_list:
    st.write(x.name)
    songs.append(x.name)
    st.audio(x)




