"""
Question:
Write a function that takes the head of a linked list and returns its
length (number of nodes), without using a built-in len().

Topic     : Linked Lists
Source    : freeCodeCamp DSA Course
Difficulty: Easy
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


def get_length(head):
    count = 0
    current = head
    while current is not None:
        count += 1
        current = current.next
    return count


if __name__ == "__main__":
    head = build_sample_list([1, 2, 3, 4, 5])
    print(get_length(head))  # 5