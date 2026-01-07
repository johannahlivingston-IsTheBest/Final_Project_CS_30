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
    """Create a game world the player can move around in."""
    def __init__(self, size):
        self.rows = size[0]
        self.cols = size[1]
        self.grid = [[[VOID] for y in range(size[1])] for x in range(size[0])]
        self.entities = set()

    def get(self, x, y):
        return self.grid[x][y]
    
    def find(self, entity):
        return entity.pos
    
    def is_solid(self, x, y):
        return self.grid[x][y][0].is_solid
    
    def is_open(self, x, y):
        return self.grid[x][y][0] == VOID or not self.is_solid(x, y)
    
    def add_entity(self, entity):
        self.place(entity, entity.pos)
        self.entities.add(entity)
    
    def del_entity(self, entity):
        self.grid[entity.pos[0]][entity.pos[1]].remove(entity)
        self.entities.remove(entity)

    def place(self, entity, target):
        if self.is_open(*target):
            if entity in self.entities:
                old_pos = self.find(entity)
                x_old = old_pos[0]
                y_old = old_pos[1]
                self.grid[x_old][y_old].remove(entity)
            entity.pos = target
            self.grid[target[0]][target[1]].insert(0, entity)
        else:
            print("THAT'S ILLEGAL")

    def move(self, entity, direction, count=1):
        step = np.array(direction) * count
        target = entity.pos + step
        self.place(entity, target)

    def show(self):
        print("\n")
        for y in range(self.cols):
            print("\n     ", end="")
            for x in range(self.rows):
                print(f' {self.grid[x][y][0]} ', end="")


class Entity():
    """Map object.
    
    Should have attributes:
    - pos
    - obstacle (bool)
    """
    def __init__(self, world, pos, symbol, is_obstacle=True):
        self.world = world
        self.pos = np.array(pos)
        self.symbol = symbol
        self.is_obstacle = is_obstacle
    
    def move(self, x, y):
        move = np.array([x, y])
        target = self.map.get(self.pos + move)
        # Check collisions
        if not (target or target.is_obstacle):
            self.pos += move
    
    def __str__(self):
        return self.symbol


if __name__ == "__main__":
    map_ = World((10, 10))
    player = Entity(map_, np.array([0, 0]), "P")
    # print(map.get(2, 3))
    map_.add_entity(player)
    map_.show()
    map_.place(player, [2, 3])
    map_.show()
    map_.move(player, [3, 0])
    map_.show()
