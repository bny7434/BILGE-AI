from core.ollama_client import OllamaClient


class ChatManager:

    def __init__(self):
        self.client = OllamaClient()

    def ask(self, prompt):
        return self.client.ask(prompt)