from agents.narrator_agent import NarratorAgent
from agents.memory_agent import MemoryAgent


# game_manager.py

class GameManager:
    def __init__(self):
        self.memory_agent = MemoryAgent()
        self.dm_agent = NarratorAgent(memory_agent=self.memory_agent)
        self.game_details = {}
        self.players = {}

    def game_setup_initial(self, setting: str, player1: str, player2: str) -> str:
        # Save game details and player sketches.
        self.game_details['setting'] = setting
        self.players['player1'] = player1
        self.players['player2'] = player2

        # Construct an initialization prompt.
        init_prompt = (
            "You are a Dungeon Master for a tabletop role-playing game. "
            "Based on the following game details and player character sketches, "
            "generate an epic initial plot, detailed character sketches for both players, "
            "and set the stage for an unforgettable adventure.\n\n"
            f"Game Setting: {setting}\n"
            f"Player 1 Sketch: {player1}\n"
            f"Player 2 Sketch: {player2}\n\n"
            "Initial Narrative:"
        )
        
        # Generate and store the initial narrative only once.
        initial_narrative = self.dm_agent.handle_message(init_prompt, {"narrative": ""})
        # Clear any previous narrative before storing.
        self.memory_agent.memory_store["narrative"] = [initial_narrative]
        return initial_narrative

    def process_move(self, move: str) -> str:
        # Build a prompt for updating the narrative based on the move.
        current_narrative = self.memory_agent.summarize_memory("narrative")
        update_prompt = (
            "Continue the story by integrating the current narrative and the player's move. "
            "Keep the narrative coherent and evolving.\n\n"
            f"Current Narrative:\n{current_narrative}\n\n"
            f"Player's Move: {move}\n\n"
            "Updated Narrative:"
        )
        updated_narrative = self.dm_agent.handle_message(update_prompt, {"narrative": current_narrative})
        # Instead of appending the whole narrative again, update with the new part only:
        self.memory_agent.store_memory("narrative", updated_narrative)
        return updated_narrative

    def run_game(self):
        print("The game is now starting!\n")
        
        # Show the initial narrative.
        current_narrative = self.memory_agent.summarize_memory("narrative")
        print("Dungeon Master (DM) sets the scene:")
        print(current_narrative)
        print("\n")
        
        turn = 1
        while True:
            # Alternate turns between Player 1 and Player 2.
            current_player = "Player 1" if turn % 2 == 1 else "Player 2"
            
            print(f"{current_player}, it's your move!")
            player_move = input("Enter your move (or type 'exit' to end the game): ")
            if player_move.lower() == "exit":
                print("Exiting game. Thank you for playing!")
                break
            
            # Build a prompt for the DM to update the narrative based on the player's move.
            update_prompt = (
                "You are a Dungeon Master guiding an epic tabletop role-playing game. "
                "Continue the story by integrating the current narrative with the player's move. "
                "Make the narrative engaging, coherent, and evolve the plot accordingly.\n\n"
                f"Current Narrative:\n{self.memory_agent.summarize_memory('narrative')}\n\n"
                f"{current_player}'s Move: {player_move}\n\n"
                "Updated Narrative:"
            )
            
            # Generate the updated narrative.
            updated_narrative = self.dm_agent.handle_message(update_prompt, {"narrative": self.memory_agent.summarize_memory("narrative")})
            
            # Save the updated narrative.
            self.memory_agent.store_memory("narrative", updated_narrative)
            
            print("\n--- Updated Narrative ---\n")
            print(updated_narrative)
            print("\n-------------------------\n")
            
            turn += 1
