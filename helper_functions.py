# helper_functions.py

import docx
from googletrans import Translator

from PyPDF2 import PdfReader  # Import the new PdfReader class




def detect_file_type(uploaded_file):
    if uploaded_file.name.lower().endswith('.pdf'):
        return 'pdf'
    elif uploaded_file.name.lower().endswith('.docx'):
        return 'docx'
    else:
        raise ValueError("Unsupported file type")


def extract_text(uploaded_file, file_type):
    text = ""
    if file_type == 'pdf':
        # For PDF, use the PdfReader class
        reader = PdfReader(uploaded_file)
        for page in reader.pages:
            text += page.extract_text()
    elif file_type == 'docx':
        # For docx, use the uploaded file as a file-like object
        doc = docx.Document(uploaded_file)
        for para in doc.paragraphs:
            text += para.text + '\n'
    return text



def translate_paragraphs(paragraphs, dest_language):
    translator = Translator()
    translated_paragraphs = []
    for paragraph in paragraphs:
        if len(paragraph.strip()) > 0:
            translation = translator.translate(paragraph, dest=dest_language)
            translated_paragraphs.append(translation.text)
    return translated_paragraphs
