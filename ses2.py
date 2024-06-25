st.title('Main section')
sb = st.sidebar.text_input('Enter your name: ' ,'')
st.write('Hello',sb)
# st.write('Hello '+sb)
# st.write(f"Name: {sb}")

col1,col2 = st.columns(2)
# with col1:
#   st.header('Devika')
# with col2:
#   st.header('Ansh')

tab1,tab2 = st.tabs(["Tab1","Tab2"]) # "TAB1" = title of tab. 
col3,col4=tab1.columns(2)
col5,col6=tab2.columns(2)
with tab1 :
  st.write('This is tab1')
  with col3:
    st.header('try')
  with col4:
    st.header('error')
    
  
  # with col2:
  #   st.header('Ansh')
with tab2:
  st.write('This is tab2')
  with col5:
    st.header('try')
    col7,col8 = col5.columns(2)
    with col7:
      st.header('error')
      with col8:
        st.header('errorless')
        
with st.container():
  st.write(f"Name: RanchoLabs")
  st.write("Created for students")
st.write('Outside container')
    
import time
# with st.spinner('In progress'):
#   time.sleep(5)
#   st.warning("incorrect")
# with st.spinner('In another progress'):
#   time.sleep(5)
#   st.error("Code error")
with st.expander('wanna read,click here '):
  st.write('This is the content')
  st.write("Run the server: Start your Django development server with python manage.pyrunserver.Upload a file: Use the application form to upload a file.")

with st.form("My form",clear_on_submit=False):
  name = st.text_input("Enter your name", "")
  age = st.number_input("Enter your age", min_value=0, max_value=120)
  hobbies = st.multiselect("Select your hobbies",["Reading", "Gaming", "Traveling", "Sports"])
  submit = st.form_submit_button("done?")

if submit:
  st.write("Form submitted successfully!")
  st.balloons()
  st.write("Name:",name)
  st.write(f"Age: {age}")
  st.write(f"Hobbies: {', '.join(hobbies)}")