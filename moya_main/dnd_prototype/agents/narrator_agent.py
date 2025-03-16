import openai
from config import AZURE_OPENAI_API_KEY, AZURE_OPENAI_ENDPOINT
from .base_agent import BaseAgent

# Configure OpenAI API parameters (using Azure credentials).
openai.api_key = AZURE_OPENAI_API_KEY
openai.api_type = "azure"
openai.api_base = AZURE_OPENAI_ENDPOINT
openai.api_version = "2023-03-15-preview"  # Adjust if needed

class NarratorAgent(BaseAgent):
    def __init__(self, name="DungeonMaster", memory_agent=None):
        super().__init__(name, memory_agent)

    def handle_message(self, message: str, context: dict) -> str:
        """
        Generate narrative text using the provided message and context.
        """
        prompt = message  # Extend or incorporate context as needed.

        # Use the Chat Completions API with only the model parameter.
        # In Azure OpenAI, the model parameter is used as the deployment name.
        response = openai.chat.completions.create(
            model="gpt-35-turbo",  # Ensure this exactly matches your configured deployment name.
            messages=[{"role": "user", "content": prompt}],
            max_tokens=400,
            temperature=0.8,
            n=1
        )

        # Extract the generated message.
        text = response.choices[0].message.content.strip()

        # Optionally, store the generated narrative in memory.
        if self.memory_agent:
            self.memory_agent.store_memory("narrative", text)
        return text
