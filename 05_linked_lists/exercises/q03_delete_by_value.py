"""
Question:
Add a delete_by_value(value) method to LinkedList that removes the
first node matching that value.

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

    def delete_by_value(self, value):
        if self.head is None:
            return

        if self.head.value == value:
            self.head = self.head.next
            return

        current = self.head
        while current.next is not None:
            if current.next.value == value:
                current.next = current.next.next
                return
            current = current.next

    def traverse(self):
        values = []
        current = self.head
        while current is not None:
            values.append(current.value)
            current = current.next
        return values


if __name__ == "__main__":
    ll = LinkedList()
    for v in [10, 20, 30, 40]:
        ll.insert_at_end(v)

    ll.delete_by_value(30)
    print(ll.traverse())  # [10, 20, 40]