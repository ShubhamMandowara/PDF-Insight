import streamlit as st
import fitz  # PyMuPDF
from langchain.llms import HuggingFaceHub
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
import os

# Streamlit UI
st.title("📑 Highlighted Text Extractor with AI Summarization")
st.write("Upload a PDF, extract highlighted text, and get a summary using Mistral-7B!")

# Hugging Face API key input
hf_api_key = st.sidebar.text_input("🔑 Enter Hugging Face API Key", type="password")

if not hf_api_key:
    st.warning("⚠ Please enter your Hugging Face API key to proceed.")
    st.stop()
else:
    os.environ["HUGGINGFACEHUB_API_TOKEN"] = hf_api_key

# Initialize session state
if "highlighted_texts" not in st.session_state:
    st.session_state.highlighted_texts = []
if "summary" not in st.session_state:
    st.session_state.summary = None

# File uploader
uploaded_file = st.file_uploader("📂 Upload a PDF", type="pdf")

def extract_highlighted_text(pdf_path):
    """Extracts highlighted text from a given PDF."""
    doc = fitz.open(pdf_path)
    highlighted_texts = []

    for page in doc:
        for annot in page.annots():
            if annot.type[0] == 8:  # Highlight annotation type
                quad_points = annot.vertices  # Get coordinates
                if quad_points:
                    text = ""
                    for i in range(0, len(quad_points), 4):
                        rect = fitz.Quad(quad_points[i:i+4]).rect
                        text += page.get_text("text", clip=rect) + " "
                    highlighted_texts.append(text.strip())

    return highlighted_texts

# Load Mistral model from Hugging Face
llm = HuggingFaceHub(repo_id="mistralai/Mistral-7B-Instruct-v0.3", model_kwargs={"temperature": 0.5})

# Define summarization prompt
prompt = PromptTemplate(
    input_variables=["text"],
    template="Summarize the following highlighted points concisely:\n\n{text}\n\nSummary:"
)

qa_chain = LLMChain(llm=llm, prompt=prompt)

if uploaded_file:
    # Save uploaded file temporarily
    pdf_path = f"temp_{uploaded_file.name}"
    with open(pdf_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    # Extract highlighted text
    st.session_state.highlighted_texts = extract_highlighted_text(pdf_path)

    # Show extracted text
    if st.session_state.highlighted_texts:
        st.success("✅ Extracted highlighted text successfully!")
        for idx, text in enumerate(st.session_state.highlighted_texts, 1):
            st.write(f"**{idx}.** {text}")

        # Summarization button
        if st.button("📖 Summarize Highlights"):
            context = "\n".join(st.session_state.highlighted_texts)
            st.session_state.summary = qa_chain.run({"text": context})

    else:
        st.warning("⚠ No highlighted text found in the PDF.")

# Display summary
if st.session_state.summary:
    st.subheader("📌 AI-Generated Summary")
    st.write(st.session_state.summary)
