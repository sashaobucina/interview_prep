from typing import List
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def vertical_order(root: TreeNode) -> List[List[int]]:
    """
    # 314: Given a binary tree, return the vertical order traversal of its nodes' values. (ie, from top to bottom, column by column).

    If two nodes are in the same row and column, the order should be from left to right.
    """
    if not root:
        return []

    ans = deque([[]])
    left, right = 0, 0

    q = deque([(root, 0)])
    while q:
        # traverse level by level
        for i in range(len(q)):
            curr, x = q.pop()

            if curr.left:
                q.appendleft((curr.left, x - 1))
            if curr.right:
                q.appendleft((curr.right, x + 1))

            if x == 0:
                ans[left].append(curr.val)
            elif x < 0:
                if abs(x) > left:
                    ans.appendleft([])
                    left += 1

                ans[x + left].append(curr.val)
            else:
                if x > right:
                    ans.append([])
                    right += 1

                ans[left + x].append(curr.val)

    return list(ans)


if __name__ == "__main__":
    # construct BT
    n5 = TreeNode(7)
    n4 = TreeNode(15)
    n3 = TreeNode(20, left=n4, right=n5)
    n2 = TreeNode(9)
    n1 = TreeNode(3, left=n2, right=n3)

    assert vertical_order(n1) == [[9], [3, 15], [20], [7]]

    print("Passed all tests!")
