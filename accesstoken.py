#from dotenv import load_dotenv
import os
import streamlit as st


load_dotenv()  # Load the secrets from .env file

# Access secrets using os.getenv('SECRET_NAME')
wellness_api_key = os.getenv('WELLNESSAPI_KEY')
# headers={
#   "authorization":st.secrets["WELLNESSGURU"]
# }
#st.write(os.environ.items())

#my_secret = os.environ.get('WELLNESSGURU')
#my_secret = os.environ['WELLNESSGURU']

# Use the secret in your Streamlit application
st.write("WELLNESS Secret Password:", st.secrets['wellness_api'])
#st.write("WELLNESS New Secret Password:", new_secret)

