import streamlit as st
import os

# Retrieve the value of the secret
my_secret = os.environ.get('WELLNESSGURU')

# Use the secret in your Streamlit application
st.write("WELLNESS Secret Password:", my_secret)
