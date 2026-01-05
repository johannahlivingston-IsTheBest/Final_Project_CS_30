##############################################################################
# Title: world
# Date: 12/19/2025
##############################################################################
"""Module that handles movement in the world."""
##############################################################################
# Imports and Global Variables -----------------------------------------------
import numpy as np

VOID = "🌳"
VOID = "•"

# Functions and Classes ------------------------------------------------------
class World:
    """Create a game world the player can move around in."""
    def __init__(self, size):
        self.rows = size[0]
        self.cols = size[1]
        self.map = [[[VOID] for y in range(size[1])] for x in range(size[0])]

    def get(self, x, y):
        return self.map[x][y]

    def place(self, entity, target):
        self.map[target].append(self.map[space])
        self.map[space].remove(self.)

    def move(self, target, direction, count):
        pass

    def show(self):
        print("\n")
        for y in range(self.cols):
            print("\n     ", end="")
            for x in range(self.rows):
                print(f' {self.map[x][y]} ', end="")


class Entity():
    """Map object.
    
    Should have attributes:
    - pos
    - obstacle (bool)
    """
    def __init__(self, map, pos, is_obstacle=True):
        self.map = map
        self.pos = pos
        self.is_obstacle = is_obstacle
    
    def move(self, x, y):
        move = np.array([x, y])
        target = self.map.get(self.pos + move)
        
        self.pos += move if not (target or target.is_obstacle) else None


if __name__ == "__main__":
    map = World((10, 10))
    # print(map.get(2, 3))
    map.show()
