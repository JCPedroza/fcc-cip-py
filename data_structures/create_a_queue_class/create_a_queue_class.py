class Queue:
    def __init__(self, lst=None):
        self.list = lst if lst else []

    def enqueue(self, item):
        self.list.append(item)
        return self

    def dequeue(self):
        return self.list.pop(0) if self.list else None

    def front(self):
        return self.list[0] if self.list else None

    def clear(self):
        self.list = []
        return self

    def is_empty(self):
        return len(self) == 0

    def print(self):
        print(self)
        return self

    def size(self):
        return len(self)

    def __len__(self):
        return len(self.list)

    def __str__(self):
        return str(self.list)
