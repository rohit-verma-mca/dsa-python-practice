"""
Question:
Implement a Node class and a LinkedList class with an insert_at_end
method and a method to print/traverse all values in order.

Topic     : Linked Lists
Source    : freeCodeCamp DSA Course
Difficulty: Easy
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
    ll.insert_at_end(20)
    ll.insert_at_end(30)
    print(ll.traverse())  # [10, 20, 30]