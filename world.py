##############################################################################
# Title: world
# Date: 12/19/2025
##############################################################################
"""Module that handles movement in the world."""
##############################################################################
# Imports and Global Variables -----------------------------------------------
import numpy as np

# Functions and Classes ------------------------------------------------------
class World:
    """Create a game world the player can move around in."""
    def __init__(self, size):
        self.X = size[0]
        self.Y = size[1]
        self.map = [["🌳" for y in range(size[1])] for x in range(size[0])]

    def get(self, x, y):
        return self.map[x][y]

    def move(self):
        pass

    def place(self):
        pass

    def show(self):
        print("\n")
        for y in range(self.Y):
            print("\n     ", end="")
            for x in range(self.X):
                print(f' {self.map[x][y]} ', end="")


if __name__ == "__main__":
    map = World((10, 10))
    print(map.get(2, 3))
    map.show()