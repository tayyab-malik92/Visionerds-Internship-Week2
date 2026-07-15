import chromadb
from sentence_transformers import SentenceTransformer


class VectorStore:

    def __init__(self):

        print("Loading Embedding Model...")

        self.model = SentenceTransformer(
            "all-MiniLM-L6-v2"
        )

        print("Embedding Model Loaded!")

        print("Starting ChromaDB...")

        self.client = chromadb.PersistentClient(path="./chroma_db")

        self.collection = self.client.get_or_create_collection(
            name="visionerds_day8",
            metadata={"hnsw:space": "cosine"}
        )

        print("ChromaDB Ready!\n")

    def add_chunks(self, chunks):

        existing = self.collection.count()

        if existing > 0:

            print("Database already contains embeddings.")
            print("Skipping embedding generation.\n")
            return

        embeddings = self.model.encode(
            chunks,
            normalize_embeddings=True
        ).tolist()

        ids = [
            f"chunk_{i}"
            for i in range(len(chunks))
        ]

        self.collection.add(
            ids=ids,
            documents=chunks,
            embeddings=embeddings
        )

        print(f"{len(chunks)} chunks stored successfully.\n")

    def search(self, query, top_k=3):

        query_embedding = self.model.encode(
            [query],
            normalize_embeddings=True
        ).tolist()

        results = self.collection.query(
            query_embeddings=query_embedding,
            n_results=top_k
        )

        return results