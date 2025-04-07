from constants import *

class Node:
    def __init__(self, tiles_list, is_initial=False, is_goal=False, parent=None, cause=None, value=0):
        self.parent = parent
        self.cause = cause
        self.value = value
        self.is_initial = is_initial
        self.is_goal = is_goal
        self.tiles_list = tiles_list
        # self.set_node_board()


    def set_node_board(self):
        self.tiles_board = []
        #make a 3x3 board from the tiles_list
        for i in range(0, BOARD_SIZE , BOARD_SIDE):
            self.tiles_board.append(self.tiles_list[i:i + BOARD_SIDE])

    def display_as_board(self):
        for row in self.tiles_board:
            print(row)
        print()



    def action(self, cause ):
        row, col = self.get_blank_tile_position()
        new_row = row
        new_col = col
        if cause == UP:
                new_row = row-1
        elif cause == DOWN:
                new_row = row+1
        elif cause == LEFT:
                new_col = col-1
        elif cause == RIGHT:
                new_col = col+1

        if self.is_valid_coordinate(new_row, new_col): #the new row and col
            neighbor = Node(self.tiles_list, parent=self, cause=cause, value=self.value + 1)
            neighbor.swap_tiles(row, col, new_row, new_col)
            return neighbor
        else:
            return None



    def is_valid_coordinate(self, x, y):
        return 0 <= x < BOARD_SIDE and 0 <= y < BOARD_SIDE

    def get_blank_tile_position(self):
        for i in range(BOARD_SIZE):
            if self.tiles_list[i] == 0:
                row = i // BOARD_SIDE
                col = i % BOARD_SIDE
                return row, col
        return None

    def swap_tiles(self, row1, col1, row2, col2):
        # Swap the tiles at the given coordinates
        index1 = row1 * BOARD_SIDE + col1
        index2 = row2 * BOARD_SIDE + col2
        val1 = self.tiles_list[index1]
        val2 = self.tiles_list[index2]
        self.tiles_list[index1] = val2
        self.tiles_list[index2] = val1