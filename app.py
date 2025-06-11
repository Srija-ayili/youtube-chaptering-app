import streamlit as st
import nltk
import os
from chaptering_model import split_text_into_chapters

# Setup NLTK data path for deployment
nltk_data_dir = os.path.join(os.path.expanduser("~"), "nltk_data")
nltk.data.path.append(nltk_data_dir)

st.set_page_config(page_title="Transcript Chaptering App", layout="wide")
st.title("📄 Upload Transcript to Generate Chapters")

uploaded_file = st.file_uploader("Upload a transcript file (.txt)", type="txt")

if uploaded_file is not None:
    transcript_text = uploaded_file.read().decode("utf-8")

    if st.button("Generate Chapters"):
        with st.spinner("Processing transcript..."):
            chapters = split_text_into_chapters(transcript_text, max_words=100)

        st.success("Chapters Generated Successfully!")
        st.markdown("### 📌 Chapters")
        for i, chapter in enumerate(chapters):
            st.markdown(f"○ **Part {i+1}** {chapter}")
