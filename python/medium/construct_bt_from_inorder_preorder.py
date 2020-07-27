from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __eq__(self, other) -> bool:
        return (type(self) == type(other)) and (self.val == other.val) and (self.left == other.left) and \
            (self.right == other.right)


def build_tree(inorder: List[int], preorder: List[int]) -> TreeNode:
    """
    # 105: Given preorder and inorder traversal of a tree, construct the binary tree.

    NOTE: You may assume that duplicates do not exist in the tree.
    """
    def _build(start, end):
        if start > end:
            return None

        val = preorder.pop(0)
        root = TreeNode(val)

        idx = idx_map[val]

        root.left = _build(start, idx - 1)
        root.right = _build(idx + 1, end)

        return root

    idx_map = {v: i for i, v in enumerate(inorder)}
    return _build(0, len(preorder) - 1)


if __name__ == "__main__":
    # construct the expected result BT
    n5 = TreeNode(7)
    n4 = TreeNode(15)
    n3 = TreeNode(20, left=n4, right=n5)
    n2 = TreeNode(9)
    n1 = TreeNode(3, left=n2, right=n3)

    inorder, preorder = [9, 3, 15, 20, 7], [3, 9, 20, 15, 7]
    assert build_tree(inorder, preorder) == n1
    print("Passed all tests!")
