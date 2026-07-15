import time
from colorama import Fore, init
from pypdf import PdfReader

from chunker import create_chunks
from vector_store import VectorStore

init(autoreset=True)

start = time.time()

print(Fore.CYAN + "=" * 60)
print(Fore.CYAN + " Visionerds Internship - Week 2 Day 8")
print(Fore.CYAN + "=" * 60)

# -----------------------------
# Load PDF
# -----------------------------

print(Fore.YELLOW + "\nLoading PDF...")

reader = PdfReader("sample.pdf")

print(Fore.GREEN + "PDF Loaded Successfully!")

text = ""

for page in reader.pages:
    extracted = page.extract_text()

    if extracted:
        text += extracted + "\n"

print(Fore.GREEN + "Text Extracted Successfully!")

# -----------------------------
# Chunking
# -----------------------------

print(Fore.YELLOW + "\nCreating Chunks...")

chunks = create_chunks(
    text,
    chunk_size=250,
    overlap=50
)

print(Fore.GREEN + f"{len(chunks)} chunks created.")

# -----------------------------
# Vector Store
# -----------------------------

print(Fore.YELLOW + "\nInitializing Vector Store...")

store = VectorStore()

store.add_chunks(chunks)

print(Fore.CYAN + "\nDatabase Statistics")
print(Fore.CYAN + "-" * 30)
print(Fore.GREEN + f"Stored Documents : {store.collection.count()}")

print(Fore.GREEN + "\nVector Database Ready!")

# -----------------------------
# Semantic Search
# -----------------------------

print(Fore.CYAN + "\n" + "=" * 60)
print(Fore.CYAN + " Semantic Search")
print(Fore.CYAN + "=" * 60)

while True:

    query = input(
        Fore.MAGENTA + "\nEnter your question (type EXIT to quit): "
    ).strip()

    if query.upper() == "EXIT":
        print(Fore.YELLOW + "\nThank you for using the Semantic Search System!")
        print(Fore.GREEN + "Goodbye!\n")
        break

    if not query:
        print(Fore.RED + "\nPlease enter a valid question.")
        continue

    search_start = time.time()

    results = store.search(query)

    search_end = time.time()

    documents = results["documents"][0]
    distances = results["distances"][0]
    ids = results["ids"][0]

    # Reject unrelated questions
    if distances[0] > 0.65:

        print(Fore.RED + "\nNo relevant information found in the document.")
        print(Fore.YELLOW + "Try asking a question related to the uploaded PDF.")

        print(Fore.CYAN + "\n" + "=" * 60)
        print(Fore.GREEN + f"Retrieval Time : {search_end-search_start:.3f} sec")
        print(Fore.CYAN + "=" * 60)

        continue

    print(Fore.CYAN + "\nTop Matching Chunks")

    for i, (doc, distance, chunk_id) in enumerate(
            zip(documents, distances, ids), start=1):

        relevance = (1 - distance) * 100

        print(Fore.CYAN + "\n" + "=" * 60)
        print(Fore.GREEN + f"Top Match #{i}")
        print(Fore.CYAN + "=" * 60)

        print(Fore.YELLOW + f"Chunk ID : {chunk_id}")
        print(Fore.YELLOW + f"Relevance : {relevance:.1f}%")
        print(Fore.YELLOW + f"Cosine Distance : {distance:.4f}\n")

        preview = doc[:400]

        if len(doc) > 400:
            preview += "..."

        print(preview)

    print(Fore.CYAN + "\n" + "=" * 60)
    print(Fore.GREEN + f"Retrieval Time : {search_end-search_start:.3f} sec")
    print(Fore.CYAN + "=" * 60)

    print(Fore.GREEN + "\nSearch completed successfully!")
    print(Fore.GREEN + f"Retrieved Top {len(documents)} most relevant chunks.")

end = time.time()

print(Fore.CYAN + "\n" + "=" * 60)
print(Fore.GREEN + f"Total Session Time : {end-start:.2f} sec")
print(Fore.CYAN + "=" * 60)

