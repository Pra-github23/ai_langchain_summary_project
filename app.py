# ==========================================================
# AI TEXT / PDF / IMAGE SUMMARIZER
#
# Required packages:
# pip install streamlit
# pip install langchain
# pip install langchain_google_genai
# pip install pypdf
# pip install pillow
# pip install pytesseract
# pip install python-dotenv
#
# Create .env file:
# GOOGLE_API_KEY=hf_your_token_here
#
# Run:
# streamlit run app.py
# ==========================================================

import streamlit as st
from dotenv import load_dotenv
import os

from pypdf import PdfReader
from PIL import Image
import pytesseract

from langchain_google_genai import ChatGoogleGenerativeAI

# Load variables from .env file
load_dotenv()

# Tesseract OCR executable path
pytesseract.pytesseract.tesseract_cmd = (
    r"C:\Program Files\Tesseract-OCR\tesseract.exe"
)

# Load google model
# Change repo_id if model is unavailable
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=os.getenv("GOOGLE_API_KEY"),
    temperature=0
)

# Streamlit page settings
st.set_page_config(page_title="AI Summary App")

# App title
st.title("AI Text / PDF / Image Summarizer")

# App description
st.write("Upload text, PDF, or image and generate a summary")

# User selects input type
option = st.selectbox(
    "Choose Input Type",
    ["Text", "PDF", "Image"]
)

# Stores extracted content
content = ""

# ==========================================================
# TEXT INPUT
# ==========================================================
if option == "Text":

    content = st.text_area(
        "Enter Text"
    )

# ==========================================================
# PDF INPUT
# ==========================================================
elif option == "PDF":

    uploaded_pdf = st.file_uploader(
        "Upload PDF",
        type=["pdf"]
    )

    if uploaded_pdf:

        reader = PdfReader(uploaded_pdf)

        pdf_text = ""

        # Extract text from all PDF pages
        for page in reader.pages:

            text = page.extract_text()

            if text:
                pdf_text += text

        content = pdf_text

        st.success(
            "PDF text extracted successfully"
        )

# ==========================================================
# IMAGE INPUT
# ==========================================================
elif option == "Image":

    uploaded_image = st.file_uploader(
        "Upload Image",
        type=["png", "jpg", "jpeg"]
    )

    if uploaded_image:

        image = Image.open(uploaded_image)

        st.image(
            image,
            caption="Uploaded Image"
        )

        # OCR extraction
        extracted_text = pytesseract.image_to_string(
            image
        )

        content = extracted_text

        st.success(
            "Text extracted from image"
        )

# ==========================================================
# SUMMARY GENERATION
# ==========================================================
if st.button("Generate Summary"):

    if not content.strip():

        st.warning(
            "Please provide content"
        )

    else:

        prompt = f"""
                 Read the content and create a beginner-friendly summary.

                 Output format:

                   📌 Main Idea
                   - Explain the topic in 2-3 simple lines.

                   📖 Easy Summary
                   - Bullet points in very simple language.
                   - Explain difficult words.
                   - Use everyday examples.

                   🎯 Key Takeaway
                   - Mention the most important lesson in one sentence.

                   Content:
                   {content}
                """

        # Loading spinner
        with st.spinner(
            "Generating summary..."
        ):

            response = llm.invoke(
                prompt
            )

        # Display summary
        st.subheader(
            "Summary"
        )

        st.markdown(response.content)

        # Optional extracted content
        with st.expander(
            "View Extracted Content"
        ):

            st.write(
                content
            )