import streamlit as st
from game_manager import GameManager

def main():
    st.title("Virtual Tabletop RPG")
    
    game = GameManager()
    
    st.header("Game Setup")
    setting = st.text_input("Enter the general idea, setting, theme, location, villain etc.:")
    player1 = st.text_input("Player 1: Describe your character:")
    player2 = st.text_input("Player 2: Describe your character:")
    
    if st.button("Initialize Game"):
        if setting and player1 and player2:
            initial_narrative = game.game_setup_initial(setting, player1, player2)
            st.success("Game Initialized!")
            st.write("--- Initial Game Setup ---")
            st.write(initial_narrative)
        else:
            st.error("Please fill in all fields.")
    
    st.header("Gameplay")
    if st.session_state.get("game_initialized", False):
        # Display current narrative once.
        current_context = game.memory_agent.summarize_memory("narrative")
        st.subheader("Current Narrative")
        st.write(current_context)
    
    move = st.text_input("Enter your move (or type 'exit' to end the game):")
    if st.button("Submit Move"):
        if move.lower() == "exit":
            st.info("Exiting game. Thank you for playing!")
        else:
            updated_narrative = game.process_move(move)
            st.write("--- Updated Narrative ---")
            st.write(updated_narrative)

if __name__ == "__main__":
    main()
