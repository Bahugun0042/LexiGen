# 🚀 **LexiGen: Multimodal Query Processor with Chat Memory**  

LexiGen is a **multimodal AI-powered query processor** that can handle **text, images, and PDFs** to provide intelligent responses using the **Groq API**. It also includes a **chat memory feature**, allowing the model to retain context within a conversation using **LangChain ConversationBufferMemory**.
---

## **🔥 Features**  
✅ **Text Query Processing** – Accepts and processes text-based user queries.  
✅ **Image Processing (OCR)** – Extracts text from images using **Tesseract OCR**.  
✅ **PDF Processing** – Reads and extracts meaningful text from **PDFs (pdfplumber)**.  
✅ **AI-Powered Responses** – Uses **Groq API (LLaMA3-8B)** for intelligent answers.  
✅ **Chat Memory** – Maintains conversation context **within a session** using **LangChain ConversationBufferMemory**.  
✅ **FastAPI Backend** – Efficient API to handle user queries and file uploads.  
✅ **User-Friendly Streamlit UI** – A simple web interface for seamless interaction.  

---

## **📌 Installation**  

### **1️⃣ Clone the Repository**  
```sh
git clone https://github.com/YOUR_GITHUB_USERNAME/YOUR_REPO_NAME.git
cd YOUR_REPO_NAME
```

### **2️⃣ Create & Activate Virtual Environment**  
```sh
python -m venv venv
# Activate it
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate
```

### **3️⃣ Install Dependencies**  
```sh
pip install -r requirements.txt
```

### **4️⃣ Set Up Environment Variables**  
Create a `.env` file and add:  
```ini
GROQ_API_KEY=your_api_key_here
```

---

## **🚀 Usage**  

### **1️⃣ Start the FastAPI Backend**  
```sh
uvicorn main:app --reload
```
Backend will run at: **`http://127.0.0.1:8000/`**  

### **2️⃣ Run the Streamlit Frontend**  
```sh
streamlit run app.py
```
It will open the **LexiGen Web UI** in your browser.  

---

## **🛠️ Tech Stack**  
- **Python**  
- **FastAPI** (Backend)  
- **Streamlit** (Frontend)  
- **Groq API** (LLaMA3 Model)  
- **Tesseract OCR** (Image Processing)  
- **pdfplumber** (PDF Processing)  
- **LangChain** (**ConversationBufferMemory** for maintaining chat context)  

---

### 🎉 Enjoy Using LexiGen! 🚀



## 🤖 API Endpoints  
| Method | Endpoint  | Description |
|--------|----------|-------------|
| `GET`  | `/`      | Check if server is running |
| `POST` | `/query` | Process query with optional **text, image, or PDF** |


---

### 🎉 Enjoy Using LexiGen! 🚀  

## Output
![Home Page](https://github.com/Bahugun0042/LexiGen/blob/8d35f8ad0520bdb558171d8d4194bb579461f3e4/Screenshot%20(10).png)
![Home Page](https://github.com/Bahugun0042/LexiGen/blob/8d35f8ad0520bdb558171d8d4194bb579461f3e4/Screenshot%20(13).png)
![Home Page](https://github.com/Bahugun0042/LexiGen/blob/8d35f8ad0520bdb558171d8d4194bb579461f3e4/Screenshot%20(14).png)


