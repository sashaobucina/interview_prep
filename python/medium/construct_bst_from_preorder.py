from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __eq__(self, other) -> bool:
        return (type(self) == type(other)) and (self.val == other.val) and (self.left == other.left) and \
            (self.right == other.right)


def bst_from_preorder(preorder: List[int]) -> TreeNode:
    """
    # 1008: Return the root node of a BST that matches the given preorder traversal.

    (Recall that a BST is a binary tree where for every node, any descendant of node.left has a 
    value < node.val, and any descendant of node.right has a value > node.val. Also recall that a 
    preorder traversal displays the value of the node first, then traverses node.left, then traverses node.right.)

    It's guaranteed that for the given test cases there is always possible to find a BST with the given requirements.
    """
    if not preorder:
        return None

    def helper(prev, i):
        # exit early if reached end of all options
        if i == N - 1:
            return TreeNode(preorder[-1]), N

        curr, nxt = preorder[i], preorder[i + 1]
        root = TreeNode(curr)

        i += 1

        # check if need to add next to left, update increment
        if nxt < curr:
            root.left, i = helper(root.val, i)

        # if left exhausted all vals, exit with current root
        if i == N:
            return root, N

        # if root is first val, go to right by default
        if prev is None or preorder[i] < prev:
            root.right, i = helper(prev, i)

        return root, i

    N = len(preorder)
    return helper(None, 0)[0]


def bst_from_preorder_better(preorder: List[int]) -> TreeNode:
    def helper(lower=-float("inf"), upper=float("inf")):
        nonlocal idx

        if idx == N:
            return None

        val = preorder[idx]

        if val < lower or val > upper:
            return None

        idx += 1
        root = TreeNode(val)

        root.left = helper(lower, val)
        root.right = helper(val, upper)

        return root

    idx = 0
    N = len(preorder)

    return helper()


if __name__ == "__main__":
    # construct expected result BST
    n6 = TreeNode(12)
    n5 = TreeNode(7)
    n4 = TreeNode(1)
    n3 = TreeNode(10, right=n6)
    n2 = TreeNode(5, left=n4, right=n5)
    n1 = TreeNode(8, left=n2, right=n3)

    preorder = [8, 5, 1, 7, 10, 12]
    assert bst_from_preorder(preorder) == n1
    assert bst_from_preorder_better(preorder) == n1
    print("Passed all tests!")
