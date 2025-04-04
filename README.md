# Plagiarism-Detection


# Code Plagiarism Detection System
This project is a Code Plagiarism Detection System designed to identify similar code snippets across repositories. It retrieves and indexes code, then uses FAISS, CodeBERT embeddings, and LLMs to assess whether a given code snippet is plagiarized.

The system follows a Retrieval-Augmented Generation (RAG) approach, where it first retrieves relevant code snippets and then evaluates plagiarism using an LLM. It provides two evaluation methods:

RAG-Based Evaluation – Uses vector similarity search to find similar code.

LLM-Based Evaluation – Leverages a language model to determine plagiarism likelihood.

Built with FastAPI, the system offers an API for checking code similarities, and it includes evaluation scripts to measure precision and recall. The project is containerized with Docker for easy deployment.

## Overview
This project is a **code plagiarism detection system** that:
- Clones and indexes code from GitHub repositories
- Uses **CodeBERT** to embed and compare code snippets
- Utilizes **FAISS** for fast similarity search
- Runs an **API with FastAPI** to check for plagiarism
- Supports evaluation

---

## Features
- **Automated Repository Cloning**: Fetches and processes GitHub repositories.
- **Multi-Language Support**: Detects and indexes different programming languages.
- **FAISS-based Code Retrieval**: Efficient similarity search for large datasets.
- **CodeBERT for Embeddings**: High-quality vector representations for code.
- **FastAPI Integration**: Provides an API endpoint for checking plagiarism.
- **LLM-Based Assessment**: Uses OpenAI to assess plagiarism.
- **Evaluation Metrics**: Supports precision and recall analysis.

---

##  Setup & Installation
### 1. Clone the Repository
```bash
 git clone https://github.com/your-username/your-repo.git
 cd your-repo
```

### 2. Install Dependencies (Locally)
Ensure you have **Python 3.8+** installed.
```bash
pip install -r requirements.txt
```

### 3. Run the API
```bash
uvicorn main:app --reload
```

### 4. Test the API
Once running, visit:
```
http://127.0.0.1:8000/docs
```

---

##  Running with Docker
###  1. Build and Run the Docker Container
```bash
docker build -t plagiarism-checker .
docker run -p 8000:8000 plagiarism-checker
```
###  2. Test the API in Docker
```
http://localhost:8000/docs
```

---

##  API Endpoints
###  **Check Plagiarism**
**Endpoint:**
```http
POST /check_plagiarism
```
**Request JSON:**
```json
{
  "code_snippet": "def add(a, b): return a + b"
}
```
**Response JSON:**
```json
{
  "plagiarism_status": "Yes",
  "similar_code": ["def sum(x, y): return x + y"]
}
```

---

## Evaluation
###  Run Retrieval Evaluation
```bash
python evaluate.py
```

### Run LLM Assessment
```bash
python llm_assessment.py
```

---

##  Project Structure
```
 your-repo/
├──  main.py  # FastAPI app with plagiarism detection
├──  embeddings_service.py  # Embedding & FAISS setup
├──  evaluate.py  # Retrieval evaluation script
├──  llm_assessment.py  # LLM-based evaluation
├──  Dockerfile  # Docker setup
├──  requirements.txt  # Dependencies
├──  repos/  # Cloned repositories (ignored in .gitignore)
```

---

---


