# main.py

import streamlit as st
import io
import pandas as pd
from helper_functions import detect_file_type, extract_text, translate_paragraphs, translate_excel_columns
from constants import SUPPORTED_FILE_TYPES, MAX_PARAGRAPH_LENGTH
from googletrans import LANGUAGES

# Customizing the page layout and color theme
st.set_page_config(page_title="Infomineo Translator Tool", layout="wide")

def main():
    # Custom CSS for a futuristic look with green, grey, and blue colors
    st.markdown("""
        <style>
        .st-bv {
            color: #29A19C; /* Primary Text Color - Green */
        }
        .st-bw {
            color: #17A589; /* Secondary Text Color - Darker Green */
        }
        header .css-1595djx {
            background-color: #1C2833; /* Header Background - Dark Grey */
        }
        .css-1d391kg {
            background-color: #17202A; /* Main Background - Darker Grey */
        }
        .st-ae {
            color: #3498DB; /* Widget Text Color - Blue */
        }
        .stButton>button {
            color: #FFFFFF;
            background-color: #29A19C; /* Button Color - Green */
            border: none;
            border-radius: 4px;
            padding: 10px 24px;
        }
        .st-bq {
            background-color: #2C3E50; /* Sidebar Background - Blue Grey */
        }
        </style>
        """, unsafe_allow_html=True)

    st.title("Infomineo Excel Translator")

    # File uploader
    uploaded_file = st.file_uploader("Upload a PDF, Word, or Excel document", type=SUPPORTED_FILE_TYPES)  # Update file types

    if uploaded_file is not None:
        file_type = detect_file_type(uploaded_file)

        if file_type in ['pdf', 'docx']:
            text = extract_text(uploaded_file, file_type)
            paragraphs = text.split('\n')
            paragraphs = [para[:MAX_PARAGRAPH_LENGTH] for para in paragraphs]

            dest_language = st.selectbox("Select Destination Language", list(LANGUAGES.values()))

            if st.button("Translate"):
                with st.spinner('Translating...'):
                    translated_text = ""
                    for paragraph in paragraphs:
                        if paragraph.strip():
                            translated_paragraphs = translate_paragraphs([paragraph], dest_language)
                            if translated_paragraphs:
                                translated_text += translated_paragraphs[0] + "\n"
                            else:
                                translated_text += "\n"
                        else:
                            translated_text += "\n"

                    translated_bytes = translated_text.encode('utf-8')

                    st.download_button(
                        label="Download Translated Text",
                        data=translated_bytes,
                        file_name="translated_text.txt",
                        mime="text/plain"
                    )
        elif file_type in ['xlsx', 'xls']:  # Handle Excel files
            # Load the Excel file
            df = pd.read_excel(uploaded_file)

            dest_language = st.selectbox("Select Destination Language", list(LANGUAGES.values()))

            if st.button("Translate"):
                with st.spinner('Translating...'):
                    translated_df = translate_excel_columns(df, dest_language)

                    # Create a download link for the translated Excel file
                    translated_excel_bytes = io.BytesIO()
                    with pd.ExcelWriter(translated_excel_bytes, engine='xlsxwriter') as writer:
                        translated_df.to_excel(writer, index=False)
                    st.download_button(
                        label="Download Translated Excel",
                        data=translated_excel_bytes.getvalue(),
                        file_name="translated_excel.xlsx",
                        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                    )

if __name__ == "__main__":
    main()
