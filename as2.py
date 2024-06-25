import streamlit as st
import calendar
with st.form("Form Submission", clear_on_submit=False):
    b = st.text_input("enter book name to be reserved")
    a = st.text_input("enter author of book to be reserved")
    d = st.selectbox("enter day",range(1,31))
    m = st.selectbox("enter day", list(calendar.month_name)[1:])
    submit = st.form_submit_button("Click to submit")
if b != "" and a != "" and d != "":
    if submit:
        d = str(d)

        txt = "your book is reserved to be picked up at: "+ d+m 
        st.success(txt)

#Q2
st.header("display")

i = ['i1.png','i2.jpeg','i3.jpeg']
p = ["price1","price2","price3"]
d = ["des1","des2","des3"]
n = ["name1","name2","name3"]
pos = 0
for x in i:
    with st.container():
        img,name,price,desc = st.columns(4)
        with img:
            st.subheader("images")
            st.image(x)
        with name:
            st.subheader("name")
            st.write(n[pos])
            st.write("name")
        with price:
            st.subheader("price")
            st.write(p[pos])
        with desc:
            st.subheader("description")
            st.write(d[pos])
    pos = pos+1
    


#Q3
with st.form("tip calculator"):
    bill = st.number_input("enter bill")
    tip =st.number_input("enter tip %",min_value=0)
    calc = st.form_submit_button()
if calc:
    tip = tip/100
    total = bill*(1+tip)
    st.write("Amount is", int(total),"Rupees")

#Q4
st.header('word/char counter')
import time
w = 1
a = st.text_area("enter text")
a = a.rstrip()
txt = a.replace(" ","")

string = a
res = len(string.split())
bt = st.button("submit")
if bt:
    with st.spinner('In progress'):
        time.sleep(5)
    st.write("word count is:", res)
    st.write("char count is:",len(txt))
#Q5
ch = st.selectbox("choose", ['Temp','Len','weight'])
if ch == "Temp":
    t = st.selectbox("Unit of temperature entered",options=["C","F"])
    val = st.number_input("enter temp")
    if t == "C":
        a = (val*9/5)+32
        st.write("temperature is:",round(a,2) , "farehneit")
    elif t == "F":
        a = (val-32)*(5/9)
        st.write("temperature is:",round(a,2) , "celsius")
elif ch == "Len":
    l = st.selectbox("Unit of length entered",options=["M","Feet"])
    va = st.number_input("enter length")
    if l == "M":
        a = (va*3.281)
        st.write("length is:",round(a,2) , "Feet")
    elif l == "Feet":
        a = (va/3.281)
        st.write("weight is:",round(a,2) , "metres")
elif ch == "weight":
    w = st.selectbox("Unit of weight entered",options=["kg","pounds"])
    we = st.number_input("enter weight")
    if w == "kg":
        a = (we*2.2)
        st.write("weight is:",round(a,2) , "pounds")
    elif w == "pounds":
        a= (we/2.2)
        st.write("weight is:",round(a,2) , "kg")