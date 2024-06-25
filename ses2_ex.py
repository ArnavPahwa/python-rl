import streamlit as st
t1,t2,t3 = st.tabs(["Home","About Us","Contact Us"])
with t1:
    st.header("Welcome to XYZ comapny")
with t2:
    st.write("XYZ Technologies is a forward-thinking company at the forefront of innovation in the fields of artificial intelligence \
              and sustainable technology solutions. Established with a vision to revolutionize how businesses operate and how individuals interact with technology, XYZ Technologies specializes in developing cutting-edge AI algorithms tailored to enhance efficiency and decision-making across various industries.")

