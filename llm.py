from google import genai
from dotenv import load_dotenv

load_dotenv()

client = genai.Client()

MODEL = "gemini-3.1-flash-lite"