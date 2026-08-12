# 📄 DocuMind AI RAG

> A local AI-powered PDF question-answering assistant built with RAG, LangChain, FAISS, Hugging Face embeddings, Ollama, and Streamlit.

## ✨ Features

- 📄 Upload one or multiple PDF documents
- 🔎 Semantic document retrieval using FAISS
- 🧠 Hugging Face embeddings
- 🤖 Local LLM inference using Ollama
- 💬 Interactive Streamlit chat interface
- 📚 Relevant source page references
- 🚫 No sources shown when the answer isn't found
- 🔐 Local document processing
- 🎨 Clean document-focused UI

## 🏗️ Architecture

```text
PDF Document
     ↓
PyPDFLoader
     ↓
Text Splitting
     ↓
Hugging Face Embeddings
     ↓
FAISS Vector Database
     ↓
Retriever
     ↓
Relevant Chunks
     ↓
Ollama Local LLM
     ↓
Answer + Sources
```

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python 3.11.9 | Application development |
| Streamlit | Web interface |
| LangChain | RAG pipeline |
| PyPDFLoader | PDF processing |
| Hugging Face | Text embeddings |
| FAISS | Vector similarity search |
| Ollama | Local LLM inference |
| HTML/CSS | UI customization |

## 📂 Project Structure

```text
DocuMind-AI-RAG/
│
├── data/
│   └── Commonwealth.pdf
│
├── vectorstore/
│   ├── index.faiss
│   └── index.pkl
│
├── utils/
│   ├── embeddings.py
│   ├── helpers.py
│   ├── pdf_loader.py
│   ├── prompt.py
│   ├── rag_engine.py
│   ├── retriever.py
│   ├── memory.py
│   └── vectorstore.py
│
├── app.py
├── config.py
├── requirements.txt
└── README.md
```

> `.venv/` is used locally and should not be uploaded to GitHub.

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/RohithKumar-KM/DocuMind-AI-RAG
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

### 3. Activate the environment

**Windows:**

```bash
.venv\Scripts\activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

## 🤖 Ollama Setup

Install Ollama and pull the required model:

```bash
ollama pull llama3.2:3b
```

Verify the model:

```bash
ollama list
```

## ▶️ Run the Application

```bash
streamlit run app.py
```

The application will open in your browser.

## 💬 How It Works

1. Upload a PDF document.
2. The PDF is loaded and split into smaller chunks.
3. Hugging Face generates embeddings for the chunks.
4. FAISS stores the embeddings for similarity search.
5. The retriever finds relevant document chunks.
6. Ollama receives the retrieved context.
7. The local LLM generates the answer.
8. Relevant source pages are displayed when an answer is found.

## 🔐 Local AI Pipeline

```text
PDF
 ↓
Local Embeddings
 ↓
FAISS
 ↓
Retriever
 ↓
Ollama
 ↓
Local LLM
 ↓
Answer
```

DocuMind AI is designed to process documents locally without requiring a hosted LLM API for the question-answering pipeline.

## 🚀 Future Improvements

- 📚 Advanced document summarization
- 🧠 Conversation memory
- 📑 Multi-document comparison
- 🔍 Hybrid search
- 📊 Retrieval evaluation
- ⚡ Faster document indexing
- 🌐 Remote deployment

## 👨‍💻 Author

**Rohith Kumar K M**

Built as a practical project to explore:

**Retrieval-Augmented Generation (RAG) • Vector Databases • Semantic Search • Local LLMs • Prompt Engineering • PDF Processing • Streamlit**

---

⭐ If you find this project useful, consider giving the repository a star!
