from transition_model import *
from constants import *
from node import *

class BFS:
    def __init__(self, start_node, goal_node):
        self.start_node = start_node
        self.goal_node = goal_node
        self.tiles_path = []

    def breadth_first_search(self):
        queue = []
        visited = set()
        queue.append(self.start_node)

        while queue:
            current_node = queue.pop(0)
            if current_node in visited:  # check if this was already expanded
                continue
            visited.add(current_node)
            if current_node == self.goal_node:
                self.track_path(current_node)
                return current_node
            queue.extend(Transiton_Model().get_neighbors(current_node))




    def track_path(self, goal):
        #fill tiles path with tile that moved and fill it as a stack
        current = goal
        while current.parent is not None:
            self.tiles_path.insert(0, current.number_tile_that_moved)
            current = current.get_parent()

    def stack_nodes(self, final):
        #stack nodes from goal node
        current = final
        path = []
        while current.parent is not None:
            path.insert(0, current)
            current = current.get_parent()
        return path