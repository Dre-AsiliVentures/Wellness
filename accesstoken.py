import os
import streamlit as st




my_secret = os.environ.get('WELLNESSGURU')

# Use the secret in your Streamlit application
st.write("WELLNESS Secret Password:", my_secret)
#st.write("WELLNESS New Secret Password:", new_secret)

