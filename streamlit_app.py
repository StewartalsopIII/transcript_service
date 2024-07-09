import streamlit as st
from dotenv import load_dotenv
import openai
import os

# Load environment variables
load_dotenv()

# Set your API key
openai.api_key = os.getenv("OPENAI_API_KEY")

def analyze_text(input_text):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are an objectively minded and centrist-oriented analyst."},
            {"role": "user", "content": input_text}
        ]
    )
    return response.choices[0].message['content'].strip()

# Streamlit app
st.title('Podcast Transcript Analyzer')

uploaded_file = st.file_uploader("Upload a transcript file", type="txt")

if uploaded_file is not None:
    input_text = uploaded_file.read().decode('utf-8')
    analysis = analyze_text(input_text)
    st.write("### Analysis")
    st.write(analysis)
else:
    st.write("Please upload a text file.")

# Run the Streamlit app using the command `streamlit run streamlit_app.py`
