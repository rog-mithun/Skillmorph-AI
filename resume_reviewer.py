import fitz  # PyMuPDF
import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel("models/gemini-1.5-pro")

def extract_resume_text(file):
    with fitz.open(stream=file.read(), filetype="pdf") as doc:
        text = ""
        for page in doc:
            text += page.get_text()
        return text

def review_resume(text):
    prompt = f"""
    You are a resume coach for tech professionals.
    
    Review the following resume content:
    \"\"\"{text}\"\"\"

    Provide feedback on:
    - Formatting and structure
    - Technical clarity and impact
    - Grammar and phrasing
    - Suggestions for improvement

    Be concise, structured, and helpful.
    """
    response = model.generate_content(prompt)
    return response.text
