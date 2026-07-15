# Visionerds Internship - Week 2 Day 8

## Objective
Build a semantic search system using sentence embeddings and ChromaDB.

## Features
- Read and extract text from a PDF document.
- Split the document into 250-word chunks with 50-word overlap.
- Generate embeddings using `all-MiniLM-L6-v2`.
- Store embeddings in a persistent ChromaDB vector database.
- Perform semantic search using user queries.
- Retrieve the Top-3 most relevant chunks with cosine distance.
- Display execution time, retrieval time, and database statistics.

## Technologies Used
- Python
- Sentence Transformers
- ChromaDB
- PyPDF
- Colorama

## Project Structure

```
DAY3/
│── main.py
│── vector_store.py
│── chunker.py
│── sample.pdf
│── README.md
│── requirements.txt
│── chroma_db/
```

## Sample Output

```
Loading PDF...
PDF Loaded Successfully!

Creating Chunks...
8 chunks created.

Initializing Vector Store...
Stored Documents : 8

Semantic Search

Question:
What is the total credit hours required for the BS Computer Science program?

Top Match #1
Cosine Distance : 0.3351
```

## Learning Outcomes
- Learned how embeddings represent text semantically.
- Implemented a vector database using ChromaDB.
- Performed semantic search using cosine similarity.
- Built the retrieval component of a Retrieval-Augmented Generation (RAG) pipeline.
