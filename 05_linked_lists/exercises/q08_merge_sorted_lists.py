"""
Question:
Write a function that merges two already-sorted linked lists into one
sorted linked list.

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


def merge_sorted_lists(head1, head2):
    dummy = Node(None)
    tail = dummy

    while head1 is not None and head2 is not None:
        if head1.value <= head2.value:
            tail.next = head1
            head1 = head1.next
        else:
            tail.next = head2
            head2 = head2.next
        tail = tail.next

    tail.next = head1 if head1 is not None else head2

    return dummy.next


if __name__ == "__main__":
    list1 = build_sample_list([1, 3, 5])
    list2 = build_sample_list([2, 4, 6])

    merged = merge_sorted_lists(list1, list2)
    print_list(merged)  # [1, 2, 3, 4, 5, 6]