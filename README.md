# 🚀 LexiGen: Multimodal Query Processor  

LexiGen is a **multimodal AI-powered query processor** that can process **text, images (photos), and PDFs** to provide intelligent responses using the **Groq API**.  

## 🔥 Features  
👉 Accepts **text queries**  
👉 Processes **images (OCR)** to extract text  
👉 Reads **PDFs** and extracts meaningful text  
👉 Uses **Groq API (LLaMA3-8B)** for AI responses  
👉 Simple **FastAPI** backend  
👉 User-friendly **Streamlit** UI  

## 📌 Installation  

### 1️⃣ Clone the Repository  
```sh
git clone https://github.com/YOUR_GITHUB_USERNAME/YOUR_REPO_NAME.git
cd YOUR_REPO_NAME
```

### 2️⃣ Create & Activate Virtual Environment  
```sh
python -m venv venv
# Activate it
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate
```

### 3️⃣ Install Dependencies  
```sh
pip install -r requirements.txt
```

### 4️⃣ Set Up Environment Variables  
Create a `.env` file and add:  
```ini
GROQ_API_KEY=your_api_key_here
```

## 🚀 Usage  

### 1️⃣ Start the FastAPI Backend  
```sh
uvicorn main:app --reload
```
It will run at: **`http://127.0.0.1:8000/`**  

### 2️⃣ Run the Streamlit Frontend  
```sh
streamlit run app.py
```
It will open the **LexiGen Web UI** in your browser.  

## 🛠️ Tech Stack  
- **Python**  
- **FastAPI** (Backend)  
- **Streamlit** (Frontend)  
- **Groq API** (LLaMA3 Model)  
- **Tesseract OCR** (Image Processing)  
- **pdfplumber** (PDF Processing)  

## 🤖 API Endpoints  
| Method | Endpoint  | Description |
|--------|----------|-------------|
| `GET`  | `/`      | Check if server is running |
| `POST` | `/query` | Process query with optional **text, image, or PDF** |

## 👨‍💻 Contributors  
- **Bahgun Sai Chapalamadugu**  

---

### 🎉 Enjoy Using LexiGen! 🚀  

## Output
![Home Page](https://github.com/Bahugun0042/LexiGen/blob/4d7289329cca54d6cca268ec38378dc97efc6499/output/Screenshot%20(204).png)
![Home Page](https://github.com/Bahugun0042/LexiGen/blob/4d7289329cca54d6cca268ec38378dc97efc6499/output/Screenshot%20(205).png)
![Home Page](https://github.com/Bahugun0042/LexiGen/blob/4d7289329cca54d6cca268ec38378dc97efc6499/output/Screenshot%20(206).png)
![Home Page](https://github.com/Bahugun0042/LexiGen/blob/4d7289329cca54d6cca268ec38378dc97efc6499/output/Screenshot%20(207).png)
![Home Page](https://github.com/Bahugun0042/LexiGen/blob/4d7289329cca54d6cca268ec38378dc97efc6499/output/Screenshot%20(209).png)
![Home Page](https://github.com/Bahugun0042/LexiGen/blob/4d7289329cca54d6cca268ec38378dc97efc6499/output/Screenshot%20(210).png)


