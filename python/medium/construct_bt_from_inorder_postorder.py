from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __eq__(self, other) -> bool:
        return (type(self) == type(other)) and (self.val == other.val) and (self.left == other.left) and \
            (self.right == other.right)


def build_tree(inorder: List[int], postorder: List[int]) -> TreeNode:
    """
    # 106: Given inorder and postorder traversal of a tree, construct the binary tree.

    NOTE: You may assume that duplicates do not exist in the tree.
    """
    def _build(start, end):
        if start > end:
            return None

        val = postorder.pop()
        root = TreeNode(val)

        in_idx = idx_map[val]

        root.right = _build(in_idx + 1, end)
        root.left = _build(start, in_idx - 1)

        return root

    idx_map = {v: i for i, v in enumerate(inorder)}
    return _build(0, len(postorder) - 1)


if __name__ == "__main__":
    # construct the expected result BT
    n5 = TreeNode(7)
    n4 = TreeNode(15)
    n3 = TreeNode(20, left=n4, right=n5)
    n2 = TreeNode(9)
    n1 = TreeNode(3, left=n2, right=n3)

    inorder, postorder = [9, 3, 15, 20, 7], [9, 15, 7, 20, 3]
    assert build_tree(inorder, postorder) == n1

    print("Passed all tests!")
