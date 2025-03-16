import random
import re
from .base_agent import BaseAgent

class DiceRollerAgent(BaseAgent):
    def __init__(self, name="DiceRoller", memory_agent=None):
        super().__init__(name, memory_agent)

    def handle_message(self, message: str, context: dict) -> str:
        """
        Parse the message for dice roll commands (e.g. '2d6') and simulate the roll.
        """
        pattern = r'(\d+)d(\d+)'
        match = re.search(pattern, message)
        if match:
            num_dice = int(match.group(1))
            dice_sides = int(match.group(2))
            results = [random.randint(1, dice_sides) for _ in range(num_dice)]
            total = sum(results)
            result_text = f"Rolling {num_dice}d{dice_sides}: {results} | Total: {total}"
        else:
            result_text = "No valid dice roll command found in your message."

        # Optionally, store the dice result in memory.
        if self.memory_agent:
            self.memory_agent.store_memory("dice", result_text)
        return result_text
