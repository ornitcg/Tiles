from constants import *


class Heuristic:
    def __init__(self,  goal_state=GOAL_STATE):
        self.goal_state = goal_state


    #  Takes the maximum between row and column distances for each tile.
    #  returns the sum of these maximum distances.
    #  This is not Manhattan distance, but  is inspired by it.
    def max_dim_dist_heuristic(self, state_node):
        state_tiles = state_node.get_tiles_list()
        goal_tiles = self.goal_state.get_tiles_list()
        total_distance = 0
        board_side = BOARD_SIDE

        for i in range(BOARD_SIZE):
            val = state_tiles[i]
            if val != 0:  # Skip the blank tile
                # Find position of this tile in goal state
                goal_index = goal_tiles.index(val)

                # Calculate current and goal row/col positions
                current_row = i // board_side
                current_col = i % board_side
                goal_row = goal_index // board_side
                goal_col = goal_index % board_side

                # Get row and column distances
                row_distance = abs(current_row - goal_row)
                col_distance = abs(current_col - goal_col)

                # Take maximum of row and column distances
                max_distance = max(row_distance, col_distance)
                total_distance += max_distance
        return total_distance

    def manhattan_distance_heuristic(self, state_node):
        state_tiles = state_node.get_tiles_list()
        goal_tiles = self.goal_state.get_tiles_list()
        total_distance = 0
        board_side = BOARD_SIDE

        for i in range(BOARD_SIZE):
            val = state_tiles[i]
            if val != 0:  # Skip the blank tile
                # Find position of this tile in goal state
                goal_index = goal_tiles.index(val)

                # Calculate current and goal row/col positions
                current_row = i // board_side
                current_col = i % board_side
                goal_row = goal_index // board_side
                goal_col = goal_index % board_side

                # Calculate Manhattan distance for this tile
                manhattan = abs(current_row - goal_row) + abs(current_col - goal_col)
                total_distance += manhattan

        return total_distance


    def max_dim_dist_with_linear_conflict(self, state_node):
        state = state_node.get_tiles_list()
        goal_state = self.goal_state.get_tiles_list()
        total_distance = 0
        # Part 1: Your existing max dimension distance calculation
        for i in range(BOARD_SIZE):
            val = state[i]
            if val != 0:  # Skip the blank tile
                # Find position of this tile in goal state
                goal_idx = goal_state.index(val)

                # Calculate current and goal row/col positions
                current_row = i // BOARD_SIZE
                current_col = i % BOARD_SIZE
                goal_row = goal_idx // BOARD_SIZE
                goal_col = goal_idx % BOARD_SIZE

                # Get row and column distances
                row_distance = abs(current_row - goal_row)
                col_distance = abs(current_col - goal_col)

                # Take maximum of row and column distances
                max_distance = max(row_distance, col_distance)
                total_distance += max_distance

        # Part 2: Add linear conflict penalties
        linear_conflicts = 0

        # Check row conflicts
        for row in range(BOARD_SIDE):
            row_tiles = []
            # Collect tiles in this row that belong to this row in the goal state
            for col in range(BOARD_SIDE):
                idx = row * BOARD_SIDE + col
                tile = state[idx]
                if tile != 0:
                    goal_idx = goal_state.index(tile)
                    goal_row = goal_idx // BOARD_SIDE
                    if goal_row == row:
                        goal_col = goal_idx % BOARD_SIDE
                        row_tiles.append((tile, col, goal_col))

            # Check for conflicts in this row
            for i in range(len(row_tiles)):
                for j in range(i + 1, len(row_tiles)):
                    tile1, pos1, goal_pos1 = row_tiles[i]
                    tile2, pos2, goal_pos2 = row_tiles[j]
                    # If tile1 is to the left of tile2 but should be to the right in goal state
                    if pos1 < pos2 and goal_pos1 > goal_pos2:
                        linear_conflicts += 1
                    # If tile1 is to the right of tile2 but should be to the left in goal state
                    elif pos1 > pos2 and goal_pos1 < goal_pos2:
                        linear_conflicts += 1

        # Check column conflicts - similar logic as rows
        for col in range(BOARD_SIDE):
            col_tiles = []
            for row in range(BOARD_SIDE):
                idx = row * BOARD_SIDE + col
                tile = state[idx]
                if tile != 0:
                    goal_idx = goal_state.index(tile)
                    goal_col = goal_idx % BOARD_SIDE
                    if goal_col == col:
                        goal_row = goal_idx // BOARD_SIDE
                        col_tiles.append((tile, row, goal_row))

            for i in range(len(col_tiles)):
                for j in range(i + 1, len(col_tiles)):
                    tile1, pos1, goal_pos1 = col_tiles[i]
                    tile2, pos2, goal_pos2 = col_tiles[j]
                    if pos1 < pos2 and goal_pos1 > goal_pos2:
                        linear_conflicts += 1
                    elif pos1 > pos2 and goal_pos1 < goal_pos2:
                        linear_conflicts += 1

        # Each linear conflict requires at least 2 additional moves
        total_distance += 2 * linear_conflicts

        return total_distance

    def count_linear_conflicts(self, state_node):
        conflicts = 0
        state_tiles = state_node.get_tiles_list()
        goal_tiles = self.goal_state.get_tiles_list()
        # Convert to 2D array for easier processing
        board = []
        for i in range(0, BOARD_SIZE, BOARD_SIDE):
            board.append(state_tiles[i:i + BOARD_SIDE])

        # Check each row
        for row in range(BOARD_SIDE):
            tiles_in_row = []
            # Collect tiles that belong in this row
            for col in range(BOARD_SIDE):
                tile = board[row][col]
                if tile != 0:  # Skip blank tile
                    # Get goal position
                    goal_idx = goal_tiles.index(tile)
                    goal_row = goal_idx // BOARD_SIDE

                    # If this tile belongs in this row, add it
                    if goal_row == row:
                        tiles_in_row.append((tile, col))

            # Check for conflicts in this row
            for i in range(len(tiles_in_row)):
                for j in range(i + 1, len(tiles_in_row)):
                    tile1, pos1 = tiles_in_row[i]
                    tile2, pos2 = tiles_in_row[j]

                    # Get goal positions
                    goal_idx1 = goal_tiles.index(tile1)
                    goal_idx2 = goal_tiles.index(tile2)
                    goal_col1 = goal_idx1 % BOARD_SIDE
                    goal_col2 = goal_idx2 % BOARD_SIDE

                    # Check if tiles are in conflict
                    if (goal_col1 > goal_col2 and pos1 < pos2) or (goal_col1 < goal_col2 and pos1 > pos2):
                        conflicts += 1

        # Check each column
        for col in range(BOARD_SIDE):
            tiles_in_col = []
            # Collect tiles that belong in this column
            for row in range(BOARD_SIDE):
                tile = board[row][col]
                if tile != 0:  # Skip blank tile
                    # Get goal position
                    goal_idx = goal_tiles.index(tile)
                    goal_col = goal_idx % BOARD_SIDE

                    # If this tile belongs in this column, add it
                    if goal_col == col:
                        tiles_in_col.append((tile, row))

            # Check for conflicts in this column
            for i in range(len(tiles_in_col)):
                for j in range(i + 1, len(tiles_in_col)):
                    tile1, pos1 = tiles_in_col[i]
                    tile2, pos2 = tiles_in_col[j]

                    # Get goal positions
                    goal_idx1 = goal_tiles.index(tile1)
                    goal_idx2 = goal_tiles.index(tile2)
                    goal_row1 = goal_idx1 // BOARD_SIDE
                    goal_row2 = goal_idx2 // BOARD_SIDE

                    # Check if tiles are in conflict
                    if (goal_row1 > goal_row2 and pos1 < pos2) or (goal_row1 < goal_row2 and pos1 > pos2):
                        conflicts += 1

        return conflicts


    def manhattan_plus_linear_conflict(self, state_node):
        state_tiles = state_node.get_tiles_list()
        goal_tiles = self.goal_state.get_tiles_list()
        total_distance = 0

        # First calculate the Manhattan distance
        for i in range(BOARD_SIZE):
            val = state_tiles[i]
            if val != 0:  # Skip the blank tile
                # Find position of this tile in goal state
                goal_idx = goal_tiles.index(val)

                # Calculate current and goal row/col positions
                current_row = i // BOARD_SIDE
                current_col = i % BOARD_SIDE
                goal_row = goal_idx // BOARD_SIDE
                goal_col = goal_idx % BOARD_SIDE

                # Add Manhattan distance for this tile
                manhattan = abs(current_row - goal_row) + abs(current_col - goal_col)
                total_distance += manhattan

        # Now calculate linear conflicts
        conflicts = self.count_linear_conflicts(state_node)

        # Each conflict requires 2 additional moves
        return total_distance + (2 * conflicts)
