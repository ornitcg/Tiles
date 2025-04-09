import heapq

class PriorityQueue:
    def __init__(self):
        self.heap = []
        self.entry_finder = {}  # Map of items to their entries
        self.counter = 0  # Unique sequence count to break ties

    def add_or_update(self, item, priority):
        """Add a new item or update the priority of an existing item."""
        if item in self.entry_finder:
            self.remove(item)
        count = self.counter
        self.counter += 1
        entry = [priority, count, item]
        self.entry_finder[item] = entry
        heapq.heappush(self.heap, entry)


    def remove(self, item):
        """Mark an existing item as REMOVED."""
        entry = self.entry_finder.pop(item)
        entry[-1] = None

    def pop(self):
        """Remove and return the lowest priority item."""
        while self.heap:
            priority, count, item = heapq.heappop(self.heap)
            if item is not None:
                del self.entry_finder[item]
                return item
        raise KeyError("pop from an empty priority queue")

    def is_empty(self):
        """Check if the priority queue is empty."""
        return not self.entry_finder