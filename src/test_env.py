import os
from dotenv import load_dotenv

load_dotenv()

openai_key = os.getenv("OPENAI_API_KEY")
print(f"OpenAI Key (first 5 chars): {openai_key[:5] if openai_key else 'Not Set'}")

