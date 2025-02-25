import os
import logging
import requests
import io
import filetype
from fastapi import FastAPI, Form, UploadFile
from dotenv import load_dotenv
from ocr import extract_text_from_image
from pdf_parser import extract_text_from_pdf
from langchain.memory import ConversationBufferMemory  # ✅ Chat history memory

# Load API Key
load_dotenv(dotenv_path="../.env")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# Initialize FastAPI
app = FastAPI()
logging.basicConfig(level=logging.INFO)

# Groq API Details
GROQ_API_URL = "https://api.groq.com/openai/v1/chat/completions"
GROQ_MODEL = "llama3-8b-8192"

# ✅ Initialize chat memory
memory = ConversationBufferMemory()

def call_groq_api(user_input):
    """Send a prompt to the Groq API while maintaining conversation history."""

    # ✅ Retrieve previous chat history
    history = memory.load_memory_variables({}).get("history", "")

    # ✅ Construct final prompt with chat memory
    final_prompt = f"{history}\nUser: {user_input}\nAI:"

    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": GROQ_MODEL,
        "messages": [{"role": "user", "content": final_prompt}],
        "temperature": 0.7
    }

    try:
        response = requests.post(GROQ_API_URL, json=data, headers=headers)

        # ✅ Print response details for debugging
        logging.info(f"Groq API Status Code: {response.status_code}")
        logging.info(f"Groq API Response Text: {response.text}")

        response.raise_for_status()  # ✅ Raise error for non-200 responses

        # ✅ Check if response is empty
        if not response.text.strip():
            logging.error("Error: Empty response from Groq API.")
            return "Error: Received an empty response from Groq API."

        json_response = response.json()

        # ✅ Ensure response has expected structure
        if "choices" in json_response and json_response["choices"]:
            ai_response = json_response["choices"][0]["message"]["content"]

            # ✅ Store this interaction in memory
            memory.save_context({"input": user_input}, {"output": ai_response})

            return ai_response
        else:
            logging.error(f"Invalid JSON response structure: {json_response}")
            return "Error: Unexpected response format from Groq API."

    except requests.exceptions.RequestException as e:
        logging.error(f"Groq API Request Error: {str(e)}")
        return f"Error: {str(e)}"

    except requests.exceptions.JSONDecodeError:
        logging.error("Error: Groq API returned non-JSON response.")
        return "Error: Received an invalid response from Groq API."


@app.get("/")
async def root():
    return {"message": "FastAPI Server is Running!"}


@app.post("/query")
async def process_query(query: str = Form(None), file: UploadFile = None):
    extracted_text = ""

    logging.info(f"📩 Received Query: {query}")

    if file:
        try:
            file_bytes = await file.read()
            file_type = filetype.guess(file_bytes)

            logging.info(f"📂 Received File: {file.filename}, Size: {len(file_bytes)} bytes, Type: {file_type.mime if file_type else 'Unknown'}")

            # ✅ Ensure file type detection works
            if file_type:
                mime_type = file_type.mime
                if "image" in mime_type:
                    extracted_text = extract_text_from_image(file_bytes)
                elif mime_type == "application/pdf":
                    extracted_text = extract_text_from_pdf(io.BytesIO(file_bytes))
            else:
                logging.warning(f"❌ Unknown file type for {file.filename}. Skipping processing.")

            logging.info(f"📝 Extracted Text: {extracted_text[:500]}...")  # Log first 500 chars

        except Exception as e:
            logging.error(f"🚨 File processing error: {str(e)}")
            return {"error": f"File processing error: {str(e)}"}

    # ✅ Maintain chat history even when no file is uploaded
    user_input = query or ""  # Ensure query is not None
    if extracted_text:
        user_input += f"\n\nExtracted Text from uploaded file:\n{extracted_text}"

    if not user_input.strip():
        return {"error": "No valid input provided."}

    ai_response = call_groq_api(user_input)

    return {"final_query": user_input, "answer": ai_response}
