import abc

class BaseAgent(abc.ABC):
    def __init__(self, name: str, memory_agent=None):
        self.name = name
        self.memory_agent = memory_agent

    @abc.abstractmethod
    def handle_message(self, message: str, context: dict) -> str:
        """
        Process an incoming message along with context and return a response.
        """
        pass
