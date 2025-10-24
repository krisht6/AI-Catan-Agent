# main.py
from game import Game

def main():
    game = Game()
    game.add_player("p1")
    game.add_player("p2")

    # Start the game
    game.start_game()

if __name__ == "__main__":
    main()
