import pytesseract
from PIL import Image
import io

# Make Tesseract Path Optional
TESSERACT_CMD = r"D:\projects\GENAI\tesseract.exe"

def extract_text_from_image(image_bytes):
    """Extract text from an image file."""
    try:
        if TESSERACT_CMD:
            pytesseract.pytesseract.tesseract_cmd = TESSERACT_CMD
            
        image = Image.open(io.BytesIO(image_bytes))
        text = pytesseract.image_to_string(image)
        return text.strip()
    except Exception as e:
        return f"Error extracting text: {str(e)}"
