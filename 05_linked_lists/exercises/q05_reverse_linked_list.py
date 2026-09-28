"""
Question:
Write a function that reverses a singly linked list in place and
returns the new head.

Topic     : Linked Lists
Source    : freeCodeCamp DSA Course
Difficulty: Medium
"""


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


def build_sample_list(values):
    head = Node(values[0])
    current = head
    for v in values[1:]:
        current.next = Node(v)
        current = current.next
    return head


def print_list(head):
    values = []
    current = head
    while current is not None:
        values.append(current.value)
        current = current.next
    print(values)


def reverse_list(head):
    previous = None
    current = head

    while current is not None:
        next_node = current.next
        current.next = previous
        previous = current
        current = next_node

    return previous  # new head


if __name__ == "__main__":
    head = build_sample_list([1, 2, 3, 4, 5])
    print_list(head)             # [1, 2, 3, 4, 5]

    new_head = reverse_list(head)
    print_list(new_head)         # [5, 4, 3, 2, 1]