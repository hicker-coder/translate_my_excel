# helper_functions.py

import docx
import pandas as pd
from googletrans import Translator
from PyPDF2 import PdfReader

def detect_file_type(uploaded_file):
    if uploaded_file.name.lower().endswith('.pdf'):
        return 'pdf'
    elif uploaded_file.name.lower().endswith('.docx'):
        return 'docx'
    elif uploaded_file.name.lower().endswith(('.xlsx', '.xls')):  # Add support for Excel files
        return 'xlsx'
    else:
        raise ValueError("Unsupported file type")

def extract_text(uploaded_file, file_type):
    text = ""
    if file_type == 'pdf':
        reader = PdfReader(uploaded_file)
        for page in reader.pages:
            text += page.extract_text()
    elif file_type == 'docx':
        doc = docx.Document(uploaded_file)
        for para in doc.paragraphs:
            text += para.text + '\n'
    elif file_type == 'xlsx':  # Handle Excel files
        # Implement logic to extract text from Excel rows
        df = pd.read_excel(uploaded_file)
        text = "\n".join(" ".join(str(cell) for cell in row) for _, row in df.iterrows())
    return text

def translate_paragraphs(paragraphs, dest_language):
    translator = Translator()
    translated_paragraphs = []
    for paragraph in paragraphs:
        if len(paragraph.strip()) > 0:
            translation = translator.translate(paragraph, dest=dest_language)
            translated_paragraphs.append(translation.text)
    return translated_paragraphs

def translate_excel_columns(df, dest_language):
    translator = Translator()
    translated_df = df.copy()

    for column in df.columns:
        translated_df[column + '_translated'] = df[column].apply(lambda x: translator.translate(str(x), dest=dest_language).text)

    return translated_df
