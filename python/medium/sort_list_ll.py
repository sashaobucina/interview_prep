class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __eq__(self, other):
        return (type(self) == type(other)) and (self.val == other.val) and (self.next == other.next)


def sort_list(head: ListNode) -> ListNode:
    """
    # 148: Sort a linked list in O(n log n) time using constant space complexity.

    NOTE: This implementation uses a recursive mergesort (top-down), so space complextity is O(n).
    """
    if not head or not head.next:
        return head

    slow, fast = head, head.next
    while slow and (fast and fast.next):
        slow = slow.next
        fast = fast.next.next

    mid = slow.next
    slow.next = None

    head1 = sort_list(head)
    head2 = sort_list(mid)

    return _merge(head1, head2)


def _merge(l1: ListNode, l2: ListNode) -> ListNode:
    cur1, cur2 = l1, l2

    dummy = ListNode()
    cur = dummy

    while cur1 and cur2:
        if cur1.val <= cur2.val:
            cur.next = ListNode(cur1.val)
            cur1 = cur1.next
        else:
            cur.next = ListNode(cur2.val)
            cur2 = cur2.next
        cur = cur.next

    cur.next = cur1 if cur1 else cur2
    return dummy.next


if __name__ == "__main__":
    # construct original linked list
    l4 = ListNode(3)
    l3 = ListNode(1, next=l4)
    l2 = ListNode(2, next=l3)
    l1 = ListNode(4, next=l2)

    # construct expected linked list
    e4 = ListNode(4)
    e3 = ListNode(3, next=e4)
    e2 = ListNode(2, next=e3)
    e1 = ListNode(1, next=e2)

    assert sort_list(head=l1) == e1

    print("Passed all tests!")
