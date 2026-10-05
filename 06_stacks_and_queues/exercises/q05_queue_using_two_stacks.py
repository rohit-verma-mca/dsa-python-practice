"""
Question:
Implement a queue (enqueue/dequeue) using only two stacks internally,
not a deque or list directly as a queue.

Topic     : Stacks, Queues
Source    : freeCodeCamp DSA Course
Difficulty: Medium
"""


class QueueUsingStacks:
    def __init__(self):
        self.stack_in = []
        self.stack_out = []

    def enqueue(self, value):
        self.stack_in.append(value)

    def dequeue(self):
        if not self.stack_out:
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())
        if not self.stack_out:
            raise IndexError("dequeue from empty queue")
        return self.stack_out.pop()


if __name__ == "__main__":
    q = QueueUsingStacks()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    print(q.dequeue())  # 1
    print(q.dequeue())  # 2
    q.enqueue(4)
    print(q.dequeue())  # 3
    print(q.dequeue())  # 4