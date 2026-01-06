##############################################################################
# Title: world
# Date: 12/19/2025
##############################################################################
"""Module that handles movement in the world."""
##############################################################################
# Imports and Global Variables -----------------------------------------------
import numpy as np

# VOID = "🌳"
VOID = "•"

# Functions and Classes ------------------------------------------------------
class World:
    """Create a game world the player can move around in.
    Brainstorming
    How to organize
    Need multiple objects on one space
    Need to be able to move easily
    Could maybe have a render function.
    Store positions in objects themselves, world just knows what objects it has.
    To render, loop through all indices on the grid. Search dictionary. If key
    matches, display that object. Otherwise, display VOID.
    Maybe just search through list of entities to grab latest positions?
    If I move through the entities themselves, map somehow needs to get that updated info.

    I need two things:
    (1) given entity, find its position;
    (2) and given position, find entity that is there.

    What I actually need
    Moving around: check collisions (task 2)
    
    """
    def __init__(self, size):
        self.rows = size[0]
        self.cols = size[1]
        # self.map = [[[VOID] for y in range(size[1])] for x in range(size[0])]
        # Dictionary format: 
        self.entities = []

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
        # Check collisions
        if not (target or target.is_obstacle):
            self.pos += move


if __name__ == "__main__":
    map = World((10, 10))
    # print(map.get(2, 3))
    map.show()
