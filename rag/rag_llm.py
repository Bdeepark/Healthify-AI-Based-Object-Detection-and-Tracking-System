from transformers import pipeline

class RAGLLM:
    def __init__(self):
        self.generator = pipeline(
            "text2text-generation",
            model="google/flan-t5-base",
            max_new_tokens=100
        )

    def generate(self, query, context):
        if not context:
            return "No relevant events found."

        # Convert context into readable text
        context_text = "\n".join([
            f"Frame {r['frame']}: Person {r['person_id']} is {r['action']}"
            for r in context
        ])

        prompt = f"""
Answer the question based on the context.

Context:
{context_text}

Question:
{query}

Answer:
"""

        output = self.generator(prompt)[0]["generated_text"]
        return output.strip()