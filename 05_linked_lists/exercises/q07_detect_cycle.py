"""
Question:
Write a function that detects whether a linked list has a cycle
(a node's "next" eventually loops back to an earlier node), using
Floyd's tortoise and hare algorithm.

Topic     : Linked Lists, Two-Pointer Technique
Source    : freeCodeCamp DSA Course
Difficulty: Medium
"""


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


def has_cycle(head):
    slow = head
    fast = head

    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            return True

    return False


if __name__ == "__main__":
    # Build a list WITHOUT a cycle
    a = Node(1)
    b = Node(2)
    c = Node(3)
    a.next = b
    b.next = c
    print(has_cycle(a))  # False

    # Build a list WITH a cycle (c points back to b)
    c.next = b
    print(has_cycle(a))  # True