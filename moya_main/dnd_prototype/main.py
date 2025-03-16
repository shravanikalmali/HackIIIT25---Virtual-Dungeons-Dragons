from game_manager import GameManager

def main():
    game = GameManager()
    # Initialize the game (collect details and generate initial plot/characters).
    game.game_setup()
    # Start the turn-based gameplay loop.
    game.run_game()

if __name__ == "__main__":
    main()
