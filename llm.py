import os

import streamlit as st
from google import genai
from dotenv import load_dotenv


# Load local .env when running on your computer
load_dotenv()


# Try environment variable first
api_key = os.getenv("GEMINI_API_KEY")


# If running on Streamlit Cloud, read Streamlit Secrets
if not api_key:
    try:
        api_key = st.secrets["GEMINI_API_KEY"]
    except Exception:
        api_key = None


if not api_key:
    raise ValueError(
        "GEMINI_API_KEY was not found. "
        "Add it to .env locally or Streamlit Cloud Secrets."
    )


client = genai.Client(api_key=api_key)

MODEL = "gemini-3.1-flash-lite"