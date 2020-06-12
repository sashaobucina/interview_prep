from collections import deque


class TreeNode:
    def __init__(self, val: int):
        self.val = val
        self.left = None
        self.right = None
        self.next = None


def connect(root: TreeNode) -> TreeNode:
    """
    # 116: Populate each next pointer to point to its next right node. 
    If there is no next right node, the next pointer should be set to None.

    Initially, all next pointers are set to NULL.
    """
    if not root:
        return None

    q = deque([root])
    while q:
        prev = q.pop()
        level_size = len(q)

        if prev.left:
            q.appendleft(prev.left)
        if prev.right:
            q.appendleft(prev.right)

        for i in range(level_size):
            curr = q.pop()
            prev.next = curr
            prev = curr

            if curr.left:
                q.appendleft(curr.left)
            if curr.right:
                q.appendleft(curr.right)

    return root


def connect_constant_mem(root: TreeNode):
    """
    Solution given perfect binary tree using constant memory.
    """
    leftmost = root

    while leftmost and leftmost.left:
        head = leftmost
        while head:
            head.left.next = head.right
            if head.next:
                head.right.next = head.next.left
            head = head.next

        leftmost = leftmost.left

    return root



if __name__ == "__main__":
    root = TreeNode(1)
    rootleft = TreeNode(2)
    rootright = TreeNode(3)
    rootleftleft = TreeNode(4)
    rootleftright = TreeNode(5)
    rootrightleft = TreeNode(6)
    rootrightright = TreeNode(7)

    root.left = rootleft
    root.right = rootright
    rootleft.left = rootleftleft
    rootleft.right = rootleftright
    rootright.left = rootrightleft
    rootright.right = rootrightright

    new_root = connect(root)

    assert new_root.left.next.val == 3
    assert new_root.left.left.next.val == 5
    assert new_root.right.left.next.val == 7

    print("Passed all tests!")