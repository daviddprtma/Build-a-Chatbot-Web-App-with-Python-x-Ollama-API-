import asyncio
import reflex as rx
from ollama import AsyncClient


class State(rx.State):
    question: str
    chat_history: list[tuple[str, str]]

    async def answer(self):
        yield rx.set_value("input_box", "")

        client = AsyncClient(host="http://localhost:11434/v1")

        model = "llama3"
        message = {'role': 'user', 'content': self.question}

        response = await AsyncClient().chat(model=model, messages=[message], stream=True)

        # Adds to the answer as the chatbot responds
        answer = ""

        self.chat_history.append((self.question, answer))

        # Clear the question input.
        self.question = ""

        # Yield here to clear the frontend input before continuing.
        yield

        async for part in response:
            answer += part["message"]["content"]
            self.chat_history[-1] = (self.chat_history[-1][0], answer)
            yield

    def key_enter(self, event):
        if event == "Enter":
            return self.answer()