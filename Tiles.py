import argparse
from bfs import *
from node import *
from heuristic import *
from a_star import *
from state_space import *
from cost_func import *

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
    print("Algorithm: ", alg.get_name())
    print("Path : ", end=' ')
    if last_node is None:
        print("No solution found.")
    else:
        # stack nodes from goal node
        solution_list = alg.stack_nodes(last_node)
        for node in solution_list:
            node.display_as_moved_tile()
            # node.display_as_board()
    print()
    print("Path length: ", len(alg.tiles_path))
    print("Expanded: ", alg.get_visited_nodes_count())


# Entry point of the program
if __name__ == "__main__":
    tiles_list = get_tiles_from_user()  # comment this and uncomment one of the next lines to test
    # tiles_list = [2,3,6,8,7,1,5,0,4]  # Example input  # no solution found
    # tiles_list = [2,0,6,8,7,1,5,3,4]  # Example input  # has solution
    # tiles_list = [1,0,2,3,4,8,6,5,7]  # Example input  # has solution 7 steps

    # print("Tiles list:", tiles_list)  #TODO DEBUG REMOVE
    try:
        if is_list_valid(tiles_list):
            # start_node = Node(tiles_list, is_initial=True)
            state_space = State_Space()
            start_state = state_space.get_initial_state(tiles_list)
            goal_state = state_space.get_goal_state()


            # run the BFS algorithm
            # bfs = BFS(state_space, start_state)  # TODO uncomment
            # last_node = bfs.breadth_first_search()  # TODO uncomment
            # display_output(bfs, last_node)  # TODO uncomment

            print() #line down

            heuristic = Heuristic( goal_state)
            cost_func = Cost_Function()
            # run the A* algorithm
            a_star = A_star(state_space, start_state, heuristic.manhattan_plus_linear_conflict, cost_func)
            last_node = a_star.a_star_search()
            display_output(a_star, last_node)

    except ValueError as e:
        print(f"ERROR: Invalid list of tiles : {e}")
        exit()




