class BFS:
    def __init__(self, graph):
        self.graph = graph

    def bf_search(self, start):
        visited = set()
        queue = [start]
        visited.add(start)

