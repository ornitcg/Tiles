from priority_queue import *
from heuristic import *
from transition_model import *

class A_star:
    def __init__(self, state_space, start_node, heuristic_func):
        self.alg_name = A_STAR
        self.state_space = state_space
        self.start_node = start_node
        self.goal_node = state_space.get_goal_state()
        self.heuristic_func = heuristic_func
        self.tiles_path = []
        self.visited = set()
        self.min_heap = PriorityQueue()



    def a_star_search(self):
        priority = self.start_node.value + self.heuristic_func(self.start_node)
        self.min_heap.add_or_update(self.start_node, priority)

        while not self.min_heap.is_empty():
            current_node = self.min_heap.pop()
            if current_node in self.visited:  # check if this was already expanded
                continue
            self.visited.add(current_node)

            if self.state_space.is_goal_state(current_node):
                self.track_path(current_node)
                return current_node

            neighbors = self.state_space.get_neighbors(current_node)
            # add neighbors to the heap
            for neighbor in neighbors:
                if neighbor not in self.visited:
                    priority = neighbor.value + self.heuristic_func(neighbor)
                    self.min_heap.add_or_update(neighbor, priority)

    def track_path(self, goal):
        # fill tiles path with tile that moved and fill it as a stack
        current = goal
        while current.parent is not None:
            self.tiles_path.insert(0, current.number_tile_that_moved)
            current = current.get_parent()



    def get_name(self):
        return self.alg_name

    def get_visited_nodes_count(self):
        return len(self.visited)

    def stack_nodes(self, final):
        # stack nodes from goal node
        current = final
        path = []
        while current:
            path.insert(0, current)
            current = current.get_parent()
        return path