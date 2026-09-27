"""
Question:
Extend the LinkedList class with insert_at_beginning and
insert_at_position(value, position) methods.

Topic     : Linked Lists
Source    : freeCodeCamp DSA Course
Difficulty: Medium
"""


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = new_node

    def insert_at_beginning(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def insert_at_position(self, value, position):
        if position == 0:
            self.insert_at_beginning(value)
            return

        new_node = Node(value)
        current = self.head
        for _ in range(position - 1):
            if current is None:
                raise IndexError("Position out of range")
            current = current.next

        new_node.next = current.next
        current.next = new_node

    def traverse(self):
        values = []
        current = self.head
        while current is not None:
            values.append(current.value)
            current = current.next
        return values


if __name__ == "__main__":
    ll = LinkedList()
    ll.insert_at_end(10)
    ll.insert_at_end(30)
    ll.insert_at_beginning(5)
    ll.insert_at_position(20, 2)
    print(ll.traverse())  # [5, 10, 20, 30]