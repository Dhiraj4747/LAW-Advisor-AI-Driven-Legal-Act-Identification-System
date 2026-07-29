# ⚖️ LawGPT – LLM Based Legal Advisory Chatbot

![Python](https://img.shields.io/badge/Python-3.12-brightgreen)
![LLM](https://img.shields.io/badge/LLM-LLaMA--7B-blue)
![VectorDB](https://img.shields.io/badge/VectorDB-FAISS-orange)

LawGPT is an AI-powered legal advisory chatbot designed to provide accurate and context-aware legal information. The system follows a Retrieval-Augmented Generation (RAG) architecture and leverages Large Language Models (LLMs) along with vector embeddings to retrieve and generate relevant legal responses from a legal document corpus. This project primarily focuses on Indian legal documents, including the Indian Penal Code (IPC).

---

## 📑 Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [System Architecture](#system-architecture)
- [Project Structure](#project-structure)
- [Technologies Used](#technologies-used)
- [Setup and Installation](#setup-and-installation)
- [Usage](#usage)
- [Future Enhancements](#future-enhancements)

---

## 📌 Introduction
LawGPT aims to assist users by delivering reliable and concise legal information through natural language queries. By combining semantic search with generative AI, the system retrieves the most relevant legal context from stored documents and generates meaningful responses for user queries.

---

## 🚀 Features
- Conversational interface for legal queries  
- Retrieval-Augmented Generation (RAG) architecture  
- Efficient semantic search using FAISS  
- Legal document embeddings using Google Generative AI  
- Handles large legal document sets through chunking and batching  
- Provides source-aware responses  
- Maintains conversational context using memory  

---

## 🏗️ System Architecture
The LawGPT system follows a modular layered architecture designed for scalability and maintainability.

### Architecture Components
1. **Frontend Interface**
   - Web-based UI for submitting legal queries and viewing responses

2. **Document Loader**
   - Loads legal documents from a directory of PDF files

3. **Text Splitter**
   - Splits extracted text into manageable chunks for embedding

4. **Embeddings**
   - Converts text into vector representations using Google Generative AI Embeddings

5. **Vector Store (FAISS)**
   - Stores and retrieves document embeddings efficiently

6. **LLM Processor (LLaMA-7B via ChatGroq)**
   - Generates responses based on retrieved legal context

7. **Memory Module**
   - Maintains conversation history for contextual continuity

---

## 🗂️ Project Structure
LawGPT/
│
├── backend/
│ ├── app.py
│ ├── document_loader.py
│ ├── text_splitter.py
│ ├── embeddings.py
│ ├── vector_store.py
│ ├── llm_processor.py
│ └── memory.py
│
├── data/
│ └── legal_documents/
│
├── requirements.txt
├── README.md
└── .env

---

## 🧠 Technologies Used
- **Programming Language:** Python 3.12  
- **LLM:** LLaMA-7B (via ChatGroq API)  
- **Embeddings:** Google Generative AI Embeddings  
- **Vector Database:** FAISS  
- **Frameworks:** LangChain, Flask  
- **NLP:** spaCy  

---

## ⚙️ Setup and Installation
```bash
git clone https://github.com/your-username/LawGPT.git
cd LawGPT
pip install -r requirements.txt
python backend/app.py


---



