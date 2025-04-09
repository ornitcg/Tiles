from transition_model import *
from constants import *
from node import *

class BFS:
    def __init__(self, state_space, start_node):
        self.alg_name = BF_SEARCH
        self.state_space = state_space
        self.start_node = start_node
        self.tiles_path = []
        self.visited = set()
        self.queue = []

    def breadth_first_search(self):
        self.queue.append(self.start_node)

        while self.queue:
            current_node = self.queue.pop(0)
            if current_node in self.visited:  # check if this was already expanded
                continue
            self.visited.add(current_node)
            if current_node == self.state_space.get_goal_state():
                self.track_path(current_node)
                return current_node
            self.queue.extend(self.state_space.get_neighbors(current_node))




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
        while current:
            path.insert(0, current)
            current = current.get_parent()
        return path

    def get_visited_nodes_count(self):
        return len(self.visited)

    def get_name(self):
        return self.alg_name