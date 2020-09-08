class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __eq__(self, other):
        return type(self) == type(other) and self.val == other.val and self.left == other.left and self.right == other.right


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def sorted_list_to_BST(head: ListNode) -> TreeNode:
    """
    # 109: Given the head of a singly linked list where elements are sorted in ascending order, convert it 
    to a height balanced BST.

    For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the 
    two subtrees of every node never differ by more than 1.
    """
    l = []
    curr = head
    while curr:
        l.append(curr.val)
        curr = curr.next

    n = len(l)

    def helper(lo, hi):
        if lo > hi:
            return None
        if lo >= hi:
            return TreeNode(l[lo])

        mid = lo + (hi - lo) // 2
        root = TreeNode(l[mid])

        root.left = helper(lo, mid - 1)
        root.right = helper(mid + 1, hi)

        return root

    return helper(0, n - 1)


if __name__ == "__main__":
    # construct LL
    l5 = ListNode(9)
    l4 = ListNode(5, next=l5)
    l3 = ListNode(0, next=l4)
    l2 = ListNode(-3, next=l3)
    l1 = ListNode(-10, next=l2)

    # construct expected BT
    n5 = TreeNode(9)
    n4 = TreeNode(-3)
    n3 = TreeNode(5, right=n5)
    n2 = TreeNode(-10, right=n4)
    n1 = TreeNode(0, left=n2, right=n3)

    assert sorted_list_to_BST(l1) == n1

    print("Passed all tests!")
