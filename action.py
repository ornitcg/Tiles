


class Action:
    def __init__(self, direction, cost=1):
        self.direction = direction
        self.cost = cost

    # getters
    def get_direction(self):
        return self.direction

    def get_cost(self):
        return self.cost
