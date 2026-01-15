##############################################################################
# Title: world
# Date: 12/19/2025
##############################################################################
"""Module that handles movement in the world."""
##############################################################################
# Imports and Global Variables -----------------------------------------------
import numpy as np
from numpy.linalg import norm
import input_utils as iu
import utils

# VOID = "🌳"
# VOID = "⚪"
# VOID = "  "
VOID = "· "  # marker for blank spaces
DIRECTIONS = {"up": np.array([0, -1]),
              "left": np.array([-1, 0]),
              "down": np.array([0, 1]),
              "right": np.array([1, 0])
}


# Functions and Classes ------------------------------------------------------
class PlacementError(Exception):
    """Error for invalid object placement on map."""
    def __init__(self, msg):
        self.msg = msg


class World:
    """Create a game world the player can move around in.

    Stores a grid of lists, where each list contains all the objects on that
    space on the grid.

    The coordinates are in standard screen coordinates with x going left-to-
    right and y going top-to-bottom.

    Example:
    | []  []  [] |
    | []  []  [] |
    | []  []  [] |

    Each cell is a list that contains all the objects that are on that space.
    The object in position 0 of the list is always solid, and takes priority.

    Attributes:
        rows (int): number of rows of map grid
        cols (int): number of columns of map grid
        grid (2x2xn array): array of lists containing entities at each tile
        entities (set): entities present in this world
    """
    def __init__(self, size):
        self.rows = size[0]
        self.cols = size[1]
        self.grid = [[[VOID] for y in range(size[1])] for x in range(size[0])]
        self.entities = set()

    def get(self, target):
        """Return the contents of a space.

        Parameters:
            target (list): coordinates of target tile

            Returns:
            (list): contents of cell (x, y)
        """
        return self.grid[target[0]][target[1]]

    def is_solid(self, target):
        """Check if a space contains a solid object.

        Parameters:
            target (list): coordinates of target tile

        Returns:
            (bool): is solid or not
        """
        cell = self.grid[target[0]][target[1]][0]
        return not (cell == VOID or not cell.is_solid)

    def is_open(self, target):
        """Check if a space is open.

        Parameters:
            target (list): coordinates of target tile

        Returns:
            (bool): is open or not
        """
        return self.grid[target[0]][target[1]][0] == VOID or not self.is_solid(target)

    def add_entity(self, *entities):
        """Add one or more entities to the world.

        Parameters:
            entity (Entity/list): the entity to add
        """
        for entity in entities:
            self.place(entity, entity.pos)
            self.entities.add(entity)

    def del_entity(self, *ids):
        """Delete one or more entities from the world.

        Parameters:
            entity (Entity/list): the entity to delete or its position
        """
        for id in ids:
            if isinstance(id, Entity):
                self.grid[id.pos[0]][id.pos[1]].remove(id)
                self.entities.remove(id)
            elif type(id) == list or type(id) == np.ndarray:
                self.grid[id[0]][id[1]].pop(0)

    def place(self, entity, target):
        """Place an entity at a target location.

        Parameters:
            entity (Entity): the entity to place
            target (list): the target location
        """
        if target[0] not in range(0, self.rows) or target[1] not in range(0, self.cols):
            raise PlacementError(f"Attempted to place entity {entity} out of bounds.")
        if self.is_open(target):
            if entity in self.entities:
                old_pos = entity.get_pos()
                x_old = old_pos[0]
                y_old = old_pos[1]
                self.grid[x_old][y_old].remove(entity)
            entity.set_pos(target)
            self.grid[target[0]][target[1]].insert(0, entity)
        else:
            raise PlacementError(f"Space ({target[0]}, {target[1]}) is already occupied by {self.get(target)[0]}.")

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
    """Create an entity that lives in a World class.

    Attributes:
        pos (ndarray): entity's position in its world
        symbol (str): entity's map icon
        name (str): name of entity
        is_solid (bool): can be moved through or not
    """
    def __init__(self, pos, symbol, name, is_solid=True):
        self.pos = np.array(pos, dtype=int)
        self.symbol = symbol
        self.name = name
        self.is_solid = is_solid

    def get_pos(self):
        """Return position of this entity."""
        return self.pos.tolist()

    def set_pos(self, new_pos):
        """Set position of this entity.
        
        Parameters:
            new_pos (list): new coordinates of this entity
        """
        self.pos = np.array(new_pos)

    def __str__(self):
        return self.symbol

    def __repr__(self):
        return f"Entity(pos={self.pos}, symbol={self.symbol}, name={self.name}, is_solid={self.is_solid})"


