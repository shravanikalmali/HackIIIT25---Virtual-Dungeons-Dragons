class MemoryAgent:
    def __init__(self):
        self.memory_store = {}

    def store_memory(self, thread: str, message: str):
        if thread not in self.memory_store:
            self.memory_store[thread] = []
        self.memory_store[thread].append(message)

    def get_memory(self, thread: str, limit: int = 10):
        return self.memory_store.get(thread, [])[-limit:]

    def summarize_memory(self, thread: str) -> str:
        messages = self.memory_store.get(thread, [])
        if not messages:
            return ""
        summary = "\n".join(messages[-5:])
        return summary
