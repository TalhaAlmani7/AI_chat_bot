from google import genai
from dotenv import load_dotenv

load_dotenv()

client = genai.Client()

response = client.models.generate_content(
    model = "gemini-3.1-flash-lite",
    contents = "Explain what an AI agent is in one simple sentence."
)

print(response.text)
