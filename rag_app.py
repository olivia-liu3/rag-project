from fastapi import FastAPI
from dotenv import load_dotenv
import os
import google.generativeai as genai
from pydantic import BaseModel
from fastapi import HTTPException

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if not GEMINI_API_KEY:
    raise ValueError("GEMINI_API_KEY not found in .env file")

genai.configure(api_key=GEMINI_API_KEY)

app = FastAPI()

class QueryRequest(BaseModel):
    question: str

def validate_user_input(text: str):
        if len(text) < 3:
            raise HTTPException(status_code=400, detail="Question is too short")
        if len(text) > 100:
            raise HTTPException(status_code=400, detail="Question is too long")
        text = text.replace(" ", "")
        if len(text) == 0:
            raise HTTPException(status_code=400, detail="Question is empty")

def validate_model_output(text: str):
    if len(text) < 3:
        raise HTTPException(status_code=500, detail="Response is too short")
    text = text.strip()
    if len(text) == 0:
        raise HTTPException(status_code=500, detail="Response is empty")

def review_model_output(original_answer: str):
    review_prompt = f"you are checking over an answer that another AI already wrote. make sure the answer is relavant. if the answer is unclear, missing pieces, not concise, or badly written, fix it. if the answer is good, do not do anything and return the response. here is the answer from the other AI: {original_answer}"
    model = genai.GenerativeModel("gemini-3.5-flash")
    review_response = model.generate_content(review_prompt)
    return review_response.text
  
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

@app.post("/query")
def query_ai(request: QueryRequest):
    question = request.question
    validate_user_input(question)
    model = genai.GenerativeModel("gemini-3.5-flash")  
    query_response = model.generate_content(question) 
    raw_answer = query_response.text  
    validate_model_output(raw_answer)
    reviewed_answer =review_model_output(raw_answer)
    return reviewed_answer
