from node import *
from constants import *

class Transiton_Model:

    def get_neighbors(self, node):
        neighbors = []
        for action in ACTIONS:
           neighbor = node.action(action)
           if neighbor is not None:
               neighbors.append(neighbor)
        return neighbors