from fastapi import FastAPI
from dotenv import load_dotenv
import os
import google.generativeai as genai

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if not GEMINI_API_KEY:
    raise ValueError("GEMINI_API_KEY not found in .env file")

genai.configure(api_key=GEMINI_API_KEY)

app = FastAPI()
  
@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.get("/test-gemini")
def test_gemini():
    try:
        model = genai.GenerativeModel("gemini-3.5-flash")
        response = model.generate_content("Explain why the sky is blue in one paragraph.")
        return {"response": response.text}
    except Exception as e:
        return {"error": str(e)}