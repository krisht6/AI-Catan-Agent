# player.py

class Player:
    def __init__(self, name):
        self.name = name
        self.resources = {
            "wood": 0,
            "brick": 0,
            "wheat": 0,
            "ore": 0,
            "sheep": 0
        }
        self.settlements = []  # Locations of settlements on the board
        self.cities = []       # Locations of cities on the board

    def collect_resource(self, resource, amount):
        if resource in self.resources:
            self.resources[resource] += amount

    def can_build_settlement(self):
        # Check if player has enough resources for a settlement
        return (self.resources["wood"] >= 1 and
                self.resources["brick"] >= 1 and
                self.resources["sheep"] >= 1 and
                self.resources["wheat"] >= 1)

    def build_settlement(self, tile):
        if self.can_build_settlement():
            self.settlements.append(tile)
            self.resources["wood"] -= 1
            self.resources["brick"] -= 1
            self.resources["sheep"] -= 1
            self.resources["wheat"] -= 1

    def can_build_city(self):
        # Check if player has enough resources for a city
        return (self.resources["ore"] >= 3 and
                self.resources["wheat"] >= 2)

    def build_city(self, tile):
        if tile in self.settlements and self.can_build_city():
            self.settlements.remove(tile)
            self.cities.append(tile)
            self.resources["ore"] -= 3
            self.resources["wheat"] -= 2
