import requests

class RAGLLM:
    def __init__(self):
        print("Using Qwen via Ollama...")

    def call_ollama(self, prompt):
        try:
            response = requests.post(
                "http://localhost:11434/api/generate",
                json={
                    "model": "qwen:4b",
                    "prompt": prompt,
                    "stream": False
                }
            )

            data = response.json()

            if "response" in data:
                answer = data["response"].strip()
            else:
                return f"Error from model: {data}"

            # Remove unwanted Yes/No starts if model still outputs them
            if answer.lower().startswith(("yes", "no")):
                parts = answer.split(".", 1)
                if len(parts) > 1:
                    answer = parts[1].strip()

            return answer

        except Exception as e:
            return f"Request failed: {str(e)}"

    def generate(self, query, records):
        # Build context text
        context_text = "\n".join(
            f"{r['timestamp']} | {r['role']} performing {r['action']}"
            for r in records
        )

        # Prompt with summary handling added
        prompt = f"""
You are an intelligent healthcare assistant.

You must answer in a natural, human-like way.

IMPORTANT INSTRUCTIONS:
- NEVER start your answer with "Yes" or "No"
- NEVER give a binary answer
- Always respond in a descriptive sentence
- Do NOT mention logs, context, or data

- If the query asks for a summary:
  • Provide a concise summary of activities
  • If "patient" is mentioned → summarize only patient actions
  • If "caregiver" is mentioned → summarize only caregiver actions
  • Otherwise → summarize all relevant activities
  • Keep it within 2–3 sentences, clear and natural

Task:
- If the action is present → describe it naturally
- If the action is NOT present → clearly explain that it was not observed
- If unrelated → answer normally

Answer Style:
- Natural and conversational
- One or two sentences maximum (except summary: max 2–3 sentences)
- Clear and specific

Examples:
Q: did the patient drink water?
A: The patient was seen drinking water during the observed period.

Q: did the caregiver cook food?
A: There is no indication that the caregiver was involved in cooking food.

Q: give a summary of patient activities
A: The patient spent time walking, sitting, and interacting with objects during the observed period.

Context:
{context_text}

Question:
{query}

Answer:
"""

        return self.call_ollama(prompt)