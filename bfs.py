from transition_model import *
from constants import *

class BFS:
    def __init__(self, start_node, goal_node):
        self.start_node = start_node
        self.goal_node = goal_node

    def bf_search(self, start, goal):
        queue = []
        visited = set()
        queue.append(start)

        while queue:
            current_node = queue.pop(0)
            if current_node.is_equal(goal):
                return current_node
            visited.add(current_node)
            queue.append(Transiton_Model().get_neighbors(current_node))
