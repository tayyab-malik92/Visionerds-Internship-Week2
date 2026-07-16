def create_chunks(text, chunk_size=400, overlap=100):
    """
    Splits text into overlapping chunks.

    Args:
        text (str): Complete document text
        chunk_size (int): Maximum words in each chunk
        overlap (int): Number of overlapping words

    Returns:
        list: List of text chunks
    """

    words = text.split()

    chunks = []

    step = chunk_size - overlap

    for i in range(0, len(words), step):

        chunk = words[i:i + chunk_size]

        chunks.append(" ".join(chunk))

        if i + chunk_size >= len(words):
            break

    return chunks