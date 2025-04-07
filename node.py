from constants import *

class Node:
    def __init__(self, tiles_list, is_initial=False, is_goal=False, parent=None, cause=None, value=0):
        self.parent = parent
        self.cause = cause
        self.value = value
        self.is_initial = is_initial
        self.is_goal = is_goal
        self.tiles_list = tiles_list
        self.set_node_board()


    def set_node_board(self):
        self.tiles_board = []
        #make a 3x3 board from the tiles_list
        for i in range(0, BOARD_SIZE , BOARD_SIDE):
            self.tiles_board.append(self.tiles_list[i:i + BOARD_SIDE])

    def display_as_board(self):
        for row in self.tiles_board:
            print(row)
        print()

