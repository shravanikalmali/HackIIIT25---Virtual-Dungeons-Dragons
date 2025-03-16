import openai
from config import AZURE_OPENAI_API_KEY, AZURE_OPENAI_ENDPOINT, AZURE_OPENAI_DEPLOYMENT
from .base_agent import BaseAgent

# Ensure Azure OpenAI settings are in place.
openai.api_key = AZURE_OPENAI_API_KEY
openai.api_type = "azure"
openai.api_base = AZURE_OPENAI_ENDPOINT
openai.api_version = "2023-03-15-preview"

class NPCInteractionAgent(BaseAgent):
    def __init__(self, name="NPC", memory_agent=None):
        super().__init__(name, memory_agent)

    def handle_message(self, message: str, context: dict) -> str:
        """
        Generate a dialogue response as an NPC based on the provided user message.
        """
        prompt = (
            "You are a non-player character (NPC) in a fantasy role-playing game. "
            "Respond in character to the following dialogue.\n"
            f"Dialogue: {message}\n"
            "NPC Response:"
        )
        response = openai.Completion.create(
            engine=AZURE_OPENAI_DEPLOYMENT,
            prompt=prompt,
            max_tokens=100,
            temperature=0.9,
            n=1
        )
        text = response.choices[0].text.strip()
        # Save NPC dialogue in memory.
        if self.memory_agent:
            self.memory_agent.store_memory("npc", text)
        return text
