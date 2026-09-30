"""
Question:
Write a function that finds the middle node of a linked list in a
single pass, using the "slow and fast pointer" technique.

Topic     : Linked Lists, Two-Pointer Technique
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


def find_middle(head):
    slow = head
    fast = head

    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next

    return slow.value


if __name__ == "__main__":
    head = build_sample_list([1, 2, 3, 4, 5])
    print(find_middle(head))  # 3

    head2 = build_sample_list([1, 2, 3, 4, 5, 6])
    print(find_middle(head2)) # 4 (second middle for even-length lists)