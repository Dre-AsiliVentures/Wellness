from decouple import config
import os
import streamlit as st



# Retrieve the value of the secret
new_secret = config('WELLNESSGURU')

my_secret = os.environ.get('WELLNESSGURU')

# Use the secret in your Streamlit application
st.write("WELLNESS Secret Password:", my_secret)
st.write("WELLNESS New Secret Password:", new_secret)
