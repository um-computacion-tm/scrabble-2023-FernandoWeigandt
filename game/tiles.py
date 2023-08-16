import random

class Tile:
    def __init__(self, letter, value):
        self.letter = letter
        self.value = value

class TileBag:
    def __init__(self):
        self.tiles = []
