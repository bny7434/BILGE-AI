import ollama


class OllamaClient:

    def __init__(self):
        self.model = "qwen3:8b"

    def ask(self, prompt: str) -> str:

        response = ollama.chat(
            model=self.model,
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        return response["message"]["content"]