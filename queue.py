class Node:
    def __init__(self, date, next=None):
        self.date = date
        self.next = next

class queue:
    def __init__(self) -> None:
        self.front = None
        self.rear = None
        self._size = 0

    def enqueue(self, item):
        self._size += 1
        node = Node(item)
        if self.rear is None:
            self.front = node
            self.rear = node
        else:
            self.rear.next = node
            self.rear = node

    def dequeue(self):
        if self.front is None:
            raise IndentationError("pop from empty queue")
        self._size -= 1
        temp = self.front
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        return temp.date
    
    def size(self):
        return self._size