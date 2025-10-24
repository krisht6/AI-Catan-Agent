# game.py
import random
from player import Player
from board import Board

class Game:
    def __init__(self):
        self.board = Board()
        self.players = []
        self.current_turn = 0

    def add_player(self, name):
        self.players.append(Player(name))

    def roll_dice(self):
        return random.randint(1, 6) + random.randint(1, 6)

    def collect_resources(self, dice_roll):
        for tile in self.board.get_tiles():
            if tile.number == dice_roll:
                for player in self.players:
                    for settlement in player.settlements:
                        if settlement == tile:
                            player.collect_resource(tile.resource, 1)
                            print(f"{player.name} collects 1 {tile.resource} from tile {tile.number}.")

    def build_structure(self, player_name, tile, structure_type):
        # Basic structure building function, for settlements and cities
        player = next((p for p in self.players if p.name == player_name), None)
        if not player:
            print("Player not found.")
            return

        if structure_type == "settlement":
            if player.can_build_settlement():
                player.build_settlement(tile)
                print(f"{player.name} builds a settlement on tile {tile.number} ({tile.resource}).")
            else:
                print(f"{player.name} does not have enough resources to build a settlement.")
        elif structure_type == "city":
            if player.can_build_city():
                player.build_city(tile)
                print(f"{player.name} upgrades a settlement to a city on tile {tile.number} ({tile.resource}).")
            else:
                print(f"{player.name} does not have enough resources to build a city.")

    def play_turn(self):
        dice_roll = self.roll_dice()
        print(f"Dice roll: {dice_roll}")
        self.collect_resources(dice_roll)

        # Display each player's resources
        for player in self.players:
            print(f"{player.name}'s resources: {player.resources}")

    def start_game(self):
        for _ in range(10):  # Play 10 turns for demonstration
            print(f"\nTurn {self.current_turn + 1}")
            self.play_turn()
            self.current_turn += 1
