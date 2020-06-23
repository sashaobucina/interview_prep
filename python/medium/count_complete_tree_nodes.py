class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def count_nodes(root: TreeNode) -> int:
    return _count(root)


def _count(node: TreeNode) -> int:
    """
    # 222: Given a complete binary tree, count the number of nodes.

    NOTE: Definition of a complete binary tree from Wikipedia
        - In a complete binary tree every level, except possibly the last, is completely filled, and 
        all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes 
        inclusive at the last level h.
    """
    if not node:
        return 0

    left_h = _subtree_height(node)
    right_h = _subtree_height(node, left=False)

    if left_h == right_h:
        return (2 << (left_h - 1)) - 1

    return 1 + count_nodes(node.left) + count_nodes(node.right)


def _subtree_height(node: TreeNode, left=True) -> int:
    height = 1
    curr = node.left if left else node.right
    while curr:
        height += 1
        curr = curr.left if left else curr.right

    return height


if __name__ == "__main__":
    # build the complete binary tree
    n6 = TreeNode(6)
    n5 = TreeNode(5)
    n4 = TreeNode(4)
    n3 = TreeNode(3, left=n6)
    n2 = TreeNode(2, left=n4, right=n5)
    root = TreeNode(1, left=n2, right=n3)

    assert count_nodes(root) == 6

    print("Passed all tests!")
