import argparse
from bfs import *
from node import *
def get_tiles_from_user():
    parser = argparse.ArgumentParser(description="Process some tiles.")
    parser.add_argument('tiles', metavar='T', type=int, nargs='+',
                        help='the tiles initial order (numbers) separated by spaces')
    args = parser.parse_args()
    return args.tiles


def is_list_valid(tiles_list):
    # Check if the list contains the exact numbers from 0 to 8
    for i in tiles_list:
        if i < 0 or i > 8:
            return False
    tiles_set = set(tiles_list)
    # print("Tiles set:", tiles_set)  #TODO DEBUG REMOVE
    if len(tiles_set) != 9:
        return False
    return True


if __name__ == "__main__":
    # tiles_list = get_tiles_from_user()
    tiles_list = [2,3,6,8,7,1,5,0,4]  # Example input
    # print("Tiles list:", tiles_list)  #TODO DEBUG REMOVE
    if not is_list_valid(tiles_list):
        print("ERROR: Invalid list of tiles. Please provide a list of numbers from 0 to 8 next time. bye bye!")
        exit()

    start_node = Node(tiles_list, is_initial=True)
    start_node.display_as_board()
    print("Valid list of tiles.")

    bfs = BFS(start_node, Node(GOAL_STATE))
    final = bfs.bf_search()
    print("Final node:")
    final.display_as_board()