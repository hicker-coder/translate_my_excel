# main.py

import streamlit as st
import io
from helper_functions import detect_file_type, extract_text, translate_paragraphs
from constants import SUPPORTED_FILE_TYPES, MAX_PARAGRAPH_LENGTH
from googletrans import LANGUAGES

# Customizing the page layout and color theme
st.set_page_config(page_title="MEF-BD1 Translator", layout="wide")

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

    st.title("MEF-BD1 PDF/Word Translator")

    # File uploader
    uploaded_file = st.file_uploader("Upload a PDF or Word document", type=SUPPORTED_FILE_TYPES)

    if uploaded_file is not None:
        file_type = detect_file_type(uploaded_file)
        text = extract_text(uploaded_file, file_type)

        paragraphs = text.split('\n')
        paragraphs = [para[:MAX_PARAGRAPH_LENGTH] for para in paragraphs]

        dest_language = st.selectbox("Select Destination Language", list(LANGUAGES.values()))

        if st.button("Translate"):
            with st.spinner('Translating...'):
                translated_text = ""
                for paragraph in paragraphs:
                    if paragraph.strip():  # Check if paragraph is not just whitespace
                        translated_paragraphs = translate_paragraphs([paragraph], dest_language)
                        if translated_paragraphs:  # Check if translation result is not empty
                            translated_text += translated_paragraphs[0] + "\n"
                        else:
                            translated_text += "\n"  # Add an empty line if no translation
                    else:
                        translated_text += "\n"  # Add an empty line for empty paragraphs

                # Convert the translated text to bytes
                translated_bytes = translated_text.encode('utf-8')

                # Create a download button with the bytes
                st.download_button(
                    label="Download Translated Text",
                    data=translated_bytes,
                    file_name="translated_text.txt",
                    mime="text/plain"
                )

if __name__ == "__main__":
    main()
