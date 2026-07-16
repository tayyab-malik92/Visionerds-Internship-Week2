def build_context(documents, ids, distances):
    """
    Build a clean, formatted context from retrieved chunks.

    Returns:
        context (str): Combined document context for the LLM.
        source_info (list): List of dictionaries with chunk metadata.
    """

    context_parts = []
    source_info = []

    for i, (doc, chunk_id, distance) in enumerate(
            zip(documents, ids, distances), start=1):

        relevance = (1 - distance) * 100

        context_parts.append(
            f"""
==========================
Source {i} | {chunk_id}
Relevance: {relevance:.1f}%
==========================
{doc}
"""
        )

        source_info.append({
            "chunk_id": chunk_id,
            "relevance": relevance
        })

    context = "\n".join(context_parts)

    return context, source_info