import re

class MessageClassifier:
    """
    Classify incoming messages so that they are handled by the appropriate agent.
    """
    def classify(self, message: str) -> str:
        # If the message contains a dice roll command, return 'dice'.
        if re.search(r'\d+d\d+', message):
            return "dice"
        # If the message contains keywords associated with NPC dialogues.
        elif any(keyword in message.lower() for keyword in ["npc", "character", "dialogue", "talk"]):
            return "npc"
        # Default to narrative if no specific command is found.
        else:
            return "narrative"
