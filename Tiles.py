import argparse
from bfs import *
from node import *
from huristic import *
from a_star import *
import time



def get_tiles_from_user():
    parser = argparse.ArgumentParser(description="Process some tiles.")
    parser.add_argument('tiles', metavar='T', type=int, nargs='+',
                        help='the tiles initial order (numbers) separated by spaces')
    args = parser.parse_args()
    return args.tiles


# Checks if the list of tiles is valid:
# - Contains exactly 9 numbers
# - Numbers are exactly 0 to 8
def is_list_valid(tiles_list):
    # Check if the list contains exactly 9 numbers
    if len(tiles_list) != 9:
     raise ValueError("Number of tiles must be 9")
     # Check if the list contains the exact numbers from 0 to 8
    for i in tiles_list:
        if i < 0 or i > 8:
            raise ValueError("Tiles must be numbers from 0 to 8")
    tiles_set = set(tiles_list)
    # check that it does not contain duplicates
    if len(tiles_set) != 9:
        raise ValueError("Tiles must not contain duplicates")
    return True


def display_output(alg, last_node):
    print("1. Algorithm: ", alg.get_name())
    print("2. Number of expanded nodes: ", alg.get_visited_nodes_count())
    print("3. Path of moves: ", end=' ')
    if last_node is None:
        print("No solution found.")
    else:
        # stack nodes from goal node
        solution_list = alg.stack_nodes(last_node)
        for node in solution_list:
            node.display_as_moved_tile()
            # node.display_as_board()



# Entry point of the program
if __name__ == "__main__":
    tiles_list = get_tiles_from_user()  # comment this and uncomment one of the next lines to test
    # tiles_list = [2,3,6,8,7,1,5,0,4]  # Example input  # no solution found
    # tiles_list = [2,0,6,8,7,1,5,3,4]  # Example input  # has solution
    # tiles_list = [0,6,3,8,7,1,5,2,4]  # Example input  # has solution

    # print("Tiles list:", tiles_list)  #TODO DEBUG REMOVE
    try:
        if is_list_valid(tiles_list):
            start_node = Node(tiles_list, is_initial=True)
            goal_state = Node(GOAL_STATE, is_goal=True)

            # run the BFS algorithm
            bfs = BFS(start_node, goal_state)
            last_node = bfs.breadth_first_search()
            display_output(bfs, last_node)

            print() #line down

            # run the A* algorithm
            a_star = A_star(start_node, goal_state, heuristic)
            last_node = a_star.a_star_search()
            display_output(a_star, last_node)

    except ValueError as e:
        print(f"ERROR: Invalid list of tiles : {e}")
        exit()



