# PDF-Insight: 📑 AI PDF Highlight Summarizer

## DEMO LINK: https://pdf-insight.streamlit.app/

## 🚀 Overview
This project extracts **highlighted text** from a PDF and generates a **concise summary** using **Mistral-7B** from Hugging Face. Built with **Streamlit**, it provides an easy-to-use interface for document analysis.

## 🔥 Features
- 📂 **Upload PDF** and extract only the **highlighted text**
- 🤖 **Summarize** extracted highlights using **Mistral-7B**
- 🔑 Requires **Hugging Face API key** for Mistral-7B access
- ⚡ **Multi-user support** using `st.session_state`
- 🎨 **Streamlit UI** for an interactive experience

## 🛠 Installation
### **Using Poetry**
```bash
# Clone the repository
git clone https://github.com/ShubhamMandowara/PDF-Insight.git
cd PDF-Insight

# Install dependencies using Poetry
poetry install

# Activate virtual environment
poetry shell

# Run the Streamlit app
streamlit run app.py
```

### **Using pip**
```bash
pip install -r requirements.txt
streamlit run app.py
```

## 📝 Usage
1. **Enter your Hugging Face API Key** in the sidebar
2. **Upload a PDF** containing highlighted text
3. **View extracted highlights**
4. **Click "Summarize Highlights"** to generate an AI-powered summary

## 📦 Requirements
- Python 3.8+
- Streamlit
- PyMuPDF (`pymupdf`)
- LangChain
- Hugging Face Hub
- langchain_community

## 📜 Example Output
```plaintext
**Extracted Highlights:**
1. "Artificial Intelligence is transforming industries."
2. "Mistral-7B is a powerful open-weight LLM."

**Generated Summary:**
AI is revolutionizing various sectors, and Mistral-7B is a strong model in the field.
```
