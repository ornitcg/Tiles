
from constants import *
from node import *
from transition_model import *

class State_Space:
    def __init__(self):
        self.transition_model = Transition_Model()


    def get_initial_state(self, tiles_list):
        """Create the initial state from a list of tiles"""
        return Node(tiles_list, is_initial=True)

    def get_goal_state(self):
        """Return the goal state"""
        return Node(GOAL_STATE, is_goal=True)

    def is_goal_state(self, node):
        """Check if the given node is a goal state"""
        return node.tiles_list == GOAL_STATE

    def get_valid_actions(self, node):
        """Get valid actions for the given state"""
        valid_actions = []
        row, col = node.get_blank_tile_position()

        if row > 0:  # Can move UP
            valid_actions.append(UP)
        if row < BOARD_SIDE - 1:  # Can move DOWN
            valid_actions.append(DOWN)
        if col > 0:  # Can move LEFT
            valid_actions.append(LEFT)
        if col < BOARD_SIDE - 1:  # Can move RIGHT
            valid_actions.append(RIGHT)

        return valid_actions

    # neighbor resulting from applying action
    def get_neighbor(self, node, action):
        return self.transition_model.apply_action(node, action)

    # get all neighbors for the given node
    def get_neighbors(self, node):
        neighbors = []
        for action in self.get_valid_actions(node):
            neighbor = self.get_neighbor(node, action)
            if neighbor:
                neighbors.append(neighbor)
        return neighbors

    # get the cost of the action (each move costs 1)
    def get_cost(self, node, action, successor):
        return 1


