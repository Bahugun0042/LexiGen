import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000/query"

st.title("LexiGen: Multimodal Query Processor")

query = st.text_area("Enter your query:", "")

uploaded_file = st.file_uploader("Upload an Image or PDF (Optional)", type=["png", "jpg", "jpeg", "webp", "pdf"])

if st.button("Submit Query"):
    if not query.strip():
        st.error("Please enter a query!")
    else:
        files = {"file": uploaded_file} if uploaded_file else None
        data = {"query": query}

        with st.spinner("Processing..."):
            response = requests.post(API_URL, data=data, files=files)
            result = response.json()

        st.subheader("AI Response:")
        st.write(result.get("answer", "No response received"))
