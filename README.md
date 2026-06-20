# Document QA RAG Application

A Retrieval-Augmented Generation (RAG) based Question Answering application built using Flask, FAISS, Sentence Transformers, and Google Gemini. The application processes PDF documents, stores document embeddings in a vector database, retrieves relevant information using semantic search, and generates accurate answers based solely on the document content.

---

## 📌 Project Overview

This project implements a Question Answering (QA) system using the Retrieval-Augmented Generation (RAG) architecture.

The application:

* Loads and processes a PDF document
* Splits the document into meaningful chunks
* Generates embeddings for each chunk
* Stores embeddings in a FAISS vector database
* Retrieves relevant document content for a user query
* Uses Google Gemini to generate context-aware answers
* Exposes functionality through a Flask REST API

---

## 🚀 Features

* PDF document processing
* Text chunking and preprocessing
* Semantic search using embeddings
* FAISS vector database integration
* Context-aware answer generation
* Flask REST API
* Error handling for invalid inputs
* Modular and scalable architecture

---

## 🏗️ Project Structure

```text
RAG_Assignment/
│
├── app.py
├── ingest.py
├── rag.py
├── document.pdf
├── requirements.txt
│
└── vectorstore/
    ├── index.faiss
    └── index.pkl
```

---

## ⚙️ Technologies Used

### Backend

* Python
* Flask

### RAG Components

* LangChain
* FAISS
* Sentence Transformers
* HuggingFace Embeddings

### LLM

* Google Gemini

### Document Processing

* PyPDF

---

## 🔄 System Workflow

```text
PDF Document
      │
      ▼
Load PDF
      │
      ▼
Split into Chunks
      │
      ▼
Generate Embeddings
      │
      ▼
Store in FAISS
      │
      ▼
User Question
      │
      ▼
Question Embedding
      │
      ▼
Retrieve Relevant Chunks
      │
      ▼
Gemini LLM
      │
      ▼
Generate Answer
      │
      ▼
Return Response
```

---

## 📥 Installation

### 1. Clone Repository

```bash
git clone https://github.com/your-username/Document-QA-RAG-Application.git

cd Document-QA-RAG-Application
```

### 2. Create Virtual Environment

```bash
python -m venv venv
```

Activate Virtual Environment:

#### Windows

```bash
venv\Scripts\activate
```

#### Linux/Mac

```bash
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Configure Gemini API Key

Create a `.env` file:

```env
GEMINI_API_KEY=YOUR_API_KEY
```

Alternatively, directly configure the key inside `rag.py`.

---

## 📄 Document Processing

Place your PDF document in the project root directory:

```text
document.pdf
```

Run:

```bash
python ingest.py
```

This will:

* Load the PDF
* Split text into chunks
* Generate embeddings
* Create FAISS vector database
* Save vector store locally

Output:

```text
PDF Loaded
Chunks Created: XX
Vector Database Saved
```

---

## ▶️ Run Application

Start Flask server:

```bash
python app.py
```

Server will run on:

```text
http://127.0.0.1:5000
```

---

## 📡 API Endpoint

### Ask Question

**Endpoint**

```http
POST /ask
```

### Request Body

```json
{
  "question": "What is business communication?"
}
```

### Success Response

```json
{
  "answer": "Business communication is the flow of information within and outside a business organization."
}
```

### Error Response

```json
{
  "error": "Question cannot be empty"
}
```

---

## 🧪 Sample Questions

```json
{
  "question": "What is business communication?"
}
```

```json
{
  "question": "What are the objectives of communication?"
}
```

```json
{
  "question": "What are barriers to communication?"
}
```

```json
{
  "question": "What is verbal communication?"
}
```

```json
{
  "question": "What is non-verbal communication?"
}
```

---

## 🛡️ Out-of-Scope Questions

If the answer is not present in the document, the application returns:

```text
The answer is not available in the provided document.
```

Example:

```json
{
  "question": "Who is the CEO of Google?"
}
```

Response:

```json
{
  "answer": "The answer is not available in the provided document."
}
```

---

## 📚 RAG Components

### Document Loader

Loads PDF content using PyPDFLoader.

### Text Splitter

Splits document into smaller chunks for efficient retrieval.

### Embedding Model

Uses:

```text
sentence-transformers/all-MiniLM-L6-v2
```

to convert text into vector embeddings.

### Vector Database

FAISS stores document embeddings and performs similarity search.

### Retriever

Finds the most relevant chunks related to a user query.

### LLM

Google Gemini generates answers using only retrieved context.

---

## 📈 Future Enhancements

* Multi-document support
* Conversation memory
* Hybrid search (BM25 + Vector Search)
* Streamlit frontend
* Docker deployment
* Cloud vector databases (Pinecone, Weaviate)
* User authentication

---

## 📝 Assumptions

* Input document is a PDF file.
* Document language is English.
* FAISS is used as the vector database.
* Gemini is used as the Large Language Model.
* Top relevant chunks are retrieved for answer generation.
* Answers are generated only from retrieved document context.

---

## 👨‍💻 Author

**Aradhya Zalte**

B.Sc. Information Technology
Mumbai University

---

## 📄 License

This project is created for educational and interview assessment purposes.
