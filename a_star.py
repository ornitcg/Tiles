from priority_queue import *
from huristic import *
from transition_model import *

class A_star:
    def __init__(self, start_node, goal_node, heuristic):
        self.alg_name = A_STAR
        self.start_node = start_node
        self.goal_node = goal_node
        self.tiles_path = []
        self.visited = set()
        self.min_heap = PriorityQueue()
        self.heuristic = heuristic



    def a_star_search(self):
        priority = self.start_node.value + self.heuristic(self.start_node.get_tiles_list(), self.goal_node.get_tiles_list())
        self.min_heap.add_or_update(self.start_node, 0)

        while not self.min_heap.is_empty():
            current_node = self.min_heap.pop()
            if current_node in self.visited:  # check if this was already expanded
                continue
            self.visited.add(current_node)
            if current_node == self.goal_node:
                self.track_path(current_node)
                return current_node
            neighbors = Transiton_Model().get_neighbors(current_node)
            # add neighbors to the heap
            for neighbor in neighbors:
                if neighbor not in self.visited:
                    priority = neighbor.value + self.heuristic(neighbor.get_tiles_list(), self.goal_node.get_tiles_list())

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