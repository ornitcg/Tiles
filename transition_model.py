from node import *
from constants import *
from action import *

class Transition_Model:
#
#     def get_neighbors(self, node):
#         neighbors = []
#         for action in ACTIONS:
#            neighbor = node.action(action)
#            if neighbor is not None:
#                neighbors.append(neighbor)
#         return neighbors
#
# class Transition_Model:

    # Returns the neighbor node after applying the action
    def apply_action(self, node, action):
        row, col = node.get_blank_tile_position()
        new_row, new_col = row, col
        direction = action.get_direction()
        if direction == UP:
            new_row = row - 1
        elif direction == DOWN:
            new_row = row + 1
        elif direction == LEFT:
            new_col = col - 1
        elif direction == RIGHT:
            new_col = col + 1

        # is new position (of empty tile) valid?
        if not (0 <= new_row < BOARD_SIDE and 0 <= new_col < BOARD_SIDE):
            return None

        # Create a new node similar to its parent
        neighbor = Node(node.tiles_list.copy(), parent=node, cause=action, value=node.value + 1)
        # update the new node's tiles list
        neighbor.swap_tiles(row, col, new_row, new_col)
        tile_number = neighbor.tiles_list[row * BOARD_SIDE + col]
        neighbor.set_number_tile_that_moved(tile_number)
        return neighbor