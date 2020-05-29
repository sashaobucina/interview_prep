from typing import List


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __eq__(self, other):
        return isinstance(other, ListNode) and self.val == other.val and (self.next == other.next)


def merge_two_lists(l1: ListNode, l2: ListNode) -> ListNode:
    """
    # 21: Merge two sorted linked lists and return it as a new list. 
    # The new list should be made by splicing together the nodes of the first two lists.
    """
    if not l1:
        return l2
    if not l2:
        return l1

    if l1.val < l2.val:
        head = l1
        l1 = l1.next
    else:
        head = l2
        l2 = l2.next

    curr = head
    while l1 or l2:
        if not l1:
            curr.next = l2
            return head
        if not l2:
            curr.next = l1
            return head

        if l1.val < l2.val:
            curr.next = l1
            curr = curr.next
            l1 = l1.next
        else:
            curr.next = l2
            curr = curr.next
            l2 = l2.next

    return head


def list_to_ll(lst: List[int]) -> ListNode:
    """ Helper function to convert lsit to linked list. """
    if not lst:
        return None

    head = ListNode(lst[0])
    curr = head
    for i in range(1, len(lst)):
        node = ListNode(lst[i])
        curr.next = node
        curr = curr.next

    return head


if __name__ == "__main__":
    l1 = list_to_ll([1, 2, 4])
    l2 = list_to_ll([1, 3, 4])
    expected = list_to_ll([1, 1, 2, 3, 4, 4])
    actual = merge_two_lists(l1, l2)
    assert expected == actual

    print("Passed all tests!")
