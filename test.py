import streamlit as st
import calendar
with st.form("Form Submission", clear_on_submit=False):
    b = st.text_input("enter book name to be reserved")
    a = st.text_input("enter author of book to be reserved")
    #d = st.number_input("enter day of book collection", min_value=1,max_value=31,step=1)
    d = st.selectbox("enter day",range(1,31))
    m = st.selectbox("enter day", list(calendar.month_name)[1:])
    submit = st.form_submit_button("Click to submit")
if b != "" and a != "" and d != "":
    if submit:
        d = str(d)
        m = str(m)
        txt = "your book is reserved to be picked up at: "+ d+'/'+m 
        st.success(txt)
