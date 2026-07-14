# Visionerds Internship – Week 2 Day 7

## Topic
Document Chunking for RAG

## Objective
Extract text from a PDF and split it into overlapping chunks for Retrieval-Augmented Generation (RAG).

## What I Implemented

- Loaded a PDF using PyPDF.
- Extracted text from all pages.
- Counted the total number of words.
- Built a custom chunking algorithm without using external chunking libraries.
- Split the document into 400-word chunks with a 100-word overlap.
- Printed chunk statistics and verified that overlap was preserved.
- Saved all generated chunks into `chunks.txt` for future retrieval tasks.

## Technologies Used

- Python
- PyPDF
- VS Code

## Output

- PDF Pages: 6
- Total Words: 1612
- Total Chunks: 6
- Chunk Size: 400 words
- Overlap: 100 words

## Learning Outcome

Learned how document chunking works and why overlapping chunks help preserve context in Retrieval-Augmented Generation (RAG) systems.