class WorldPlayer(Entity):
    """Create a player entity."""
    def __init__(self, pos, symbol, name):
        super().__init__(pos, symbol, name)

    def __repr__(self):
        return f"WorldPlayer(pos={self.pos}, symbol={self.symbol}, name={self.name}, is_solid={self.is_solid})"


class Objective(Entity):
    """Create an objective entity.
    
    The player wins when they reach this tile.
    """
    def __init__(self, pos, symbol, name):
        super().__init__(pos, symbol, name, is_solid=False)

    def __repr__(self):
        return f"Objective(pos={self.pos}, symbol={self.symbol}, name={self.name}, is_solid={self.is_solid})"


class Wall(Entity):
    """Create a wall entity."""
    def __init__(self, pos, symbol):
        super().__init__(pos, symbol, name="Wall", is_solid=True)

    def __repr__(self):
        return f"Objective(pos={self.pos}, symbol={self.symbol}, name={self.name}, is_solid={self.is_solid})"


class Decor(Entity):
    """Create a decor entity."""
    def __init__(self, pos, symbol, is_solid=False):
        super().__init__(pos, symbol, name="Decor", is_solid=is_solid)

    def __repr__(self):
        return f"Objective(pos={self.pos}, symbol={self.symbol}, name={self.name}, is_solid={self.is_solid})"


def move_player(player, objective, world):
    """Get user input and move player.
    
    Parameters:
        player (WorldPlayer): the player entity to move
        objective (Objective): the objective the player needs to reach
        world (World): the world the player is in
    """
    while True:
        direction = iu.menu(f"Move to the {objective.name} ({objective.symbol}): ", DIRECTIONS.keys(), keymap="wasd")
        movement = DIRECTIONS[direction]
        try:
            world.move(player, movement)
            break
        except PlacementError:
            print("\n--- INVALID MOVEMENT ---\nThat space is full or out of bounds!")


def make_wall(map_, start, end, orientation=None, custom_icon=None):
    """Create a wall on the map.
    
    Parameters:
        map_ (World): the map on which wall will be made
        start (list): start point of wall
        end (list): end point of wall
        orientation (str): Which way wall is facing, L or R
        custom_icon (str): use a custom icon for the wall
    """
    start = np.array(start)
    end = np.array(end)
    try:
        direction = (end - start) / norm(end - start)
    except ZeroDivisionError:  # start and end are identical
        direction = np.array([0, 0])
    if np.isnan(direction).any():
        direction = np.array([0, 0])
    # Pick symbol of wall
    if custom_icon:
        icon = custom_icon
    elif np.array_equal(np.abs(direction), np.array([1.0, 0.0])):
        # Horizontal wall
        icon = "➖"
    elif np.array_equal(np.abs(direction), np.array([0.0, 1.0])) or np.array_equal(direction, np.array([0.0, 0.0])):
        # Vertical wall
        if orientation == "L":
            icon = "┃ "
        elif orientation == "R":
            icon = " ┃"
        else:
            raise ValueError("vertical walls require orientation 'L' or 'R'.")
    else:
        raise ValueError("Failed to build wall due to invalid start and end (no diagonals).")
    num_tiles = int(norm(end - start)) + 1
    direction = direction.astype(int)
    for tile in range(num_tiles):
        wall = Wall(start + direction*tile, icon)
        map_.add_entity(wall)


