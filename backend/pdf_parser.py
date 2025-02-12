import pdfplumber

def extract_text_from_pdf(file_obj):
    """Extract text from PDF file."""
    try:
        with pdfplumber.open(file_obj) as pdf:
            text = "\n".join(page.extract_text() for page in pdf.pages if page.extract_text())
        return text.strip()
    except Exception as e:
        return f"Error extracting text: {str(e)}"
