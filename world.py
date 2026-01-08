##############################################################################
# Title: world
# Date: 12/19/2025
##############################################################################
"""Module that handles movement in the world."""
##############################################################################
# Imports and Global Variables -----------------------------------------------
import numpy as np
import input_utils as iu

# VOID = "🌳"
VOID = "•"


class PlacementError(Exception):
    """Error for invalid object placement on map."""
    def __init__(self, msg):
        self.msg = msg


# Functions and Classes ------------------------------------------------------
class World:
    """Create a game world the player can move around in.
    
    Stores a grid of lists, where each list contains all the objects on that
    space on the grid.

    Example:
    | []  []  [] |
    | []  []  [] |
    | []  []  [] |

    Each cell is a list that contains all the objects that are on that space.
    The object in position 0 of the list is always solid, and takes priority.
    """
    def __init__(self, size):
        self.rows = size[0]
        self.cols = size[1]
        self.grid = [[[VOID] for y in range(size[1])] for x in range(size[0])]
        self.entities = set()

    def get(self, x, y):
        """Return the contents of space (x, y).
        
        Parameters:
            x (int): row of grid
            y (int): column of grid
        
            Returns:
            (list): contents of cell (x, y)
        """
        return self.grid[x][y]
    
    def find(self, entity):
        """Return the position of an entity.
        
        Parameters:
            entity (Entity): the entity
        
        Returns:
        (array) the entity's position
        """
        return entity.pos
    
    def is_solid(self, x, y):
        """Check if a space contains a solid object.
        
        Parameters:
            x (int): row of grid
            y (int): column of grid
        
        Returns:
            (bool): is solid or not
        """
        return self.grid[x][y][0].is_solid
    
    def is_open(self, x, y):
        """Check if a space is open.
        
        Parameters:
            x (int): row of grid
            y (int): column of grid
        
        Returns:
            (bool): is open or not
        """
        return self.grid[x][y][0] == VOID or not self.is_solid(x, y)
    
    def add_entity(self, entity):
        """Add an entity to the world.
        
        Parameters:
            entity (Entity): the entity to add
        """
        self.place(entity, entity.pos)
        self.entities.add(entity)
    
    def del_entity(self, entity):
        """Delete an entity from the world.
        
        Parameters:
            entity (Entity): the entity to delete
        """
        self.grid[entity.pos[0]][entity.pos[1]].remove(entity)
        self.entities.remove(entity)

    def place(self, entity, target):
        """Place an entity at a target location.
        
        Parameters:
            entity (Entity): the entity to place
            target (list): the target location
        """
        if self.is_open(*target):
            if entity in self.entities:
                old_pos = self.find(entity)
                x_old = old_pos[0]
                y_old = old_pos[1]
                self.grid[x_old][y_old].remove(entity)
            entity.pos = target
            self.grid[target[0]][target[1]].insert(0, entity)
        else:
            raise PlacementError(f"Space ({target[0]}, {target[1]}) is already occupied by {self.get(*target)[0]}.")

    def move(self, entity, direction, count=1):
        """Move an entity in a direction for a specific amount of steps.
        
        Parameters:
            entity (Entity): the entity to move
            direction (list): the direction
            count (int): number of times to move
        """
        step = np.array(direction) * count
        target = entity.pos + step
        self.place(entity, target)

    def show(self):
        """Display the world to the user."""
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
    def __init__(self, pos, symbol, name, is_solid=True):
        self.pos = np.array(pos)
        self.symbol = symbol
        self.name = name
        self.is_solid = is_solid
    
    def move(self, x, y):
        move = np.array([x, y])
        target = self.map.get(self.pos + move)
        # Check collisions
        if not (target or target.is_obstacle):
            self.pos += move
    
    def __str__(self):
        return self.symbol
    
    def __repr__(self):
        return f"Entity(pos={self.pos}, symbol={self.symbol}, name={self.name}, is_solid={self.is_solid})"
    

def WorldPlayer(Entity):
    def __init__(self, pos, symbol, name):
        super().__init__(pos, symbol, name)
    
    def move(self, x, y):
        


def game_loop(world):
    pass

if __name__ == "__main__":
    map_ = World((10, 10))
    player = Entity(np.array([0, 0]), "P", "player1")
    player2 = Entity(np.array([4, 1]), "X", "player2")
    # print(map.get(2, 3))
    map_.add_entity(player)
    map_.add_entity(player2)
    map_.show()
    map_.place(player, [2, 3])
    map_.show()
    map_.move(player, [2, -2])
    map_.show()
