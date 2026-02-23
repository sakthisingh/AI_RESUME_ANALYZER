# utils.py

import pdfplumber
from docx import Document
import re
import nltk
from nltk.corpus import stopwords

nltk.download("stopwords")

def extract_text(file_path):

    if file_path.endswith(".pdf"):
        return extract_from_pdf(file_path)

    elif file_path.endswith(".docx"):
        return extract_from_docx(file_path)

    else:
        raise ValueError("Unsupported file format")

def extract_from_pdf(file_path):
    text = ""
    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            content = page.extract_text()
            if content:
                text += content
    return text

def extract_from_docx(file_path):
    doc = Document(file_path)
    text = ""
    for para in doc.paragraphs:
        text += para.text + "\n"
    return text

def clean_text(text):

    text = text.lower()
    text = re.sub(r"\W", " ", text)
    text = re.sub(r"\s+", " ", text)

    stop_words = set(stopwords.words("english"))
    words = text.split()
    words = [w for w in words if w not in stop_words]

    return " ".join(words)