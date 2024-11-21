from collections import deque


class ColaDeque:
    def __init__(self):
        self.items = deque()

    def is_empty(self):
        return len(self.items) == 0

    def queue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.popleft()
        raise IndexError("Desencolar de una cola vacía")

    def front(self):
        if not self.is_empty():
            return self.items[0]
        raise IndexError("Cola vacía")

    def size(self):
        return len(self.items)