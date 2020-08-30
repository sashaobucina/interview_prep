from typing import List
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def find_leaves(root: TreeNode) -> List[List[int]]:
    """
    # 366: Given a binary tree, collect a tree's nodes as if you were doing this:
        - Collect and remove all leaves, repeat until the tree is empty.
    """
    if not root:
        return []

    def bfs(root):
        leaves = []

        q = deque([(None, root, False)])
        while q:
            parent, curr, is_left = q.pop()

            if not curr.left and not curr.right:
                leaves.append(curr.val)

                # disconnect from tree
                if parent:
                    if is_left:
                        parent.left = None
                    else:
                        parent.right = None

            if curr.left:
                q.appendleft((curr, curr.left, True))
            if curr.right:
                q.appendleft((curr, curr.right, False))

        return leaves

    res = []
    while root.left or root.right:
        res.append(bfs(root))

    res.append([root.val])
    return res


if __name__ == "__main__":
    # construct BT for testing
    n5 = TreeNode(5)
    n4 = TreeNode(4)
    n3 = TreeNode(3)
    n2 = TreeNode(2, left=n4, right=n5)
    n1 = TreeNode(1, left=n2, right=n3)

    assert find_leaves(n1) == [[3, 4, 5], [2], [1]]
    assert n1.left is None and n1.right is None

    print("Passed all tests!")
