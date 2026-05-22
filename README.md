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
