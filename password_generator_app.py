import streamlit as st
import random
import string

st.title("Password Generator")

length = st.slider("Select Password Length", 6, 20)

characters = string.ascii_letters + string.digits + string.punctuation

if st.button("Generate Password"):
    
    password = ""   
    
    for i in range(length):
        password = password + random.choice(characters)

    st.write("Generated Password:", password)