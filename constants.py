import math
from action import *

# for representation as a 2D board
BOARD_SIZE = 9
BOARD_SIDE = int(math.sqrt(BOARD_SIZE))

UP = "UP"
DOWN = "DOWN"
LEFT = "LEFT"
RIGHT = "RIGHT"
ACTIONS = [UP, DOWN, LEFT, RIGHT]

GOAL_STATE = [0, 1, 2, 3, 4, 5, 6, 7, 8]

BF_SEARCH = "BFS"
A_STAR = "A*"