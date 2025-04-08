from constants import *

class Node:
    def __init__(self, tiles_list, is_initial=False, is_goal=False, parent=None, cause=None, value=0, number_tile=None):
        self.parent = parent
        self.cause = cause
        self.value = value
        self.is_initial = is_initial
        self.is_goal = is_goal
        self.number_tile_that_moved = number_tile
        self.tiles_list = tiles_list
        self.tiles_board = []




    def __hash__(self):
        return hash(tuple(self.tiles_list))  #for the set

    def __eq__(self, other):
        if not isinstance(other, Node):
            return False
        return self.tiles_list == other.tiles_list

    def set_node_board(self): # used for nice display for debugging
        self.tiles_board = []
        for i in range(0, BOARD_SIZE , BOARD_SIDE):  # create the board 3X3
            self.tiles_board.append(self.tiles_list[i:i + BOARD_SIDE])

    # display for debugging
    def display_as_board(self):
        self.set_node_board()
        for row in self.tiles_board:
            print(row)
        print()

    # display for assignment
    def display_as_moved_tile(self):
        print(self.number_tile_that_moved)


    def action(self, cause ):
        row, col = self.get_blank_tile_position()
        new_row = row  #of the number tile
        new_col = col  #of the number tile
        if cause == UP:
                new_row = row-1
        elif cause == DOWN:
                new_row = row+1
        elif cause == LEFT:
                new_col = col-1
        elif cause == RIGHT:
                new_col = col+1

        if self.is_valid_coordinate(new_row, new_col): #the new row and col
            neighbor = Node(self.tiles_list.copy(), parent=self, cause=cause, value=self.value + 1)
            neighbor.swap_tiles(row, col, new_row, new_col)
            tile_number = neighbor.tiles_list[row * BOARD_SIDE + col]
            neighbor.set_number_tile_that_moved(tile_number)
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


    def get_value(self):
        return self.value


    def set_number_tile_that_moved(self, number_tile):
        self.number_tile_that_moved = number_tile


    def get_parent(self):
        return self.parent

