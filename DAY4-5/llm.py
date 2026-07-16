from groq import Groq
from config import GROQ_API_KEY, MODEL_NAME, SYSTEM_PROMPT
from prompt_builder import build_prompt


class LLM:

    def __init__(self):

        print("Connecting to Groq...")

        self.client = Groq(api_key=GROQ_API_KEY)

        print("Groq Connected!\n")

    def ask(self, context, question):
        """
        Generates an answer using the retrieved document context.
        """

        prompt = build_prompt(
            context=context,
            question=question
        )

        response = self.client.chat.completions.create(

            model=MODEL_NAME,

            messages=[
                {
                    "role": "system",
                    "content": SYSTEM_PROMPT
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],

            temperature=0.1,
            max_tokens=700,
            top_p=0.9
        )

        return response.choices[0].message.content.strip()