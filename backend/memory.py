from prompt import SYSTEM_PROMPT

class Memory:

    def __init__(self):
        self.messages = [
            {
                "role": "system",
                "content": SYSTEM_PROMPT
            }
        ]

    def add_user(self, text):
        self.messages.append({
            "role": "user",
            "content": text
        })

    def add_ai(self, text):
        self.messages.append({
            "role": "assistant",
            "content": text
        })

    def history(self):
        return self.messages

memory = Memory()
