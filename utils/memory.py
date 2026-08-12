from langchain_core.messages import HumanMessage, AIMessage


class ChatMemory:

    def __init__(self):
        self.messages = []

    def add_user(self, message):
        self.messages.append(HumanMessage(content=message))

    def add_ai(self, message):
        self.messages.append(AIMessage(content=message))

    def get_history(self):
        return self.messages

    def clear(self):
        self.messages = []