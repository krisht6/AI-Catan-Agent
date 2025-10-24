# board.py
from tile import Tile
import random

class Board:
    def __init__(self):
        self.tiles = []
        self.setup_tiles()

    def setup_tiles(self):
        # Define resources and numbers typically used in Catan
        resources = ["wood", "brick", "wheat", "ore", "sheep", "desert"]
        numbers = [2, 3, 3, 4, 4, 5, 5, 6, 6, 8, 8, 9, 9, 10, 10, 11, 11, 12]

        # Shuffle resources and numbers to assign them randomly
        resource_distribution = random.choices(resources, k=19)
        number_distribution = random.sample(numbers, k=18) + [0]  # 0 for desert

        # Create tiles with assigned resources and numbers
        for i in range(19):
            resource = resource_distribution[i]
            number = number_distribution[i] if resource != "desert" else 0
            tile = Tile(resource, number)
            self.tiles.append(tile)

    def get_tiles(self):
        return self.tiles
