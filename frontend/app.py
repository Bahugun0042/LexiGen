import streamlit as st
import requests

# FastAPI backend URL
API_URL = "http://127.0.0.1:8000/query"

# Streamlit UI - Chatbot Style
st.set_page_config(page_title="LexiGen 2.0", layout="wide")

st.title("🤖 LexiGen 2.0 - AI Chatbot with Multimodal Inputs")

# Initialize session state for chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input at the bottom
query = st.chat_input("Ask something...")
uploaded_file = st.file_uploader("Upload Image/PDF (Optional)", type=["png", "jpg", "jpeg", "webp", "pdf"])

# Submit action
if query or uploaded_file:
    # Store user message in chat history
    user_message = query if query else "Uploaded a file"
    st.session_state.messages.append({"role": "user", "content": user_message})
    
    with st.chat_message("user"):
        st.markdown(user_message)
    
    # Prepare request data
    files = {"file": uploaded_file} if uploaded_file else None
    data = {"query": query}

    with st.spinner("Processing..."):
        response = requests.post(API_URL, data=data, files=files)
        result = response.json()

    # Store AI response in chat history
    ai_response = result.get("answer", "No response received")
    st.session_state.messages.append({"role": "assistant", "content": ai_response})

    # Display AI response
    with st.chat_message("assistant"):
        st.markdown(ai_response)
