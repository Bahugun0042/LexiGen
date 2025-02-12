import os
import logging
import requests
import io
from fastapi import FastAPI, Form, UploadFile
from dotenv import load_dotenv
from ocr import extract_text_from_image
from pdf_parser import extract_text_from_pdf

# Load API Key
load_dotenv(dotenv_path="../.env")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# Initialize FastAPI
app = FastAPI()
logging.basicConfig(level=logging.INFO)

# Groq API Details
GROQ_API_URL = "https://api.groq.com/openai/v1/chat/completions"
GROQ_MODEL = "llama3-8b-8192"  # Change if needed

def call_groq_api(prompt):
    """Send a prompt to the Groq API and return the response."""
    headers = {"Authorization": f"Bearer {GROQ_API_KEY}", "Content-Type": "application/json"}
    data = {
        "model": GROQ_MODEL,
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.7
    }
    
    response = requests.post(GROQ_API_URL, json=data, headers=headers)
    
    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"]
    else:
        logging.error(f"Groq API Error: {response.text}")
        return "Error generating response from Groq API."

@app.get("/")
async def root():
    return {"message": "FastAPI Server is Running!"}

@app.post("/query")
async def process_query(query: str = Form(None), file: UploadFile = None):
    extracted_text = ""

    logging.info(f"Received Query: {query}")
    
    if file:
        try:
            file_bytes = await file.read()  # ✅ Read file as bytes
            logging.info(f"📂 Received File: {file.filename}, Size: {len(file_bytes)} bytes")

            file_ext = file.filename.split(".")[-1].lower()

            if file_ext in ["jpg", "jpeg", "png", "webp"]:
                extracted_text = extract_text_from_image(file_bytes)

            elif file_ext == "pdf":
                extracted_text = extract_text_from_pdf(io.BytesIO(file_bytes))

            logging.info(f"Extracted Text: {extracted_text[:300]}...")  # First 300 chars preview

        except Exception as e:
            logging.error(f"File processing error: {str(e)}")
            return {"error": f"File processing error: {str(e)}"}

    # ✅ If extracted text exists, append it to the user query
    final_prompt = f"User Query: {query}\n\nExtracted Text from uploaded file:\n{extracted_text}" if extracted_text else query
    ai_response = call_groq_api(final_prompt)

    return {"final_query": final_prompt, "answer": ai_response}
