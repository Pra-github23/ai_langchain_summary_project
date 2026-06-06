# 🚀 AI Text, PDF & Image Summarizer

An AI-powered application that generates concise summaries from **Text**, **PDF files**, and **Images**. The application extracts content from different input formats and uses a Large Language Model (LLM) to produce easy-to-read bullet-point summaries.

## ✨ Features

* 📝 Text Summarization
* 📄 PDF Summarization
* 🖼️ Image Text Extraction using OCR
* 🤖 AI-Powered Summaries
* 🌐 Simple and Interactive Streamlit Interface
* 🔐 Secure API Key Management using Environment Variables

---

## 🛠️ Technologies Used

### Python

Core programming language used to build the application and integrate all components.

### Streamlit

Used to create the web-based user interface.

Features:

* Text Input
* PDF Upload
* Image Upload
* Summary Display

### LangChain

Framework used to connect the application with AI models.

Responsibilities:

* Prompt Management
* AI Model Interaction
* Response Handling

### AI Models

Supports AI models such as:

* Google Gemini
* Hugging Face Models
* OpenAI Models

Used for:

* Understanding Content
* Generating Summaries

### PyPDF

Extracts text from uploaded PDF documents.

### Pillow (PIL)

Processes uploaded images before OCR extraction.

### Tesseract OCR

Converts image text into machine-readable text.

### Python-Dotenv

Loads API keys securely from environment variables.

---

## 🔄 Project Workflow

```text
User Input
(Text / PDF / Image)
          │
          ▼
Text Extraction
(PyPDF / Tesseract OCR)
          │
          ▼
LangChain
          │
          ▼
AI Model
(Gemini / Hugging Face / OpenAI)
          │
          ▼
Generate Summary
          │
          ▼
Display Result
(Streamlit)
```

---

## 📂 Project Structure

```text
ai_summary_project/
│
├── app.py
├── .env
├── requirements.txt
├── README.md
└── venv/
```

---

## ⚙️ Installation

### Clone Repository

```bash
git clone <your-repository-url>
cd ai_summary_project
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

Windows:

```bash
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file in the project root.

Example:

```env
GOOGLE_API_KEY=your_api_key
```

or

```env
HUGGINGFACE_API_KEY=your_api_key
```

---

## ▶️ Run Application

```bash
streamlit run app.py
```

Open your browser and visit:

```text
http://localhost:8501
```

---

## 🎯 Use Cases

* Summarizing Articles
* Summarizing Research Papers
* Extracting and Summarizing PDF Content
* Extracting Text from Images
* Quick Content Understanding
* Learning and Productivity Applications

---

## 📸 Supported Input Types

| Input Type           | Supported |
| -------------------- | --------- |
| Text                 | ✅         |
| PDF                  | ✅         |
| Image (PNG/JPG/JPEG) | ✅         |

---

## 🌟 Future Enhancements

* Text-to-Speech Summary
* Multi-Language Summaries
* Chat with PDF
* Audio File Summarization
* Export Summary to PDF
* RAG-based Document Question Answering

---

## 👨‍💻 Author

Developed as a hands-on AI project using Python, LangChain, Streamlit, OCR, and Large Language Models.