def make_building(map_, *corners, custom_icon=None):
    """Make a series of connected walls.

    Corners should be passed in order of connection.
    
    Parameters:
        map_ (World): the world in which the building is made
        corners (list(s)): each corner point of the building
        custom_icon (str): use a custom wall icon
    """
    corners = np.array(corners)
    corners -= np.ones_like(corners)  # Offset by one so easier visual work
    last_direction = None  # To determine if wall is left or right
    for connection in range(len(corners)-1):
        corner1 = corners[connection]
        corner2 = corners[connection+1]
        c1_to_c2 = corner2 - corner1  # Get distance from corner1 to corner2
        # Find unit vector (length 1) from c1 to c2
        c1_to_c2_unit = c1_to_c2 / norm(c1_to_c2)
        if c1_to_c2_unit[0] != 0:  # Horizontal wall
            make_wall(map_, corner1, corner2, custom_icon=custom_icon)
            last_direction = "R" if c1_to_c2_unit[0] > 0 else "L"
        elif c1_to_c2_unit[1] != 0:  # Vertical wall
            orientation = last_direction
            make_wall(map_, corner1+c1_to_c2_unit, corner2-c1_to_c2_unit, orientation, custom_icon=custom_icon)


def build_map():
    """Make the map.

    Starts by creating a World and then adding walls and decor.
    """
    full_map = World((25, 25))
    # Admin building
    make_building(full_map, [8, 11], [7, 11], [7, 14], [8, 14], [8, 17],
                  [10, 17], [10, 15], [12, 15], [12, 18],[17, 18], [17, 14],
                  [19, 14], [19, 11], [17, 11], [17, 8], [14, 8], [14, 11],
                  [9, 11])
    # Dorms
    make_building(full_map, [7, 3], [3, 3], [3, 6], [7, 6], [7, 4])
    # Administration building
    make_building(full_map, [7, 21], [6, 21], [6, 18], [4, 18], [4, 20],
                  [2, 20], [2, 24], [7, 24], [7, 22])
    # Ballroom
    make_building(full_map, [19, 4], [21, 4], [21, 7], [23, 7], [23, 2],
                  [19, 2])
    # Library
    make_building(full_map, [22, 19], [19, 19], [19, 24], [22, 24], [22, 19])
    # Make doors
    full_map.del_entity([6, 11], [6, 12], [16, 15], [18, 20], [18, 21],
                        [21, 20], [21, 21])
    # Add building names
    full_map.add_entity(Decor([3, 3], "️D "))
    full_map.add_entity(Decor([14, 8], "️M "))
    full_map.add_entity(Decor([2, 20], "️A "))
    full_map.add_entity(Decor([21, 2], "️B "))
    full_map.add_entity(Decor([19, 19], "️L "))
    # Add world border
    make_building(full_map, [25, 1], [1, 1], [1, 25], [25, 25],
                  custom_icon="⬛")
    # Trees 🌳 🌲
    full_map.add_entity(Decor([23, 15], "🌳"), Decor([24, 23], "🌳"),
                        Decor([21, 9], "🌲"), Decor([23, 2], "🌳"),
                        Decor([22, 13], "🌳"), Decor([22, 19], "🌲"),
                        Decor([24, 5], "🌳"), Decor([23, 8], "🌳"),
                        Decor([24, 14], "🌲"), Decor([23, 22], "🌳"),
                        Decor([24, 20], "🌳"), Decor([24, 10], "🌲"))
    return full_map


def game_loop(objective):
    """Start a map segment minigame.

    Parameters:
        objective (str): where the player needs to move to
    """
    building_dict = {
        "main building": [13, 13],
        "dorms": [4, 4],
        "library": [20, 20],
        "administration office": [4, 18],
        "ballroom": [21, 5],
        "forest": [23, 14],
    }
    # Find goal position
    if objective.lower() in building_dict:
        goal_pos = building_dict[objective]
    else:
        raise KeyError(f"'{objective}' is not a valid objective location.")
    # Initialize world objects
    game = build_map()
    player1 = WorldPlayer(np.array([1, 14]), "🏃", "player")
    # ⭕  ➖  🏃 ┃ 
    goal = Objective(goal_pos, "⭕", objective)
    game.add_entity(player1)
    game.add_entity(goal)
    while True:
        utils.clear()
        game.show()
        move_player(player1, goal, game)
        if player1.get_pos() == goal.get_pos():
            utils.clear()
            break


if __name__ == "__main__":
    game_loop("forest")
