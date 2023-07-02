import os
import streamlit as st


st.write(os.environ.items())

#my_secret = os.environ.get('WELLNESSGURU')
my_secret = os.environ['WELLNESSGURU']

# Use the secret in your Streamlit application
st.write("WELLNESS Secret Password:", my_secret)
#st.write("WELLNESS New Secret Password:", new_secret)

