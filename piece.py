
class Piece:
    def __init__(self, owner):
        self.owner = owner

class Settlement(Piece):
    def __init__(self, owner):
        super().__init__(owner)
        self.type = "settlement"

class City(Piece):
    def __init__(self, owner):
        super().__init__(owner)
        self.type = "city"

class Road(Piece):
    def __init__(self, owner):
        super().__init__(owner)
        self.type = "road"
