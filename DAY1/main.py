from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
from colorama import Fore, Style, init
from tabulate import tabulate
import numpy as np
import os
import time

init(autoreset=True)

print("=" * 70)
print(Fore.CYAN + "Visionerds Internship - Week 2 Day 6")
print(Fore.CYAN + "Semantic Search Engine")
print("=" * 70)

#model loading


print(Fore.YELLOW + "\nLoading embedding model...")

model = SentenceTransformer("all-MiniLM-L6-v2")

print(Fore.GREEN + "Model Loaded Successfully!")

#sample sentences loading which i write in sentences.txt

with open("sentences.txt", "r", encoding="utf-8") as file:
    sentences = [line.strip() for line in file if line.strip()]

print(Fore.GREEN + f"\nLoaded {len(sentences)} Sentences")
#embeddings creations (vector for strings)
if os.path.exists("embeddings.npy"):

    print(Fore.YELLOW + "Loading Saved Embeddings...")

    embeddings = np.load("embeddings.npy")

else:

    print(Fore.YELLOW + "Generating Embeddings...")

    embeddings = model.encode(sentences)

    np.save("embeddings.npy", embeddings)

    print(Fore.GREEN + "Embeddings Saved Successfully!")

# similarity check that is cosine similarity


matrix = cosine_similarity(embeddings)

headers = [""] + [f"S{i+1}" for i in range(len(sentences))]

table = []

for i in range(len(sentences)):
    row = [f"S{i+1}"]

    for value in matrix[i]:
        row.append(f"{value:.2f}")

    table.append(row)

print("\n")
print(Fore.CYAN + "Similarity Matrix\n")

print(tabulate(table, headers=headers, tablefmt="grid"))

#score 

def confidence(score):

    if score >= 0.80:
        return "Very High"

    elif score >= 0.60:
        return "High"

    elif score >= 0.40:
        return "Medium"

    else:
        return "Low"

#searching

def semantic_search(query, top_k=3):

    query_embedding = model.encode([query])

    scores = cosine_similarity(
        query_embedding,
        embeddings
    )[0]

    indexes = scores.argsort()[::-1][:top_k]

    results = []

    for idx in indexes:

        results.append(
            (
                sentences[idx],
                scores[idx]
            )
        )

    return results



print("\n")
print(Fore.CYAN + "=" * 70)
print("Project Statistics")
print("=" * 70)

print(f"Model               : all-MiniLM-L6-v2")
print(f"Embedding Dimension : {len(embeddings[0])}")
print(f"Stored Sentences    : {len(sentences)}")
\

print("\n")
print(Fore.CYAN + "=" * 70)
print("Semantic Search Engine")
print("=" * 70)

while True:

    query = input(
        Fore.YELLOW +
        "\nEnter Query ('exit' to quit): "
    )

    if query.lower() == "exit":

        print(Fore.RED + "\nGood Bye!")

        break

    start = time.perf_counter()

    results = semantic_search(query)

    end = time.perf_counter()

    print("\n")

    print(Fore.GREEN + "Top Matches\n")

    for i, (sentence, score) in enumerate(results, start=1):

        bar = "█" * int(score * 20)

        print(Fore.CYAN + f"{i}. {sentence}")

        print(f"Similarity : {score:.3f}")

        print(f"Confidence : {confidence(score)}")

        print(f"Score Bar  : {bar}")

        print()

    print(Fore.MAGENTA +
          f"Search Time : {(end-start)*1000:.2f} ms")