"""
Question:
Implement a Queue class with enqueue, dequeue, peek, and is_empty
methods, using collections.deque internally for O(1) operations on
both ends.

Topic     : Queues
Source    : freeCodeCamp DSA Course
Difficulty: Easy
"""

from collections import deque


class Queue:
    def __init__(self):
        self.items = deque()

    def enqueue(self, value):
        self.items.append(value)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        return self.items.popleft()

    def peek(self):
        if self.is_empty():
            raise IndexError("peek from empty queue")
        return self.items[0]

    def is_empty(self):
        return len(self.items) == 0


if __name__ == "__main__":
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    print(q.peek())     # 1
    print(q.dequeue())  # 1
    print(q.dequeue())  # 2
    print(q.is_empty()) # False