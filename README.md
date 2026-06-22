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

# Week 6
### Description of my multi-step flow
- Makes Gemini first write an outline for a research paper 
- Using the outline from the first step, compose the research paper

### What each step does
- the line "outline_response = model.generate_content("make an outline for a 1 page research paper on the topic of AI and ethics")" creates the outline
- the next line "response = model.generate_content(f"write a 1 page research paper on the topic of AI and ethics based on the following outline: {outline_response.text}")" creates the paper
- the lines "except Exception as e:" and "return {"error": str(e)}" makes Gemini display that an error has occurred and why it has occurred

### Why steps are separated
- the seperation organizes the LLM's reasoning 
- this ensures that the essential first step (making the outline) is completed and cannot be skipped 

### Any challenges or open questions
- some words in the paper are sounded by forward slashes and quotations for no reason, how could I get rid of that?

# Week 7 
### Why does input validation exist
- filters user input by flagging prrompts that are empty, too short, or too long
- helps to ensure quality AI response

### Why does output validation exist
- prevents general errors from AI response to reach user
- raises error if response is empty or too short

### Why is a second AI model used to review responses
- a second AI model is given the role to quality control the response and less likely to make the same mistakes as the first AI 
- fixes bad responses. rewritten responses given to user
- allows good responses to reach user