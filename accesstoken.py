import streamlit as st
import os

# Retrieve the value of the secret
#my_secret = os.environ.get('wellnessguru')
my_secret = os.environ["wellnessguru"]

# Use the secret in your Streamlit application
st.write("WELLNESS Secret Password:", my_secret)
