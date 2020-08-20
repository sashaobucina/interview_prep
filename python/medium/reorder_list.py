class ListNode:
    def __init__(self, val=0, nxt=None):
        self.val = val
        self.next = nxt

    def __eq__(self, other):
        return (type(self) == type(other)) and (self.val == other.val) and (self.next == other.next)


def reorder_list(head: ListNode) -> None:
    """
    # 143: Given a singly linked list L: L0→L1→…→Ln-1→Ln,
    reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…

    You may not modify the values in the list's nodes, only nodes itself may be changed.
    """
    if not head:
        return None

    # get the middle node
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # reverse the second part of the list
    prev, curr = None, slow
    while curr:
        tmp = curr.next
        curr.next = prev
        prev, curr = curr, tmp

    # merge the two lists, stepping through each one by one
    curr1, curr2 = head, prev
    while curr2.next:
        tmp = curr1.next
        curr1.next = curr2
        curr1 = tmp

        tmp = curr2.next
        curr2.next = curr1
        curr2 = tmp


if __name__ == "__main__":
    # construct original LL
    l5 = ListNode(5)
    l4 = ListNode(4, l5)
    l3 = ListNode(3, l4)
    l2 = ListNode(2, l3)
    l1 = ListNode(1, l2)

    # construct expected resulting LL
    _l5 = ListNode(3)
    _l4 = ListNode(4, _l5)
    _l3 = ListNode(2, _l4)
    _l2 = ListNode(5, _l3)
    _l1 = ListNode(1, _l2)

    reorder_list(l1)
    assert l1 == _l1

    print("Passed all tests!")
