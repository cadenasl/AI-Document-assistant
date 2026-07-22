# AI Document Assistant

> **⚠️ Work in Progress**
>
> This project is currently under active development as part of my portfolio while I prepare for AI Engineer roles. New features, improvements, and architectural refinements are being added regularly.

## Overview

AI Document Assistant is a Retrieval-Augmented Generation (RAG) application that allows users to upload PDF documents, index them into a vector database, and interact with them using a locally hosted Large Language Model.

The goal of this project is to demonstrate practical AI engineering skills including:

- Document parsing
- Text chunking
- Embedding generation
- Vector databases
- Semantic search
- Retrieval-Augmented Generation (RAG)
- Local LLM inference
- FastAPI backend development

---

# Current Features

- Upload PDF documents
- Extract text using PyMuPDF
- Chunk documents using RecursiveCharacterTextSplitter
- Generate embeddings
- Store embeddings in ChromaDB
- Semantic search over document content
- Ask questions about uploaded documents
- Generate AI-powered document summaries
- Run entirely locally using Ollama (no external API required)

---

# Architecture

```text
PDF Upload
    │
    ▼
PyMuPDF
    │
    ▼
Chunker
    │
    ▼
Embedding Model
    │
    ▼
ChromaDB
    │
    ▼
Semantic Search
    │
    ▼
Ollama (Llama 3.2)
    │
    ▼
Answer / Summary
```

---

# Technology Stack

- Python
- FastAPI
- PyMuPDF
- LangChain Text Splitters
- ChromaDB
- Ollama
- Llama 3.2
- aiofiles

---

# Design Decisions

### PyMuPDF

Chosen for fast and reliable PDF text extraction with access to document metadata.

### RecursiveCharacterTextSplitter

Used to preserve paragraph structure while creating chunks suitable for semantic retrieval.

### ChromaDB

Selected as a lightweight local vector database that requires minimal setup while providing fast similarity search.

### Ollama

Runs the language model locally, eliminating API costs and allowing the entire application to work offline.

### FastAPI

Provides a modern, modular REST API with automatic OpenAPI documentation.

---

# Current API

| Endpoint        | Description                 |
| --------------- | --------------------------- |
| POST /upload    | Upload a PDF document       |
| POST /ask       | Ask questions using RAG     |
| POST /summarize | Generate a document summary |

---

# Project Structure

```text
services/
│
├── ai/
│   ├── ollama_service.py
│   └── prompts.py
│
├── documents/
│   ├── parser.py
│   ├── chunker.py
│   ├── analyzer.py
│   └── upload_service.py
│
└── embeddings/
    ├── embedding_service.py
    └── vector_store.py

routes/
├── upload.py
├── ask.py
└── summarize.py
```

---

# Planned Improvements

This project is actively evolving. Planned features include:

- Document management endpoints
- Multiple PDF upload support
- Metadata storage
- Source citations with page numbers
- Hybrid search (keyword + vector)
- Retrieval evaluation metrics
- Streaming responses
- Docker deployment
- Authentication
- Automated testing
- CI/CD pipeline
- Performance benchmarking

---

# Why I Built This

The purpose of this project is to gain hands-on experience building production-style AI systems rather than simple LLM demos.

It focuses on concepts commonly used in modern AI applications:

- Retrieval-Augmented Generation (RAG)
- Embedding pipelines
- Vector databases
- Local LLM deployment
- Backend API architecture
- Modular software design

As I continue developing this project, I plan to improve retrieval quality, scalability, evaluation, and overall system architecture.

---

# Feedback

I'm continuously improving this project and welcome feedback on the implementation, architecture, and best practices.

Thanks for taking the time to check it out!
