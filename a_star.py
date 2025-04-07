class A_star:
    def __init__(self, start, goal):
        self.start = start
        self.goal = goal
        self.open_set = set()
        self.closed_set = set()
        self.g_score = {}
        self.f_score = {}
        self.came_from = {}

    def heuristic(self, a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    def reconstruct_path(self, current):
        total_path = [current]
        while current in self.came_from:
            current = self.came_from[current]
            total_path.append(current)
        return total_path[::-1]  # Return reversed path