# RAG Project

This repository contains my Retrieval-Augmented Generation (RAG) project for the GenAI Secure Coding course.

This project will be built incrementally each week.


## Git Commands Used So Far

- git clone  
- git status  
- git add  
- git commit  
- git push

# Week 4
### Set up
- created an env inside project folder
- installed project dependencies (fastapi, uvicorn, python-dotenv, google-generativeai)
- Gemini API key and inputted it into .env
- updated .gitignore to protect .env
- created an app using FastAPI that displays {"status":"running"} when someone visits

### Purpose of rag_app.py
- the file python reads
- imports abunch of tools from project dependencies 
- tells python to look at the .env file
- if there is a key, the key is stored, if not, an error appears
- creates app
- app displays {"status": "running"} when someone visits

### Questions
- what is rag or gemini logic 
- is Github used to save history and ensure that if I mess up, I can retrive an older version with ease?
- how does "return" make the app display text? doesn't print do that?

# Weel 5
### What /test-gemini does
- a end point of the server that displays the response of a prompt 
- prompt is inputted into rag_app.py, sent to Gemini, then sent to the server
- JSON is used to format the data between exchanges so its in the same "language"

### Where the Gemini call lives
- Gemini call lives inside test_gemini() in rag_app.py
- rag_app.py runs on the server, not browser so the API key is hidden

### What you learned from the Gemini documentation
- using the "All models" page, I found a model that was supported and had quota

### Questions
- what does "str(e)" in the except section of test_gemini() mean
- does return work as print? why is everything after return displayed? 
