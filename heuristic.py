from constants import *


class Heuristic:
    def __init__(self, goal_state=GOAL_STATE):
        self.goal_state = goal_state


    #  Takes the maximum between row and column distances for each tile.
    #  returns the sum of these maximum distances.
    #  This is not Manhattan distance, but  is inspired by it.
    def max_dim_dist_heuristic(self, state_node):
        state = state_node.get_tiles_list()
        total_distance = 0
        board_side = BOARD_SIDE

        for i in range(BOARD_SIZE):
            val = state[i]
            if val != 0:  # Skip the blank tile
                # Find position of this tile in goal state
                goal_idx = goal_state.index(val)

                # Calculate current and goal row/col positions
                current_row = i // board_side
                current_col = i % board_side
                goal_row = goal_idx // board_side
                goal_col = goal_idx % board_side

                # Get row and column distances
                row_distance = abs(current_row - goal_row)
                col_distance = abs(current_col - goal_col)

                # Take maximum of row and column distances
                max_distance = max(row_distance, col_distance)
                total_distance += max_distance
        return total_distance