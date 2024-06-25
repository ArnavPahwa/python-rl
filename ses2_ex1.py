import streamlit as st
with st.form("Form Submission", clear_on_submit=True):
    name = st.text_input("Enter your name")
    email = st.text_input("Enter your email")
    submit = st.form_submit_button("Click to submit")
if submit:
    st.success("Form is submitted")
    st.balloons()
    


