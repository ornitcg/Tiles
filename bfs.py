from transition_model import *
from constants import *
from node import *

class BFS:
    def __init__(self, start_node, goal_node):
        self.start_node = start_node
        self.goal_node = goal_node

    def bf_search(self):
        queue = []
        visited = set()
        queue.append(self.start_node)

        while queue:
            current_node = queue.pop(0)
            print("Current node:")
            current_node.display_as_board()
            if current_node.is_equal(self.goal_node):
                return current_node
            visited.add(current_node)
            queue.append(Transiton_Model().get_neighbors(current_node))
