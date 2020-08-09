from collections import deque, defaultdict


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def path_sum_naive(root: TreeNode, _sum: int) -> int:
    """
    # 437: You are given a binary tree in which each node contains an integer value.

    Find the number of paths that sum to a given value.

    The path does not need to start or end at the root or a leaf, but it must go downwards 
    (traveling only from parent nodes to child nodes).

    The tree has no more than 1,000 nodes and the values are in the range -1,000,000 to 1,000,000.

    Time complexity: O(2^n)
    Space complexity: O(n)
    """
    if not root:
        return 0

    def helper(node, _sum):
        if _sum == 0 and not node:
            return 1

        if not node:
            return 0

        left = 0
        if node.left:
            left = helper(node.left, _sum - node.left.val)

        right = 0
        if node.right:
            right = helper(node.right, _sum - node.right.val)

        return (left + right + 1) if _sum == 0 else (left + right)

    paths = 0
    q = deque([root])
    while q:
        curr = q.pop()
        paths += helper(curr, _sum - curr.val)

        if curr.left:
            q.appendleft(curr.left)
        if curr.right:
            q.appendleft(curr.right)

    return paths


def path_sum(root: TreeNode, _sum: int) -> int:
    """
    Same technique used in to #560 to find all the continuous subarrays in an array that sum up to a target value.

    Time complexity: O(n)
    Space complexity: O(n)
    """
    count, k = 0, _sum

    d = defaultdict(int)
    d[0] = 1

    def preorder(node: TreeNode, curr_sum: int):
        nonlocal count
        if not node:
            return

        curr_sum += node.val

        count += d[curr_sum - k]

        d[curr_sum] += 1

        preorder(node.left, curr_sum)
        preorder(node.right, curr_sum)

        d[curr_sum] -= 1

    preorder(root, 0)
    return count


if __name__ == "__main__":
    # construct BT
    n9 = TreeNode(11)
    n8 = TreeNode(1)
    n7 = TreeNode(-2)
    n6 = TreeNode(3)
    n5 = TreeNode(2, right=n8)
    n4 = TreeNode(3, left=n6, right=n7)
    n3 = TreeNode(-3, right=n8)
    n2 = TreeNode(5, left=n4, right=n5)
    n1 = TreeNode(10, left=n2, right=n3)

    assert path_sum_naive(n1, 8) == 3
    assert path_sum(n1, 8) == 3

    print("Passed all tests!")
