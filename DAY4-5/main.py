import time
from colorama import Fore, init
from pypdf import PdfReader

from chunker import create_chunks
from vector_store import VectorStore
from llm import LLM
from context_builder import build_context

init(autoreset=True)

start = time.time()

print(Fore.CYAN + "=" * 60)
print(Fore.CYAN + " Visionerds Internship - Week 2 (Day 9 & Day 10)")
print(Fore.CYAN + "=" * 60)

# -------------------------------------------------------
# Load PDF
# -------------------------------------------------------

print(Fore.YELLOW + "\nLoading PDF...")

reader = PdfReader("sample.pdf")

print(Fore.GREEN + "PDF Loaded Successfully!")

text = ""

for page in reader.pages:
    extracted = page.extract_text()

    if extracted:
        text += extracted + "\n"

print(Fore.GREEN + "Text Extracted Successfully!")

# -------------------------------------------------------
# Chunking
# -------------------------------------------------------

print(Fore.YELLOW + "\nCreating Chunks...")

chunks = create_chunks(
    text,
    chunk_size=250,
    overlap=50
)

print(Fore.GREEN + f"{len(chunks)} chunks created.")

# -------------------------------------------------------
# Vector Store
# -------------------------------------------------------

print(Fore.YELLOW + "\nInitializing Vector Store...")

store = VectorStore()
store.add_chunks(chunks)

print(Fore.CYAN + "\nDatabase Statistics")
print(Fore.CYAN + "-" * 30)
print(Fore.GREEN + f"Stored Documents : {store.collection.count()}")

print(Fore.GREEN + "\nVector Database Ready!")

# -------------------------------------------------------
# LLM
# -------------------------------------------------------

print(Fore.YELLOW + "\nInitializing LLM...")

llm = LLM()

print(Fore.GREEN + "LLM Ready!")

# -------------------------------------------------------
# Chat Loop
# -------------------------------------------------------

print(Fore.CYAN + "\n" + "=" * 60)
print(Fore.CYAN + " AI Document Assistant")
print(Fore.CYAN + "=" * 60)

while True:

    query = input(
        Fore.MAGENTA + "\nAsk a question (type EXIT to quit): "
    ).strip()

    if query.upper() == "EXIT":
        print(Fore.YELLOW + "\nThank you for using the AI Document Assistant!")
        break

    if not query:
        print(Fore.RED + "Please enter a valid question.")
        continue

    # -------------------------------------------------------
    # Retrieval
    # -------------------------------------------------------

    retrieval_start = time.time()

    results = store.search(query)

    retrieval_end = time.time()

    documents = results["documents"][0]
    distances = results["distances"][0]
    ids = results["ids"][0]

    # Reject unrelated questions
    if distances[0] > 0.65:

        print(Fore.RED + "\nI couldn't find relevant information in this document.")
        print(Fore.YELLOW + "Please ask a question related to the uploaded PDF.")

        print(
            Fore.GREEN
            + f"\nRetrieval Time : {retrieval_end-retrieval_start:.3f} sec"
        )

        continue

    # -------------------------------------------------------
    # Context Building
    # -------------------------------------------------------

    print(Fore.YELLOW + "\nBuilding Context...")

    context, source_info = build_context(
        documents,
        ids,
        distances
    )

    # -------------------------------------------------------
    # LLM
    # -------------------------------------------------------

    print(Fore.YELLOW + "Generating AI Response...")

    llm_start = time.time()

    answer = llm.ask(
        context=context,
        question=query
    )

    llm_end = time.time()

    # -------------------------------------------------------
    # Output
    # -------------------------------------------------------

    print(Fore.CYAN + "\n" + "=" * 60)
    print(Fore.GREEN + "AI Answer")
    print(Fore.CYAN + "=" * 60)

    print(answer)

    # -------------------------------------------------------
    # Sources
    # -------------------------------------------------------

    print(Fore.CYAN + "\n" + "=" * 60)
    print(Fore.GREEN + "Retrieved Sources")
    print(Fore.CYAN + "=" * 60)

    for source in source_info:

        print(
            Fore.YELLOW
            + f"{source['chunk_id']} | Relevance: {source['relevance']:.1f}%"
        )

    # -------------------------------------------------------
    # Confidence
    # -------------------------------------------------------

    confidence = max(0, (1 - distances[0]) * 100)

    print(Fore.CYAN + "\n" + "=" * 60)
    print(Fore.GREEN + f"Confidence Score : {confidence:.1f}%")
    print(Fore.GREEN + f"Retrieval Time   : {retrieval_end - retrieval_start:.3f} sec")
    print(Fore.GREEN + f"LLM Response Time: {llm_end - llm_start:.3f} sec")
    print(Fore.CYAN + "=" * 60)

end = time.time()

print(Fore.CYAN + "\n" + "=" * 60)
print(Fore.GREEN + f"Total Session Time : {end-start:.2f} sec")
print(Fore.CYAN + "=" * 60)
