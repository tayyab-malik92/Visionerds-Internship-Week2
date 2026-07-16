def build_prompt(context, question):
    """
    Builds the final user prompt for the LLM.
    """

    prompt = f"""
You are provided with retrieved document context.

Your task is to answer the user's question ONLY using the information in the context.

If the answer is not present in the context, respond exactly:

I couldn't find that information in the provided document.

==================================================
DOCUMENT CONTEXT
==================================================

{context}

==================================================
USER QUESTION
==================================================

{question}

==================================================
ANSWER
==================================================
"""

    return prompt