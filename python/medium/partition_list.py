class ListNode:
    def __init__(self, val=0, nxt=None):
        self.val = val
        self.next = nxt

    def __eq__(self, other):
        return (type(self) == type(other)) and (self.val == other.val) and (self.next == other.next)


def partition(head: ListNode, x: int) -> ListNode:
    """
    # 86: Given a linked list and a value x, partition it such that all nodes less than x come before 
    nodes greater than or equal to x.

    You should preserve the original relative order of the nodes in each of the two partitions.
    """
    dummy = ListNode()
    dummy.next = head

    right_dummy = ListNode()
    right = right_dummy

    prev, curr = dummy, head
    while curr:
        if curr.val < x:
            prev = curr
            curr = curr.next
        else:
            tmp = curr.next
            prev.next = tmp

            right.next = curr
            right = right.next

            curr.next = None
            curr = tmp

    # connect left and right sides of LL
    prev.next = right_dummy.next
    return dummy.next


if __name__ == "__main__":
    # construct original LL
    l6 = ListNode(2)
    l5 = ListNode(5, nxt=l6)
    l4 = ListNode(2, nxt=l5)
    l3 = ListNode(3, nxt=l4)
    l2 = ListNode(4, nxt=l3)
    l1 = ListNode(1, nxt=l2)

    # construct expected LL
    _l6 = ListNode(5)
    _l5 = ListNode(3, nxt=_l6)
    _l4 = ListNode(4, nxt=_l5)
    _l3 = ListNode(2, nxt=_l4)
    _l2 = ListNode(2, nxt=_l3)
    _l1 = ListNode(1, nxt=_l2)

    assert partition(l1, 3) == _l1

    print("Passed all tests!")
