from typing import List
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def vertical_traversal(root: TreeNode) -> List[List[int]]:
    """
    # 987: Given a binary tree, return the vertical order traversal of its nodes values.

    For each node at position (X, Y), its left and right children respectively will be at positions 
    (X-1, Y-1) and (X+1, Y-1).

    Running a vertical line from X = -infinity to X = +infinity, whenever the vertical line touches 
    some nodes, we report the values of the nodes in order from top to bottom (decreasing Y coordinates).

    If two nodes have the same position, then the value of the node that is reported first is the value 
    that is smaller.

    Return an list of non-empty reports in order of X coordinate.

    Every report will have a list of values of nodes.

    NOTE: Sol'n implements global, three-dimensional sorting of (col, row, value) using BFS, respectively.
    """
    # 1) construct global node list
    node_list = []

    def bfs(root):
        q = deque([(root, 0, 0)])
        while q:
            node, row, col = q.pop()
            if node:
                node_list.append((col, row, node.val))
                q.appendleft((node.left, row + 1, col - 1))
                q.appendleft((node.right, row + 1, col + 1))

    bfs(root)

    # 2) sort the global node list
    node_list.sort()

    # 3) retrieve sorted results partitioned but column index
    i = 0
    ans, curr_level = [], []

    while i < len(node_list):
        curr_level = []
        while i < len(node_list) - 1 and (node_list[i][0] == node_list[i + 1][0]):
            curr_level.append(node_list[i][2])
            i += 1

        curr_level.append(node_list[i][2])
        ans.append(curr_level)
        i += 1

    return ans


if __name__ == "__main__":
    # construct BT
    n5 = TreeNode(7)
    n4 = TreeNode(15)
    n3 = TreeNode(20, left=n4, right=n5)
    n2 = TreeNode(9)
    n1 = TreeNode(3, left=n2, right=n3)

    assert vertical_traversal(n1) == [[9], [3, 15], [20], [7]]

    print("Passed all tests!")
