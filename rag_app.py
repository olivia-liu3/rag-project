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
        outline_response = model.generate_content("make an outline for a 1 page research paper on the topic of AI and ethics")
        response = model.generate_content(f"write a 1 page research paper on the topic of AI and ethics based on the following outline: {outline_response.text}")   
        return {"response": response.text}
    except Exception as e:
        return {"error": str(e)}