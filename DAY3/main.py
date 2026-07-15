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

# --------------------------------------------------
# Load PDF
# --------------------------------------------------

print(Fore.YELLOW + "\nLoading PDF...")

reader = PdfReader("sample.pdf")

print(Fore.GREEN + "PDF Loaded Successfully!")

text = ""

for page in reader.pages:

    extracted = page.extract_text()

    if extracted:
        text += extracted + "\n"

print(Fore.GREEN + "Text Extracted Successfully!")

# --------------------------------------------------
# Chunking
# --------------------------------------------------

print(Fore.YELLOW + "\nCreating Chunks...")

chunks = create_chunks(
    text,
    chunk_size=250,
    overlap=50
)

print(Fore.GREEN + f"{len(chunks)} chunks created.")

# --------------------------------------------------
# Vector Store
# --------------------------------------------------

print(Fore.YELLOW + "\nInitializing Vector Store...")

store = VectorStore()

store.add_chunks(chunks)

print(Fore.YELLOW + "\nDatabase Statistics")
print("-" * 30)
print(Fore.WHITE + f"Stored Documents : {store.collection.count()}")

print(Fore.GREEN + "\nVector Database Ready!")

# --------------------------------------------------
# Semantic Search
# --------------------------------------------------

print(Fore.CYAN + "\n" + "=" * 60)
print(" Semantic Search")
print("=" * 60)

query = input(Fore.MAGENTA + "\nEnter your question: ")

search_start = time.time()

results = store.search(query)

search_end = time.time()

documents = results["documents"][0]
distances = results["distances"][0]
ids = results["ids"][0]

print(Fore.CYAN + "\nTop Matching Chunks")

for i, (doc, distance, chunk_id) in enumerate(
    zip(documents, distances, ids),
    start=1
):

    print("\n" + Fore.YELLOW + "=" * 60)
    print(Fore.GREEN + f"Top Match #{i}")
    print(Fore.YELLOW + "=" * 60)

    print(Fore.LIGHTBLUE_EX + f"Chunk ID : {chunk_id}")
    print(Fore.CYAN + f"Cosine Distance : {distance:.4f}\n")

    preview = doc.replace("\n", " ")

    if len(preview) > 350:
        preview = preview[:350] + "..."

    print(Fore.WHITE + preview)

end = time.time()

print(Fore.CYAN + "\n" + "=" * 60)
print(Fore.GREEN + f"Retrieval Time : {search_end - search_start:.3f} sec")
print(Fore.GREEN + f"Execution Time : {end - start:.2f} sec")
print(Fore.CYAN + "=" * 60)
print(Fore.YELLOW + "\nSearch completed successfully!")
print(Fore.YELLOW + f"Retrieved Top {len(documents)} most relevant chunks.")