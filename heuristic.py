from constants import *


class Heuristic:
    def __init__(self,  goal_state=GOAL_STATE):
        self.goal_state = goal_state

    def count_linear_conflicts(self, state_node):
        conflicts = 0
        goal_tiles = self.goal_state.get_tiles_list()

        # Convert to 2D array for easier processing
        board_2d = state_node.get_tiles_2D()
        goal_2d = self.goal_state.get_tiles_2D()


        # Check each row for tiles that belong in this row
        for board_row in board_2d:
            tiles_in_row = []
            row_index = board_2d.index(board_row)
            goal_row = goal_2d[row_index]
            # create list of tiles that belong to this row
            for tile in board_row:
                if tile != 0:  # Skip blank tile
                    if tile in goal_row :  #in the right row but not in the right position
                        tiles_in_row.append((tile, goal_row.index(tile))) #tuple of tile and its goal position

            conflicts += self.count_conflicts_in_list(tiles_in_row)


        # Check each column for tiles that belong in this column
        for col_ind in range(BOARD_SIDE):
            tiles_in_col = []
            # Collect tiles that belong in this column
            for board_row in board_2d:
                tile = board_row[col_ind]
                if tile != 0:  # Skip blank tile
                    # Get goal position
                    goal_index = goal_tiles.index(tile)
                    goal_col = goal_index % BOARD_SIDE

                    # If this tile belongs in this column, add it
                    if goal_col == col_ind:
                        tile_goal_row = goal_index // BOARD_SIDE
                        tiles_in_col.append((tile, tile_goal_row))  # tuple of tile and its goal position

            # Check for conflicts in this column
            conflicts += self.count_conflicts_in_list(tiles_in_col)

        return conflicts




    # The heuristic function that combines Manhattan distance and linear conflict
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


    def count_conflicts_in_list(self, state_tiles):
        conflicts = 0
        for i in range(len(state_tiles)):
            for j in range(i + 1, len(state_tiles)):
                # pos are the positions of the tiles in the goal row
                tile1, pos1 = state_tiles[i]
                tile2, pos2 = state_tiles[j]

                # Check if tiles are in conflict
                if pos1 > pos2:
                    conflicts += 1

        return conflicts

